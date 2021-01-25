import logging

from usecase.spec.hk_spec import HK_MATCH_DICT
from usecase.spec.jp_spec import JP_MATCH_DICT
from usecase.spec.tw_spec import TW_MATCH_DICT

log = logging.getLogger(__name__)


class VerifyGeoService:

    def verify(self, vpon_geo_domain_list, prebid_list: list):
        log.info("verify() vpon_geo_domain_list size={} prebid_list size={}".format(len(vpon_geo_domain_list),
                                                                                    len(prebid_list)))
        vpon_geo_domain_dict = {vpon_geo_domain.criteria_id: vpon_geo_domain
                                for vpon_geo_domain in vpon_geo_domain_list}
        hk_correct_count, hk_error_list = self.__verify(vpon_geo_domain_dict,
                                                        HK_MATCH_DICT)
        tw_correct_count, tw_error_list = self.__verify(vpon_geo_domain_dict,
                                                        TW_MATCH_DICT)
        jp_correct_count, jp_error_list = self.__verify(vpon_geo_domain_dict,
                                                        JP_MATCH_DICT)
        correct_count = hk_correct_count + tw_correct_count + jp_correct_count
        error_list = hk_error_list + tw_error_list + jp_error_list
        return correct_count, error_list, self.__verify_prebid(vpon_geo_domain_dict,
                                                               prebid_list)

    def __verify_prebid(self, vpon_geo_domain_dict, prebid_list: list):
        log.info("verify_prebid() vpon_geo_domain_dict size={}, prebid_list size={}".format(len(vpon_geo_domain_dict),
                                                                                            len(prebid_list)))
        match_count = sum([1 for criteria_id in prebid_list if criteria_id[0] in vpon_geo_domain_dict])
        return match_count / len(prebid_list) * 100

    def __verify(self, vpon_geo_domain_dict, geo_dict):
        correct_count = 0
        error_list = []
        for key, v in geo_dict.items():
            if key in vpon_geo_domain_dict:
                vpon_geo_domain = vpon_geo_domain_dict[key]
                if vpon_geo_domain.tier1 == v['tier1'] and vpon_geo_domain.tier2 == v[
                    'tier2'] and vpon_geo_domain.tier3 == v['tier3']:
                    correct_count += 1
                else:
                    error_list.append(vpon_geo_domain)
        log.info("__verify() correct_count={} error_list size={}".format(correct_count,
                                                                         len(error_list)
                                                                         ))
        return correct_count, error_list
