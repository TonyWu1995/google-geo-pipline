from unittest import TestCase

from usecase.hk_vpon_geo_service import HKVponGeoService

hk_geo_list = [
    [2344, 'Hong Kong', 'Hong Kong', '', '', 'HK', 'Region', 35],
    [9061585, 'Mui Wo', 'Mui Wo,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood', 205],
    [9061586, 'Cheung Chau', 'Cheung Chau,New Territories,Hong Kong', '9069535,2344', '', 'HK',
     'Neighborhood', 205],
    [9061587, 'Tung Chung', 'Tung Chung,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood',
     205],
    [9061588, 'Lung Kwu Tan', 'Lung Kwu Tan,New Territories,Hong Kong', '9069535,2344', '', 'HK',
     'Neighborhood', 212],
    [9061589, 'Tin Shui Wai', 'Tin Shui Wai,New Territories,Hong Kong', '9069535,2344', '', 'HK',
     'Neighborhood', 213],
    [9061590, 'Yuen Long', 'Yuen Long,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood',
     213],
    [9061591, 'Sheung Shui', 'Sheung Shui,New Territories,Hong Kong', '9069535,2344', '', 'HK',
     'Neighborhood', 207],
    [9061592, 'Fanling', 'Fanling,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood', 207],
    [9061593, 'Kwu Tung', 'Kwu Tung,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood',
     207],
    [9061594, 'San Tin', 'San Tin,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood', 213],
    [9061595, 'Kam Tin', 'Kam Tin,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood', 213],
    [9061596, 'Kwai Chung', 'Kwai Chung,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood',
     206],
    [9061597, 'Lai Chi Kok', 'Lai Chi Kok,Kowloon,Hong Kong', '9069536,2344', '', 'HK', 'Neighborhood', 216],
    [9061598, 'Tsing Yi', 'Tsing Yi,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood',
     206],
    [9061599, 'Tsuen Wan', 'Tsuen Wan,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood',
     211],
    [9061600, 'Ting Kau', 'Ting Kau,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood',
     211],
    [9061603, 'Tuen Mun', 'Tuen Mun,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood',
     212],
    [9061614, 'Yau Ma Tei', 'Yau Ma Tei,Kowloon,Hong Kong', '9069536,2344', '', 'HK', 'Neighborhood', 218],
    [9061624, 'Tai Tam', 'Tai Tam,Hong Kong Island,Hong Kong', '9069537,2344', '', 'HK', 'Neighborhood',
     221],
    [9061625, 'Repulse Bay', 'Repulse Bay,Hong Kong Island,Hong Kong', '9069537,2344', '', 'HK',
     'Neighborhood', 210],
    [9061626, 'Shek O', 'Shek O,Hong Kong Island,Hong Kong', '9069537,2344', '', 'HK', 'Neighborhood', 221],
    [9061628, 'Sai Kung', 'Sai Kung,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood',
     208],
    [9061629, 'Ma On Shan', 'Ma On Shan,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood',
     209],
    [9061630, 'Sha Tin', 'Sha Tin,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood', 209],
    [9061635, 'Fo Tan', 'Fo Tan,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood', 209],
    [9061636, 'Tai Po', 'Tai Po,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood', 210],
    [9061637, 'Sha Tau Kok', 'Sha Tau Kok,New Territories,Hong Kong', '9069535,2344', '', 'HK',
     'Neighborhood', 207],
    [9061640, 'Wong Chuk Hang', 'Wong Chuk Hang,Hong Kong Island,Hong Kong', '9069537,2344', '', 'HK',
     'Neighborhood', 221],
    [9069535, 'New Territories', 'New Territories,Hong Kong', '2344', '', 'HK', 'Region', 1268],
    [9069536, 'Kowloon', 'Kowloon,Hong Kong', '2344', '', 'HK', 'Region', 1269],
    [9069537, 'Hong Kong Island', 'Hong Kong Island,Hong Kong', '2344', '', 'HK', 'Territory', 1270]]


class TestHKVponGeoService(TestCase):

    def test_to_hk_mapping_table(self):
        service = HKVponGeoService()

        input_hk_list = [
            [9069537, 'Hong Kong Island', 'Hong Kong Island,Hong Kong', '2344', '', 'HK', 'Territory', 1270]
        ]

        result_dict = service.to_hk_mapping_table(input_hk_list)

        self.assertEqual(result_dict, {
            'Hong Kong Island': 1270
        })

    def test_match(self):
        service = HKVponGeoService()
        hk_geo = [9069535, 'New Territories', 'New Territories,Hong Kong', '2344', '', 'HK', 'Region', 1268]
        hk_dict = service.to_hk_mapping_table(hk_geo_list)

        result = service.calc_vpon_id(hk_dict, hk_geo)
        self.assertEqual(result[0], 35)
        self.assertEqual(result[1], 1268)
        self.assertEqual(result[2], 0)

    def test_match_case1(self):
        service = HKVponGeoService()
        hk_geo = [9061635, 'Fo Tan', 'Fo Tan,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood', 209]
        hk_dict = service.to_hk_mapping_table(hk_geo_list)
        result = service.calc_vpon_id(hk_dict, hk_geo)
        self.assertEqual(result[0], 35)
        self.assertEqual(result[1], 1268)
        self.assertEqual(result[2], 209)

    def test_match_case2(self):
        service = HKVponGeoService()
        hk_geo = [9061635, 'Fo Tan', 'Fo Tan,New Territories,Hong Kong', '9069535,2344', '', 'HK', 'Neighborhood', 209]
        hk_dict = service.to_hk_mapping_table(hk_geo_list)
        result = service.calc_vpon_id(hk_dict, hk_geo)
        self.assertEqual(result[0], 35)
        self.assertEqual(result[1], 1268)
        self.assertEqual(result[2], 209)
