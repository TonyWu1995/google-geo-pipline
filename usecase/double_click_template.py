import json
import logging

from usecase.dto.double_click_dto import DoubleClickDTO

log = logging.getLogger(__name__)


class DoubleClickTemplate:

    def __header(self):
        return 'doubleclick-geo-table {\n'

    def __footer(self):
        return '}'

    def build(self, vpon_geo_list: list) -> str:
        log.debug("build() vpon_geo_list size={}".format(len(vpon_geo_list)))
        config_list = []
        vpon_geo_list = [row for row in vpon_geo_list if row.tier1 != 0]
        vpon_geo_list.sort(key=lambda x: x.criteria_id)

        for vpon_geo_domain in vpon_geo_list:
            dto = DoubleClickDTO(vpon_geo_domain.tier1, vpon_geo_domain.tier2, vpon_geo_domain.tier3)
            output = json.dumps({k: v for k, v in dto.__dict__.items() if v is not None})
            output = str(vpon_geo_domain.criteria_id) + " = " + output + "\n"
            config_list.append(output)
        return self.__header() + ''.join(config_list) + self.__footer()

    def __remove_nulls(self, d):
        return {k: v for k, v in d.__dict__.items() if v is not None}
