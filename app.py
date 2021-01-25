import logging
import sys
from logging.config import fileConfig

from config.config_loader import load_config
from config.double_click_config import DoubleClickConfig
from config.ftp_config import FTPConfig
from usecase.double_click_template import DoubleClickTemplate
from usecase.dto.google_geo_dto import GoogleGeoDTO
from usecase.dto.vpon_geo_dto import VponGeoDTO
from usecase.ftp_service import FTPService
from usecase.general_vpon_geo_service import GeneralVponGeoService
from usecase.generate_verify_spec_service import GenerateVerifySpecService
from usecase.hk_vpon_geo_service import HKVponGeoService
from usecase.verify_geo_service import VerifyGeoService
from util.file_util import read_csv, read_vpon_geo_excel, read_excel, save_file

logging.config.fileConfig('./logging_config.ini', disable_existing_loggers=False)
log = logging.getLogger(__name__)


def main(config_file_path, version):
    log.debug("main() config_file_path={} version={}".format(config_file_path, version))
    double_click_config = DoubleClickConfig.build(load_config(config_file_path, 'doubleclick-config'))

    # step 0 read google and vpon geo file
    google_geo_table = read_csv(double_click_config.google_geo_path)
    vpon_geo_table = read_vpon_geo_excel(double_click_config.vpon_geo_path)
    hk_geo_list = read_excel(double_click_config.hk_google_vpon_geo_path).values.tolist()
    # TODO read csv from verify spec

    # # step 1 build country code
    google_geo_dto_list = GoogleGeoDTO.build_google_geo_list(google_geo_table.values.tolist())
    country_code_set = set(google_geo_dto.country_code for google_geo_dto in google_geo_dto_list)
    vpon_geo_dto_list = VponGeoDTO.build_vpon_geo_list(vpon_geo_table.values.tolist())

    # # # step2 match
    vpon_geo_service = GeneralVponGeoService()
    country_code_set.remove('HK')
    vpon_geo_domain_list = [vpon_geo_service.generate(google_geo_dto_list, vpon_geo_dto_list, country_code) for
                            country_code
                            in list(country_code_set)]
    # # # general
    vpon_geo_domain_list = [vpon_geo_domain for row in vpon_geo_domain_list for vpon_geo_domain in
                            row]
    # hk
    hk_vpon_geo_service = HKVponGeoService()
    hk_vpon_geo_list = hk_vpon_geo_service.generate(hk_geo_list)
    #
    vpon_geo_domain_list = vpon_geo_domain_list+hk_vpon_geo_list
    log.info("build() vpon_geo_domain_list size={} google size={}".format(len(vpon_geo_domain_list),
                                                                          len(google_geo_dto_list)))
    verify_geo_service = VerifyGeoService()
    result = verify_geo_service.verify(vpon_geo_domain_list, read_csv(double_click_config.prebid_path).values.tolist())

    log.info("verify correct count={}, error list={}, id in prebid rate={}".format(result[0], result[1],
                                                                                   result[2],
                                                                                   ))

    s = GenerateVerifySpecService()
    result = s.generate(vpon_geo_domain_list)
    for row in result:
        print(row[0].__dict__, row[1])
    # save and export to repo
    conf_file_name = 'doubleclick-{}.conf'.format(version)
    double_click_template = DoubleClickTemplate()
    # save_file(conf_file_name, double_click_template.build(vpon_geo_domain_list))

    # ftp_service = FTPService(FTPConfig.build(load_config(config_file_path, 'ftp-config')))
    # ftp_service.upload_file(conf_file_name, open("./" + conf_file_name, 'rb'))


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        main('conf/application.yml', 'latest')
