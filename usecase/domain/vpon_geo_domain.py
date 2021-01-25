class VponGeoDomain:
    # TODO google vpon path
    def __init__(self, criteria_id=None, tier1=None, tier2=None, tier3=None, vpon_geo_name="", google_geo_name=""):
        self._criteria_id = criteria_id
        self._tier1 = tier1
        self._tier2 = tier2
        self._tier3 = tier3
        self._vpon_geo_name = vpon_geo_name
        self._google_geo_name = google_geo_name

    @property
    def criteria_id(self):
        return self._criteria_id

    @property
    def tier1(self):
        return self._tier1

    @property
    def tier2(self):
        return self._tier2

    @property
    def tier3(self):
        return self._tier3

    @staticmethod
    def build(criteria_id, tier_1, tier_2, tier_3, vpon_geo_name, google_geo_name):
        # default
        if tier_1 == 0 and tier_2 == 0 and tier_3 == 0:
            return VponGeoDomain(int(criteria_id),
                                 int(tier_1),
                                 vpon_geo_name=vpon_geo_name,
                                 google_geo_name=google_geo_name)
        if tier_1 > 0 and tier_2 > 0 and tier_3 > 0:
            return VponGeoDomain(int(criteria_id),
                                 int(tier_1),
                                 int(tier_2),
                                 int(tier_3),
                                 vpon_geo_name=vpon_geo_name,
                                 google_geo_name=google_geo_name)
        if tier_1 > 0 and tier_2 > 0:
            return VponGeoDomain(int(criteria_id),
                                 int(tier_1),
                                 int(tier_2),
                                 vpon_geo_name=vpon_geo_name,
                                 google_geo_name=google_geo_name
                                 )
        if tier_1 > 0 and tier_3 > 0:
            return VponGeoDomain(int(criteria_id),
                                 int(tier_1),
                                 int(tier_3),
                                 vpon_geo_name=vpon_geo_name,
                                 google_geo_name=google_geo_name
                                 )
        if tier_2 > 0 and tier_3 > 0:
            return VponGeoDomain(int(criteria_id),
                                 int(tier_2),
                                 int(tier_3),
                                 vpon_geo_name=vpon_geo_name,
                                 google_geo_name=google_geo_name
                                 )
        if tier_1 > 0:
            return VponGeoDomain(int(criteria_id),
                                 int(tier_1),
                                 vpon_geo_name=vpon_geo_name,
                                 google_geo_name=google_geo_name
                                 )
        if tier_2 > 0:
            return VponGeoDomain(int(criteria_id),
                                 int(tier_2),
                                 vpon_geo_name=vpon_geo_name,
                                 google_geo_name=google_geo_name
                                 )
        if tier_3 > 0:
            return VponGeoDomain(int(criteria_id),
                                 int(tier_3),
                                 vpon_geo_name=vpon_geo_name,
                                 google_geo_name=google_geo_name)
        return None
