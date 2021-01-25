import logging

from usecase.domain.vpon_geo_domain import VponGeoDomain

log = logging.getLogger(__name__)

special_geo_name_dict = {
    'Republic of the Congo': 'Congo',
    'North Macedonia': 'Macedonia (FYROM)',
    'Eswatini': 'Swaziland',
    'Federated States of Micronesia': 'Micronesia',
    'Turks and Caicos Islands': 'Turksand Caicos Islands',  # right no this name but spec have
    'Macao': 'Macau',
    'Hualien Airport': 'Hualien County',
}


class GeneralVponGeoService:
    tag_label = ['Province', 'Township', 'District', 'Prefecture']

    def generate(self, google_geo_dto_list: list, vpon_geo_list: list, country_code: str):
        log.info(
            "generate() google_geo_dto_list size={}, vpon_geo_list size={} country_code={}".format(
                len(google_geo_dto_list), len(vpon_geo_list), country_code))
        google_geo_dto_dict = {google_geo_dto.criteria_id: google_geo_dto for google_geo_dto in google_geo_dto_list if
                               google_geo_dto.country_code == country_code}
        # do format
        vpon_geo_dto_list = [vpon_geo_dto for vpon_geo_dto in vpon_geo_list if
                             vpon_geo_dto.country_code == country_code]
        # do match
        if len(vpon_geo_dto_list) > 0 and len(google_geo_dto_dict) > 0:
            result = self.match(google_geo_dto_dict, vpon_geo_dto_list)
            return result
        if len(google_geo_dto_dict) > 0:
            result = [VponGeoDomain.build(k, 0, 0, 0) for k, v in
                      google_geo_dto_dict.items()]
            return result
        return []

    def match(self, google_geo_dto_dict, vpon_geo_dto_list):
        result = []
        for key, google_geo_dto in google_geo_dto_dict.items():
            # calc_result_list = [
            #     [self.calc_match_count(google_geo_dto.name_list, [vpon_geo[3], vpon_geo[4], vpon_geo[5]]), vpon_geo]
            #     for vpon_geo in vpon_geo_dto_list]
            calc_result_list = [
                [self.calc_match_count(google_geo_dto.name_list,
                                       [vpon_geo.tier1_name, vpon_geo.tier2_name, vpon_geo.tier3_name]), vpon_geo]
                for vpon_geo in vpon_geo_dto_list]
            max_value = max(result[0] for result in calc_result_list)
            calc_result_list = [row[1] for row in calc_result_list if row[0] == max_value]
            match = self.filter_match(calc_result_list, google_geo_dto.name_list)
            print(match)
            # if len(match) > 0:
            #     vpon_domain = VponGeoDomain.build(key, match[7], match[8], match[6])
            #     result.append(vpon_domain)
            # else:
            #     vpon_domain = VponGeoDomain.build(key, 0, 0, 0)
            #     result.append(vpon_domain)
        return result

    def filter_match(self, calc_result_list, google_geo_name_list):
        result = []
        for i in range(0, len(google_geo_name_list)):
            match = [row for row in calc_result_list if
                     row[0] == google_geo_name_list[len(google_geo_name_list) - i - 1] or row[0] ==
                     google_geo_name_list[len(google_geo_name_list) - i - 1].split(' ')[0]]
            if len(match) > 0:
                result.append(match[0])
                break
        for i in range(0, len(google_geo_name_list)):
            match = [row for row in calc_result_list if
                     row[0].split(' ')[0] == google_geo_name_list[len(google_geo_name_list) - i - 1] or
                     row[0].split(' ')[0] ==
                     google_geo_name_list[len(google_geo_name_list) - i - 1].split(' ')[0]]
            if len(match) > 0:
                result.append(match[0])
                break
        return result[0] if len(result) > 0 else []

    # TODO refactor
    def calc_match_count(self, google_geo_name, vpon_tier_list):
        result = []
        for i in range(0, len(vpon_tier_list)):
            match_list = []
            for j in range(i, len(google_geo_name)):
                if google_geo_name[j] == vpon_tier_list[i]:
                    match_list.append(vpon_tier_list)
                    break
            result.append(match_list)

        result = [i for row in result for i in row]
        return result.count(result[0]) if len(result) > 0 else 0

    # # TODO rm
    # def __calc_geo_name(self, name_list):
    #     common = set(name_list).intersection(self.tag_label)
    #     for tag in common:
    #         name_list.remove(tag)
    #     name = ' '.join(name_list)
    #     if name in special_geo_name_dict:
    #         return special_geo_name_dict[name]
    #     return name
    #
