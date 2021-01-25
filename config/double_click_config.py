class DoubleClickConfig:

    def __init__(self, google_geo_path: str, vpon_geo_path: str, hk_google_vpon_geo_path: str, prebid_path: str):
        self._google_geo_path = google_geo_path
        self._vpon_geo_path = vpon_geo_path
        self._hk_google_vpon_geo_path = hk_google_vpon_geo_path
        self._prebid_path = prebid_path

    @property
    def google_geo_path(self):
        return self._google_geo_path

    @property
    def vpon_geo_path(self):
        return self._vpon_geo_path

    @property
    def hk_google_vpon_geo_path(self):
        return self._hk_google_vpon_geo_path

    @property
    def prebid_path(self):
        return self._prebid_path

    @staticmethod
    def build(config: dict):
        return DoubleClickConfig(config['google-geo-path'], config['vpon-geo-path'], config['hk-google-vpon-geo-path'],config['prebid_path'])
