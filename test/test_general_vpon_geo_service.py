from unittest import TestCase

from usecase.dto.google_geo_dto import GoogleGeoDTO
from usecase.general_vpon_geo_service import GeneralVponGeoService


class TestGeneralVponGeoService(TestCase):
    ae_vpon_geo_list = [['Abu Dhabi', 'Abu Dhabi', 'Province', 'Abu Dhabi', '', '', 0, 0, 0, 'AE'],
                        ['Ajman', 'Ajman', 'Province', 'Ajman', '', '', 0, 0, 0, 'AE'],
                        ['Dubai', 'Dubai', 'Province', 'Dubai', '', '', 0, 0, 0, 'AE'],
                        ['Fujairah', 'Fujairah', 'City', 'Fujairah', '', '', 0, 0, 0, 'AE'],
                        ['Fujairah', 'Fujairah', 'Province', 'Fujairah', '', '', 0, 0, 0, 'AE'],
                        ['Ras al Khaimah', 'Ras al Khaimah', 'Province', 'Ras al Khaimah', '', '', 0, 0, 0, 'AE'],
                        ['Sharjah', 'Sharjah', 'Province', 'Sharjah', '', '', 0, 0, 0, 'AE'],
                        ['Umm Al Quwain', 'Umm Al Quwain', 'Province', 'Umm Al Quwain', '', '', 0, 0, 0, 'AE'],
                        ['United Arab Emirates', 'United Arab Emirates', 'Country', 'United Arab Emirates', '', '', 0,
                         0, 0, 'AE']]

    def test_match_case1(self):
        service = GeneralVponGeoService()
        google_geo_dict = {
            1000010: GoogleGeoDTO(1000010, 'Abu Dhabi', ['United Arab Emirates', 'Abu Dhabi', 'Abu Dhabi'],
                                  '90,759,672,158', '',
                                  "AE", 'City')
        }
        result = service.match(google_geo_dict, self.ae_vpon_geo_list)
        self.assertEqual(result[0].criteria_id, 1000010)
        self.assertEqual(result[0].tier1, 0)
        self.assertEqual(result[0].tier2, None)
        self.assertEqual(result[0].tier3, None)

    def test_match_case2(self):
        service = GeneralVponGeoService()
        mo_vpon_geo_list = [['Macau', 'Macau', 'Region', 'Macau', None, None, 516, 0, 0, 'MO']]
        google_geo_dict = {
            2446: GoogleGeoDTO(2446, 'Abu Dhabi', ['Macau'],
                               '90,759,672,158', '',
                               "MO", 'City')
        }
        result = service.match(google_geo_dict, mo_vpon_geo_list)
        self.assertEqual(result[0].criteria_id, 2446)
        self.assertEqual(result[0].tier1, 516)
        self.assertEqual(result[0].tier2, None)
        self.assertEqual(result[0].tier3, None)

    def test_match_case3(self):
        service = GeneralVponGeoService()
        mo_vpon_geo_list = [['Abruzzo', 'Abruzzo', 'Region', 'Abruzzo', '', '', 0, 0, 0, 'IT'],
                            ['Aosta', 'Aosta', 'Region', 'Aosta', '', '', 0, 0, 0, 'IT'],
                            ['Apulia', 'Apulia', 'Region', 'Apulia', '', '', 0, 0, 0, 'IT'],
                            ['Basilicata', 'Basilicata', 'Region', 'Basilicata', '', '', 0, 0, 0, 'IT'],
                            ['Calabria', 'Calabria', 'Region', 'Calabria', '', '', 0, 0, 0, 'IT'],
                            ['Campania', 'Campania', 'Region', 'Campania', '', '', 0, 0, 0, 'IT'],
                            ['Emilia-Romagna', 'Emilia-Romagna', 'Region', 'Emilia-Romagna', '', '', 0, 0, 0, 'IT'],
                            ['Friuli-Venezia Giulia', 'Friuli-Venezia Giulia', 'Region', 'Friuli-Venezia Giulia', '',
                             '', 0, 0, 0, 'IT'],
                            ['Italy', 'Italy', 'Country', 'Italy', '', '', 0, 0, 0, 'IT'],
                            ['Lazio', 'Lazio', 'Region', 'Lazio', '', '', 0, 0, 0, 'IT'],
                            ['Liguria', 'Liguria', 'Region', 'Liguria', '', '', 0, 0, 0, 'IT'],
                            ['Lombardy', 'Lombardy', 'Region', 'Lombardy', '', '', 0, 0, 0, 'IT'],
                            ['Marche', 'Marche', 'Region', 'Marche', '', '', 0, 0, 0, 'IT'],
                            ['Molise', 'Molise', 'Region', 'Molise', '', '', 0, 0, 0, 'IT'],
                            ['Piedmont', 'Piedmont', 'Region', 'Piedmont', '', '', 0, 0, 0, 'IT'],
                            ['Sardinia', 'Sardinia', 'Region', 'Sardinia', '', '', 0, 0, 0, 'IT'],
                            ['Sicily', 'Sicily', 'Region', 'Sicily', '', '', 0, 0, 0, 'IT'],
                            ['Trentino-Alto Adige / South Tyrol', 'Trentino-Alto Adige / South Tyrol', 'Region',
                             'Trentino-Alto Adige / South Tyrol', '', '', 0, 0, 0, 'IT'],
                            ['Tuscany', 'Tuscany', 'Region', 'Tuscany', '', '', 0, 0, 0, 'IT'],
                            ['Umbria', 'Umbria', 'Region', 'Umbria', '', '', 0, 0, 0, 'IT'],
                            ['Veneto', 'Veneto', 'Region', 'Veneto', '', '', 0, 0, 0, 'IT']]
        google_geo_dict = {
            20593: GoogleGeoDTO(20593, 'Province of Reggio Emilia', ['Reggio Emilia'],
                                '90,759,672,158', '',
                                "IT", 'City')
        }
        result = service.match(google_geo_dict, mo_vpon_geo_list)
        self.assertEqual(result[0].criteria_id, 20593)
        self.assertEqual(result[0].tier1, 0)
