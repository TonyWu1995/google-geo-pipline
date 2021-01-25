class String(str):

    def normalize_geo(self):
        pass

    def is_equal_two_hyphen(self):
        return self == '--'

    def is_empty(self):
        return len(self) == 0
    # TODO
    # def __calc_geo_name(self, name_list):
    #     common = set(name_list).intersection(self.tag_label)
    #     for tag in common:
    #         name_list.remove(tag)
    #     name = ' '.join(name_list)
    #     if name in special_geo_name_dict:
    #         return special_geo_name_dict[name]
    #     return name
