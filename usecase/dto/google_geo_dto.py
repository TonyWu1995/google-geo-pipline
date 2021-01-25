from util.string_util import calc_geo_name


class GoogleGeoDTO:

    def __init__(self, criteria_id, id, name_list, parentId, region_code, country_code, target_type):
        self.criteria_id = criteria_id
        self.id = id
        self.name_list = name_list
        self.parentId = parentId
        self.region_code = region_code
        self.country_code = country_code
        self.target_type = target_type

    @staticmethod
    def build(google_geo_list):
        name_list = [GoogleGeoDTO.__normalize_google_geo(geo_name) for geo_name in google_geo_list[2].split(',')]
        name_list.reverse()
        return GoogleGeoDTO(google_geo_list[0], google_geo_list[1], name_list,
                            google_geo_list[3], google_geo_list[4], google_geo_list[5]
                            , google_geo_list[6])

    @staticmethod
    def build_google_geo_list(google_geo_table: list):
        # list : Criteria ID,Name,Canonical Name,Parent ID,Region Code,Country Code,Target Type
        return [GoogleGeoDTO.build(google_geo_list) for google_geo_list in google_geo_table]

    @staticmethod
    def __normalize_google_geo(name: str):
        return calc_geo_name(name.split(' '))
