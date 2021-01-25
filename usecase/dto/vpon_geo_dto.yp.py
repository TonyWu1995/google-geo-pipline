from util.string import String
from util.string_util import calc_geo_name


class VponGeoDTO:

    def __init__(self, tier1_name, tier2_name, tier3_name, tier_id1, tier_id2, tier_id3):
        self._tier1_name = tier1_name
        self._tier2_name = tier2_name
        self._tier3_name = tier3_name
        self._tier_id1 = tier_id1
        self._tier_id2 = tier_id2
        self._tier_id3 = tier_id3

    @staticmethod
    def build(vpon_geo_list):
        tier1 = VponGeoDTO.__check_is_equal_two_hyphen(VponGeoDTO.__normalize_vpon_geo(vpon_geo_list[3]))
        tier2 = VponGeoDTO.__check_is_equal_two_hyphen(VponGeoDTO.__normalize_vpon_geo(vpon_geo_list[4]))
        tier3 = VponGeoDTO.__check_is_equal_two_hyphen(VponGeoDTO.__normalize_vpon_geo(vpon_geo_list[5]))
        tier_id1 = VponGeoDTO.__check_is_empty_and_equal_two_hyphen(vpon_geo_list[6])
        tier_id2 = VponGeoDTO.__check_is_empty_and_equal_two_hyphen(vpon_geo_list[7])
        tier_id3 = VponGeoDTO.__check_is_empty_and_equal_two_hyphen(vpon_geo_list[8])
        return VponGeoDTO(tier1, tier2, tier3, tier_id1, tier_id2, tier_id3)

    @staticmethod
    def __check_is_empty_and_equal_two_hyphen(s: str):
        return 0 if String(s).is_equal_two_hyphen() or String(s).is_empty() else int(s)

    @staticmethod
    def __check_is_equal_two_hyphen(s):
        return None if String(s).is_equal_two_hyphen() else s

    @staticmethod
    def __normalize_vpon_geo(s: str):
        return calc_geo_name(s.split(',')[0].split(' '))
