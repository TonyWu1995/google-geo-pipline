import logging

from usecase.domain.vpon_geo_domain import VponGeoDomain

log = logging.getLogger(__name__)


class HKVponGeoService:

    def generate(self, hk_geo_list: list):
        log.info("generate() hk_geo_list size={}".format(
            len(hk_geo_list)))
        hk_geo_list = self.filter(hk_geo_list)
        hk_mapping_dict = self.to_hk_mapping_table(hk_geo_list)
        result = []
        for hk_geo in hk_geo_list:
            vpon_id_list, vpon_geo_name = self.calc_vpon_geo(hk_mapping_dict, hk_geo)
            google_geo_name = hk_geo[2].split(",")
            google_geo_name.reverse()
            result.append(
                VponGeoDomain.build(hk_geo[0], vpon_id_list[0], vpon_id_list[1], vpon_id_list[2], vpon_geo_name,
                                    google_geo_name
                                    ))
        log.debug("generate() result size={} hk_mapping_dict size={}".format(len(result), len(hk_mapping_dict)))
        return result

    def calc_vpon_geo(self, hk_mapping_dict, hk_geo):
        log.debug("calc_vpon_geo() hk_geo={}".format(hk_geo))
        geo_name_list = hk_geo[2].split(',')
        geo_name_list.reverse()
        vpon_id_list = [hk_mapping_dict[geo_name] for geo_name in geo_name_list]
        if len(vpon_id_list) < 3:
            for i in range(0, 3 - len(vpon_id_list)):
                vpon_id_list.append(0)
        return [vpon_id_list, geo_name_list]

    def filter(self, hk_geo_list):
        result = filter(lambda row: row[0] != '', hk_geo_list)
        result = filter(lambda row: row[0] != 'criteria id', result)
        return list(result)

    def to_hk_mapping_table(self, hk_geo_list) -> dict:
        return {row[1]: row[len(row) - 1] for row in hk_geo_list}
