from usecase.spec.hk_spec import HK_MATCH_DICT
from usecase.spec.jp_spec import JP_MATCH_DICT
from usecase.spec.tw_spec import TW_MATCH_DICT


class GenerateVerifySpecService:

    def generate(self, vpon_geo_domain_list: list):

        vpon_geo_domain_dict = {vpon_geo_domain.criteria_id: vpon_geo_domain
                                for vpon_geo_domain in vpon_geo_domain_list}

        return self.__generate(vpon_geo_domain_dict, TW_MATCH_DICT) + self.__generate(vpon_geo_domain_dict,
                                                                                      HK_MATCH_DICT) + self.__generate(
            vpon_geo_domain_dict, JP_MATCH_DICT)

    def __generate(self, vpon_geo_domain_dict, geo_dict):
        return [[vpon_geo_domain_dict[key],
                 vpon_geo_domain_dict[key]._vpon_geo_name == vpon_geo_domain_dict[key]._google_geo_name] for key, v in
                geo_dict.items()]
