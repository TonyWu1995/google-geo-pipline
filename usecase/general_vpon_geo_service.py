import logging

from usecase.domain.vpon_geo_domain import VponGeoDomain

log = logging.getLogger(__name__)

# TODO rm
special_geo_name_dict = {
    'Republic of the Congo': 'Congo',
    'North Macedonia': 'Macedonia (FYROM)',
    'Eswatini': 'Swaziland',
    'Federated States of Micronesia': 'Micronesia',
    'Turks and Caicos Islands': 'Turksand Caicos Islands',  # right no this name but spec have
    'Macao': 'Macau',
    'Hualien Airport': 'Hualien County',
}

#JP error
# sepcial_dict = {
#     ('Japan', 'Shiga', 'Konan'): ['', '', '', '', '', None, 0, 38, 74, 'JP'],
#     ('Japan', 'Gifu', 'Ikeda'): ['', '', '', '', '', None, 0, 38, 47, 'JP'],
#     ('Japan', 'Yamanashi', 'Chuo'): ['', '', '', '', '', None, 0, 38, 85, 'JP'],
#     ('Japan', 'Ibaraki', 'Tokai'): ['', '', '', '', '', None, 0, 38, 52, 'JP'],
#     ('Japan', 'Kagoshima', 'Izumi'): ['', '', '', '', '', None, 0, 38, 56, 'JP'],
#     ('Japan', 'Nagasaki', 'Tsushima'): ['', '', '', '', '', None, 0, 38, 56, 'JP'],
#     ('Japan', 'Hiroshima', 'Miyoshi'): ['', '', '', '', '', None, 0, 38, 49, 'JP'],
#     ('Japan', 'Hiroshima', 'Fuchu'): ['', '', '', '', '', None, 0, 38, 49, 'JP'],
#     ('Japan', 'Saitama', 'Miyoshi'): ['', '', '', '', '', None, 0, 38, 73, 'JP'],
#     ('Japan', 'Gunma', 'Numata'): ['', '', '', '', '', None, 0, 38, 48, 'JP'],
#     ('Japan', 'Ibaraki', 'Ibaraki'): ['', '', '', '', '', None, 0, 38, 52, 'JP']
# }


class GeneralVponGeoService:

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
            calc_result_list = [
                [self.calc_match_count(google_geo_dto.name_list,
                                       [vpon_geo.tier1_name, vpon_geo.tier2_name, vpon_geo.tier3_name]), vpon_geo]
                for vpon_geo in vpon_geo_dto_list]
            max_value = max(result[0] for result in calc_result_list)
            calc_result_list = [row[1] for row in calc_result_list if row[0] == max_value]
            match_list = self.filter_match(calc_result_list, google_geo_dto.name_list)
            if len(match_list) > 0:
                vpon_geo_dto = match_list[0]
                vpon_domain = VponGeoDomain.build(key, vpon_geo_dto.tier_id1, vpon_geo_dto.tier_id2,
                                                  vpon_geo_dto.tier_id3)
                result.append(vpon_domain)
            else:
                vpon_domain = VponGeoDomain.build(key, 0, 0, 0)
                result.append(vpon_domain)
        return result

    def filter_match(self, calc_result_list, google_geo_name_list):
        result = []
        for i in range(0, len(google_geo_name_list)):
            match = [row for row in calc_result_list if
                     row.name == google_geo_name_list[len(google_geo_name_list) - i - 1] or row.name ==
                     google_geo_name_list[len(google_geo_name_list) - i - 1].split(' ')[0]]
            if len(match) > 0:
                result.append(match[0])
                break
        for i in range(0, len(google_geo_name_list)):
            match = [row for row in calc_result_list if
                     row.name.split(' ')[0] == google_geo_name_list[len(google_geo_name_list) - i - 1] or
                     row.name.split(' ')[0] ==
                     google_geo_name_list[len(google_geo_name_list) - i - 1].split(' ')[0]]
            if len(match) > 0:
                result.append(match[0])
                break
        return [result[0]] if len(result) > 0 else []

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
