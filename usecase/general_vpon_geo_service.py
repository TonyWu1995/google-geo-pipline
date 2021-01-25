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
        google_geo_dto_dict = self.format_google_geo_dto_dict(google_geo_dto_list, country_code)
        # do format
        vpon_geo_list = self.format_vpon_goe_list(vpon_geo_list, country_code)
        # do match
        if len(vpon_geo_list) > 0 and len(google_geo_dto_dict) > 0:
            result = self.match(google_geo_dto_dict, vpon_geo_list)
            return result
        if len(google_geo_dto_dict) > 0:
            result = [VponGeoDomain.build(k, 0, 0, 0) for k, v in
                      google_geo_dto_dict.items()]
            return result
        return []

    def match(self, google_geo_dto_dict, vpon_geo_list):
        result = []
        for key, value in google_geo_dto_dict.items():
            name_list = value.name
            calc_result_list = [[self.calc_match_count(name_list, [vpon_geo[3], vpon_geo[4], vpon_geo[5]]), vpon_geo]
                                for vpon_geo in vpon_geo_list]
            calc_result_list = [row[1] for row in calc_result_list if row[0] == max(calc_result_list)[0]]
            match = self.filter_match(calc_result_list, name_list)
            if len(match) > 0:
                vpon_domain = VponGeoDomain.build(key, match[7], match[8], match[6])
                result.append(vpon_domain)
            else:
                vpon_domain = VponGeoDomain.build(key, 0, 0, 0)
                result.append(vpon_domain)
        return result

    def filter_match(self, calc_result_list, name_list):
        result = []
        for i in range(0, len(name_list)):
            match = [row for row in calc_result_list if
                     row[0] == name_list[len(name_list) - i - 1] or row[0] ==
                     name_list[len(name_list) - i - 1].split(' ')[0]]
            if len(match) > 0:
                result.append(match[0])
                break
        for i in range(0, len(name_list)):
            match = [row for row in calc_result_list if
                     row[0].split(' ')[0] == name_list[len(name_list) - i - 1] or row[0].split(' ')[0] ==
                     name_list[len(name_list) - i - 1].split(' ')[0]]
            if len(match) > 0:
                result.append(match[0])
                break
        return result[0] if len(result) > 0 else []

    # TODO refactor
    def calc_match_count(self, geo_name, tier_list):
        result = []
        for i in range(0, len(tier_list)):
            match_list = []
            for j in range(i, len(geo_name)):
                if geo_name[j] == tier_list[i]:
                    match_list.append(tier_list)
                    break
            result.append(match_list)
        result = [i for row in result for i in row]
        return result.count(result[0]) if len(result) > 0 else 0

    def format_google_geo_dto_dict(self, google_geo_dto_list, country_code: str):
        google_geo_dto_dict = {google_geo_dto.criteria_id: google_geo_dto for google_geo_dto in google_geo_dto_list if
                               google_geo_dto.country_code == country_code}
        for key, google_geo_dto in google_geo_dto_dict.items():
            google_geo_dto_name_list = [self.__normalize_google_geo(geo_name) for geo_name in
                                        google_geo_dto.name.split(',')]
            google_geo_dto_name_list.reverse()
            google_geo_dto.name = google_geo_dto_name_list
        return google_geo_dto_dict

    def __normalize_google_geo(self, name: str):
        return self.__calc_geo_name(name.split(' '))

    def __calc_geo_name(self, name_list):
        common = set(name_list).intersection(self.tag_label)
        for tag in common:
            name_list.remove(tag)
        name = ' '.join(name_list)
        if name in special_geo_name_dict:
            return special_geo_name_dict[name]
        return name

    def __normalize_vpon_geo(self, s: str):
        return self.__calc_geo_name(s.split(',')[0].split(' '))

    #TODO rm
    def format_vpon_goe_list(self, vpon_geo_list: list, country_code: str):
        vpon_geo_list = [row for row in vpon_geo_list if row[9] == country_code]
        for row in vpon_geo_list:
            # tier1 tier2 tier3
            row[3] = None if self.__normalize_vpon_geo(row[3]) == '--' else self.__normalize_vpon_geo(row[3])
            row[4] = None if self.__normalize_vpon_geo(row[4]) == '--' else self.__normalize_vpon_geo(row[4])
            row[5] = None if self.__normalize_vpon_geo(row[5]) == '--' else self.__normalize_vpon_geo(row[5])
            row[6] = 0 if row[6] == '--' or row[6] == '' else int(row[6])
            row[7] = 0 if row[7] == '--' or row[6] == '' else int(row[7])
            row[8] = 0 if row[8] == '--' or row[6] == '' else int(row[8])
        return vpon_geo_list
