from unittest import TestCase

from config.double_click_config import DoubleClickConfig


class TestDoubleClickConfig(TestCase):

    def test_build(self):
        config = {}
        config['google-geo-path'] = 'test'
        config['vpon-geo-path'] = 'test1'

        build_result = DoubleClickConfig.build(config)

        self.assertEqual(build_result.vpon_geo_path, 'test1')
        self.assertEqual(build_result.google_geo_path, 'test')
