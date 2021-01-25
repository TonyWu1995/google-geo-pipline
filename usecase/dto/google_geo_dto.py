


class GoogleGeoDTO:

    def __init__(self, criteria_id, id, name, parentId, region_code, country_code, target_type):
        self.criteria_id = criteria_id
        self.id = id
        self.name = name
        self.parentId = parentId
        self.region_code = region_code
        self.country_code = country_code
        self.target_type = target_type

    @staticmethod
    def build_google_geo_list(google_geo_table: list):
        # list : Criteria ID,Name,Canonical Name,Parent ID,Region Code,Country Code,Target Type
        return [GoogleGeoDTO(row[0], row[1], row[2],
                             row[3], row[4], row[5], row[6]) for row in google_geo_table]
