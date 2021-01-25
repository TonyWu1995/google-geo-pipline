def calc_geo_name(name_list):
    common = set(name_list).intersection(['Province', 'Township', 'District', 'Prefecture'])
    for tag in common:
        name_list.remove(tag)
    return ' '.join(name_list)
