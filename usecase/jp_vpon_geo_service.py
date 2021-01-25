import logging

from usecase.general_vpon_geo_service import GeneralVponGeoService

log = logging.getLogger(__name__)


sepcial_dict = {
    ('Japan', 'Shiga', 'Konan'): ['', '', '', '', '', None, 0, 38, 74, 'JP'],
    ('Japan', 'Gifu', 'Ikeda'): ['', '', '', '', '', None, 0, 38, 47, 'JP'],
    ('Japan', 'Yamanashi', 'Chuo'): ['', '', '', '', '', None, 0, 38, 85, 'JP'],
    ('Japan', 'Ibaraki', 'Tokai'): ['', '', '', '', '', None, 0, 38, 52, 'JP'],
    ('Japan', 'Kagoshima', 'Izumi'): ['', '', '', '', '', None, 0, 38, 56, 'JP'],
    ('Japan', 'Nagasaki', 'Tsushima'): ['', '', '', '', '', None, 0, 38, 56, 'JP'],
    ('Japan', 'Hiroshima', 'Miyoshi'): ['', '', '', '', '', None, 0, 38, 49, 'JP'],
    ('Japan', 'Hiroshima', 'Fuchu'): ['', '', '', '', '', None, 0, 38, 49, 'JP'],
    ('Japan', 'Saitama', 'Miyoshi'): ['', '', '', '', '', None, 0, 38, 73, 'JP'],
    ('Japan', 'Gunma', 'Numata'): ['', '', '', '', '', None, 0, 38, 48, 'JP'],
    ('Japan', 'Ibaraki', 'Ibaraki'): ['', '', '', '', '', None, 0, 38, 52, 'JP']
}


class JPVponGeoService(GeneralVponGeoService):
    tag_label = ['Province', 'Township', 'District', 'Prefecture']

    def generate(self, google_geo_dto_list: list, vpon_geo_list: list, country_code="JP"):
        log.info(
            "generate() google_geo_dto_list size={}, vpon_geo_list size={} country_code={}".format(
                len(google_geo_dto_list), len(vpon_geo_list), country_code))
        return super().generate(google_geo_dto_list, vpon_geo_list, country_code)

    def filter_match(self, calc_result_list, name_list):
        if tuple(name_list) in sepcial_dict:
            return sepcial_dict[tuple(name_list)]
        result = [super().filter_match(calc_result_list, name_list)]
        return result[0] if len(result) > 0 else []
