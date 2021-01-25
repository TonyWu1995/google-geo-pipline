from unittest import TestCase

from usecase.dto.google_geo_dto import GoogleGeoDTO
from usecase.general_vpon_geo_service import GeneralVponGeoService

vpon_geo_list = [['Taiwan', 'Taiwan', 'Country', 'Taiwan', None, None, 93, 0, 0, 'TW'],
                 ['Changhua County', 'Changhua County', 'County', 'Taiwan', 'Changhua County', None, 94, 93,
                  0, 'TW'],
                 ['Chiayi City', 'Chiayi City', 'City', 'Taiwan', 'Chiayi City', None, 95, 93, 0, 'TW'],
                 ['Chiayi County', 'Chiayi County', 'County', 'Taiwan', 'Chiayi County', None, 96, 93, 0,
                  'TW'],
                 ['Hsinchu City', 'Hsinchu City', 'City', 'Taiwan', 'Hsinchu City', None, 97, 93, 0, 'TW'],
                 ['Hsinchu County', 'Hsinchu County', 'County', 'Taiwan', 'Hsinchu County', None, 98, 93, 0,
                  'TW'],
                 ['Hualien County', 'Hualien County', 'County', 'Taiwan', 'Hualien County', None, 99, 93, 0,
                  'TW'],
                 ['Kaohsiung City', 'Kaohsiung City', 'City', 'Taiwan', 'Kaohsiung City', None, 100, 93, 0,
                  'TW'],
                 ['Keelung City', 'Keelung City', 'City', 'Taiwan', 'Keelung City', None, 101, 93, 0, 'TW'],
                 ['Kinmen County', 'Kinmen County', 'County', 'Taiwan', 'Kinmen County', None, 102, 93, 0,
                  'TW'],
                 ['Miaoli County', 'Miaoli County', 'County', 'Taiwan', 'Miaoli County', None, 103, 93, 0,
                  'TW'],
                 ['Nantou County', 'Nantou County', 'County', 'Taiwan', 'Nantou County', None, 104, 93, 0,
                  'TW'],
                 ['New Taipei City', 'New Taipei City', 'City', 'Taiwan', 'New Taipei City', None, 105, 93,
                  0, 'TW'],
                 ['Penghu County', 'Penghu County', 'County', 'Taiwan', 'Penghu County', None, 106, 93, 0,
                  'TW'],
                 ['Pingtung County', 'Pingtung County', 'County', 'Taiwan', 'Pingtung County', None, 107, 93,
                  0, 'TW'],
                 ['Taichung City', 'Taichung City', 'City', 'Taiwan', 'Taichung City', None, 108, 93, 0,
                  'TW'],
                 ['Tainan City', 'Tainan City', 'City', 'Taiwan', 'Tainan City', None, 109, 93, 0, 'TW'],
                 ['Taipei City', 'Taipei City', 'City', 'Taiwan', 'Taipei City', None, 110, 93, 0, 'TW'],
                 ['Taitung County', 'Taitung County', 'County', 'Taiwan', 'Taitung County', None, 111, 93, 0,
                  'TW'],
                 ['Taoyuan City', 'Taoyuan City', 'City', 'Taiwan', 'Taoyuan City', None, 112, 93, 0,
                  'TW'],
                 ['Yilan County', 'Yilan County', 'County', 'Taiwan', 'Yilan County', None, 113, 93, 0,
                  'TW'],
                 ['Yunlin County', 'Yunlin County', 'County', 'Taiwan', 'Yunlin County', None, 114, 93, 0,
                  'TW'],
                 ['Beidou', 'Beidou', 'Township', 'Taiwan', 'Changhua County', 'Beidou', 904, 93, 94, 'TW'],
                 ['Changhua', 'Changhua', 'City', 'Taiwan', 'Changhua County', 'Changhua', 905, 93, 94, 'TW'],
                 ['Dacheng', 'Dacheng', 'Township', 'Taiwan', 'Changhua County', 'Dacheng', 906, 93, 94, 'TW'],
                 ['Dacun', 'Dacun', 'Township', 'Taiwan', 'Changhua County', 'Dacun', 907, 93, 94, 'TW'],
                 ['Erlin', 'Erlin', 'Township', 'Taiwan', 'Changhua County', 'Erlin', 908, 93, 94, 'TW'],
                 ['Ershui', 'Ershui', 'Township', 'Taiwan', 'Changhua County', 'Ershui', 909, 93, 94, 'TW'],
                 ['Fangyuan', 'Fangyuan', 'Township', 'Taiwan', 'Changhua County', 'Fangyuan', 910, 93, 94,
                  'TW'],
                 ['Fenyuan', 'Fenyuan', 'Township', 'Taiwan', 'Changhua County', 'Fenyuan', 911, 93, 94, 'TW'],
                 ['Fuxing', 'Fuxing', 'Township', 'Taiwan', 'Changhua County', 'Fuxing', 912, 93, 94, 'TW'],
                 ['Hemei', 'Hemei', 'Township', 'Taiwan', 'Changhua County', 'Hemei', 913, 93, 94, 'TW'],
                 ['Huatan', 'Huatan', 'Township', 'Taiwan', 'Changhua County', 'Huatan', 914, 93, 94, 'TW'],
                 ['Lukang', 'Lukang', 'Township', 'Taiwan', 'Changhua County', 'Lukang', 915, 93, 94, 'TW'],
                 ['Pitou', 'Pitou', 'Township', 'Taiwan', 'Changhua County', 'Pitou', 916, 93, 94, 'TW'],
                 ['Puxin', 'Puxin', 'Township', 'Taiwan', 'Changhua County', 'Puxin', 917, 93, 94, 'TW'],
                 ['Puyan', 'Puyan', 'Township', 'Taiwan', 'Changhua County', 'Puyan', 918, 93, 94, 'TW'],
                 ['Shengang', 'Shengang', 'Township', 'Taiwan', 'Changhua County', 'Shengang', 919, 93, 94,
                  'TW'],
                 ['Shetou', 'Shetou', 'Township', 'Taiwan', 'Changhua County', 'Shetou', 920, 93, 94, 'TW'],
                 ['Tianwei', 'Tianwei', 'Township', 'Taiwan', 'Changhua County', 'Tianwei', 921, 93, 94, 'TW'],
                 ['Tianzhong', 'Tianzhong', 'Township', 'Taiwan', 'Changhua County', 'Tianzhong', 922, 93, 94,
                  'TW'],
                 ['Xianxi', 'Xianxi', 'Township', 'Taiwan', 'Changhua County', 'Xianxi', 923, 93, 94, 'TW'],
                 ['Xihu', 'Xihu', 'Township', 'Taiwan', 'Changhua County', 'Xihu', 924, 93, 94, 'TW'],
                 ['Xiushui', 'Xiushui', 'Township', 'Taiwan', 'Changhua County', 'Xiushui', 925, 93, 94, 'TW'],
                 ['Xizhou', 'Xizhou', 'Township', 'Taiwan', 'Changhua County', 'Xizhou', 926, 93, 94, 'TW'],
                 ['Yongjing', 'Yongjing', 'Township', 'Taiwan', 'Changhua County', 'Yongjing', 927, 93, 94,
                  'TW'],
                 ['Yuanlin', 'Yuanlin', 'Township', 'Taiwan', 'Changhua County', 'Yuanlin', 928, 93, 94, 'TW'],
                 ['Zhutang', 'Zhutang', 'Township', 'Taiwan', 'Changhua County', 'Zhutang', 929, 93, 94, 'TW'],
                 ['East', 'East', 'District', 'Taiwan', 'Chiayi City', 'East', 930, 93, 95, 'TW'],
                 ['West', 'West', 'District', 'Taiwan', 'Chiayi City', 'West', 931, 93, 95, 'TW'],
                 ['Alishan', 'Alishan', 'Township', 'Taiwan', 'Chiayi County', 'Alishan', 932, 93, 96, 'TW'],
                 ['Budai', 'Budai', 'Township', 'Taiwan', 'Chiayi County', 'Budai', 933, 93, 96, 'TW'],
                 ['Dalin', 'Dalin', 'Township', 'Taiwan', 'Chiayi County', 'Dalin', 934, 93, 96, 'TW'],
                 ['Dapu', 'Dapu', 'Township', 'Taiwan', 'Chiayi County', 'Dapu', 935, 93, 96, 'TW'],
                 ['Dongshi', 'Dongshi', 'Township', 'Taiwan', 'Chiayi County', 'Dongshi', 936, 93, 96, 'TW'],
                 ['Fanlu', 'Fanlu', 'Township', 'Taiwan', 'Chiayi County', 'Fanlu', 937, 93, 96, 'TW'],
                 ['Liujiao', 'Liujiao', 'Township', 'Taiwan', 'Chiayi County', 'Liujiao', 938, 93, 96, 'TW'],
                 ['Lucao', 'Lucao', 'Township', 'Taiwan', 'Chiayi County', 'Lucao', 939, 93, 96, 'TW'],
                 ['Meishan', 'Meishan', 'Township', 'Taiwan', 'Chiayi County', 'Meishan', 940, 93, 96, 'TW'],
                 ['Minxiong', 'Minxiong', 'Township', 'Taiwan', 'Chiayi County', 'Minxiong', 941, 93, 96, 'TW'],
                 ['Puzi', 'Puzi', 'City', 'Taiwan', 'Chiayi County', 'Puzi', 942, 93, 96, 'TW'],
                 ['Shuishang', 'Shuishang', 'Township', 'Taiwan', 'Chiayi County', 'Shuishang', 943, 93, 96,
                  'TW'],
                 ['Taibao', 'Taibao', 'City', 'Taiwan', 'Chiayi County', 'Taibao', 944, 93, 96, 'TW'],
                 ['Xikou', 'Xikou', 'Township', 'Taiwan', 'Chiayi County', 'Xikou', 945, 93, 96, 'TW'],
                 ['Xingang', 'Xingang', 'Township', 'Taiwan', 'Chiayi County', 'Xingang', 946, 93, 96, 'TW'],
                 ['Yizhu', 'Yizhu', 'Township', 'Taiwan', 'Chiayi County', 'Yizhu', 947, 93, 96, 'TW'],
                 ['Zhongpu', 'Zhongpu', 'Township', 'Taiwan', 'Chiayi County', 'Zhongpu', 948, 93, 96, 'TW'],
                 ['Zhuqi', 'Zhuqi', 'Township', 'Taiwan', 'Chiayi County', 'Zhuqi', 949, 93, 96, 'TW'],
                 ['East', 'East', 'District', 'Taiwan', 'Hsinchu City', 'East', 950, 93, 97, 'TW'],
                 ['North', 'North', 'District', 'Taiwan', 'Hsinchu City', 'North', 951, 93, 97, 'TW'],
                 ['Xiangshan', 'Xiangshan', 'District', 'Taiwan', 'Hsinchu City', 'Xiangshan', 952, 93, 97,
                  'TW'],
                 ['Baoshan', 'Baoshan', 'Township', 'Taiwan', 'Hsinchu County', 'Baoshan', 953, 93, 98, 'TW'],
                 ['Beipu', 'Beipu', 'Township', 'Taiwan', 'Hsinchu County', 'Beipu', 954, 93, 98, 'TW'],
                 ['Emei', 'Emei', 'Township', 'Taiwan', 'Hsinchu County', 'Emei', 955, 93, 98, 'TW'],
                 ['Guanxi', 'Guanxi', 'Township', 'Taiwan', 'Hsinchu County', 'Guanxi', 956, 93, 98, 'TW'],
                 ['Hengshan', 'Hengshan', 'Township', 'Taiwan', 'Hsinchu County', 'Hengshan', 957, 93, 98,
                  'TW'],
                 ['Hukou', 'Hukou', 'Township', 'Taiwan', 'Hsinchu County', 'Hukou', 958, 93, 98, 'TW'],
                 ['Jianshi', 'Jianshi', 'Township', 'Taiwan', 'Hsinchu County', 'Jianshi', 959, 93, 98, 'TW'],
                 ['Qionglin', 'Qionglin', 'Township', 'Taiwan', 'Hsinchu County', 'Qionglin', 960, 93, 98,
                  'TW'],
                 ['Wufeng', 'Wufeng', 'Township', 'Taiwan', 'Hsinchu County', 'Wufeng', 961, 93, 98, 'TW'],
                 ['Xinfeng', 'Xinfeng', 'Township', 'Taiwan', 'Hsinchu County', 'Xinfeng', 962, 93, 98, 'TW'],
                 ['Xinpu', 'Xinpu', 'Township', 'Taiwan', 'Hsinchu County', 'Xinpu', 963, 93, 98, 'TW'],
                 ['Zhubei', 'Zhubei', 'City', 'Taiwan', 'Hsinchu County', 'Zhubei', 964, 93, 98, 'TW'],
                 ['Zhudong', 'Zhudong', 'Township', 'Taiwan', 'Hsinchu County', 'Zhudong', 965, 93, 98, 'TW'],
                 ['Fengbin', 'Fengbin', 'Township', 'Taiwan', 'Hualien County', 'Fengbin', 966, 93, 99, 'TW'],
                 ['Fenglin', 'Fenglin', 'Township', 'Taiwan', 'Hualien County', 'Fenglin', 967, 93, 99, 'TW'],
                 ['Fuli', 'Fuli', 'Township', 'Taiwan', 'Hualien County', 'Fuli', 968, 93, 99, 'TW'],
                 ['Guangfu', 'Guangfu', 'Township', 'Taiwan', 'Hualien County', 'Guangfu', 969, 93, 99, 'TW'],
                 ['Hualien', 'Hualien', 'City', 'Taiwan', 'Hualien County', 'Hualien', 970, 93, 99, 'TW'],
                 ["Ji'an", "Ji'an", 'Township', 'Taiwan', 'Hualien County', "Ji'an", 971, 93, 99, 'TW'],
                 ['Ruisui', 'Ruisui', 'Township', 'Taiwan', 'Hualien County', 'Ruisui', 972, 93, 99, 'TW'],
                 ['Shoufeng', 'Shoufeng', 'Township', 'Taiwan', 'Hualien County', 'Shoufeng', 973, 93, 99,
                  'TW'],
                 ['Wanrong', 'Wanrong', 'Township', 'Taiwan', 'Hualien County', 'Wanrong', 974, 93, 99, 'TW'],
                 ['Xincheng', 'Xincheng', 'Township', 'Taiwan', 'Hualien County', 'Xincheng', 975, 93, 99,
                  'TW'],
                 ['Xiulin', 'Xiulin', 'Township', 'Taiwan', 'Hualien County', 'Xiulin', 976, 93, 99, 'TW'],
                 ['Yuli', 'Yuli', 'Township', 'Taiwan', 'Hualien County', 'Yuli', 977, 93, 99, 'TW'],
                 ['Zhuoxi', 'Zhuoxi', 'Township', 'Taiwan', 'Hualien County', 'Zhuoxi', 978, 93, 99, 'TW'],
                 ['Alian', 'Alian', 'District', 'Taiwan', 'Kaohsiung City', 'Alian', 979, 93, 100, 'TW'],
                 ['Daliao', 'Daliao', 'District', 'Taiwan', 'Kaohsiung City', 'Daliao', 980, 93, 100, 'TW'],
                 ['Dashe', 'Dashe', 'District', 'Taiwan', 'Kaohsiung City', 'Dashe', 981, 93, 100, 'TW'],
                 ['Dashu', 'Dashu', 'District', 'Taiwan', 'Kaohsiung City', 'Dashu', 982, 93, 100, 'TW'],
                 ['Fengshan', 'Fengshan', 'District', 'Taiwan', 'Kaohsiung City', 'Fengshan', 983, 93, 100,
                  'TW'],
                 ['Gangshan', 'Gangshan', 'District', 'Taiwan', 'Kaohsiung City', 'Gangshan', 984, 93, 100,
                  'TW'],
                 ['Gushan', 'Gushan', 'District', 'Taiwan', 'Kaohsiung City', 'Gushan', 985, 93, 100, 'TW'],
                 ['Hunei', 'Hunei', 'District', 'Taiwan', 'Kaohsiung City', 'Hunei', 986, 93, 100, 'TW'],
                 ['Jiaxian', 'Jiaxian', 'District', 'Taiwan', 'Kaohsiung City', 'Jiaxian', 987, 93, 100, 'TW'],
                 ['Lingya', 'Lingya', 'District', 'Taiwan', 'Kaohsiung City', 'Lingya', 988, 93, 100, 'TW'],
                 ['Linyuan', 'Linyuan', 'District', 'Taiwan', 'Kaohsiung City', 'Linyuan', 989, 93, 100, 'TW'],
                 ['Liugui', 'Liugui', 'District', 'Taiwan', 'Kaohsiung City', 'Liugui', 990, 93, 100, 'TW'],
                 ['Luzhu', 'Luzhu', 'District', 'Taiwan', 'Kaohsiung City', 'Luzhu', 991, 93, 100, 'TW'],
                 ['Maolin', 'Maolin', 'District', 'Taiwan', 'Kaohsiung City', 'Maolin', 992, 93, 100, 'TW'],
                 ['Meinong', 'Meinong', 'District', 'Taiwan', 'Kaohsiung City', 'Meinong', 993, 93, 100, 'TW'],
                 ['Mituo', 'Mituo', 'District', 'Taiwan', 'Kaohsiung City', 'Mituo', 994, 93, 100, 'TW'],
                 ['Namaxia', 'Namaxia', 'District', 'Taiwan', 'Kaohsiung City', 'Namaxia', 995, 93, 100, 'TW'],
                 ['Nanzi', 'Nanzi', 'District', 'Taiwan', 'Kaohsiung City', 'Nanzi', 996, 93, 100, 'TW'],
                 ['Neimen', 'Neimen', 'District', 'Taiwan', 'Kaohsiung City', 'Neimen', 997, 93, 100, 'TW'],
                 ['Niaosong', 'Niaosong', 'District', 'Taiwan', 'Kaohsiung City', 'Niaosong', 998, 93, 100,
                  'TW'],
                 ['Qianjin', 'Qianjin', 'District', 'Taiwan', 'Kaohsiung City', 'Qianjin', 999, 93, 100, 'TW'],
                 ['Qianzhen', 'Qianzhen', 'District', 'Taiwan', 'Kaohsiung City', 'Qianzhen', 1000, 93, 100,
                  'TW'],
                 ['Qiaotou', 'Qiaotou', 'District', 'Taiwan', 'Kaohsiung City', 'Qiaotou', 1001, 93, 100, 'TW'],
                 ['Qieding', 'Qieding', 'District', 'Taiwan', 'Kaohsiung City', 'Qieding', 1002, 93, 100, 'TW'],
                 ['Qijin', 'Qijin', 'District', 'Taiwan', 'Kaohsiung City', 'Qijin', 1003, 93, 100, 'TW'],
                 ['Qishan', 'Qishan', 'District', 'Taiwan', 'Kaohsiung City', 'Qishan', 1004, 93, 100, 'TW'],
                 ['Renwu', 'Renwu', 'District', 'Taiwan', 'Kaohsiung City', 'Renwu', 1005, 93, 100, 'TW'],
                 ['Sanmin', 'Sanmin', 'District', 'Taiwan', 'Kaohsiung City', 'Sanmin', 1006, 93, 100, 'TW'],
                 ['Shanlin', 'Shanlin', 'District', 'Taiwan', 'Kaohsiung City', 'Shanlin', 1007, 93, 100, 'TW'],
                 ['Taoyuan', 'Taoyuan', 'District', 'Taiwan', 'Kaohsiung City', 'Taoyuan', 1008, 93, 100, 'TW'],
                 ['Tianliao', 'Tianliao', 'District', 'Taiwan', 'Kaohsiung City', 'Tianliao', 1009, 93, 100,
                  'TW'],
                 ['Xiaogang', 'Xiaogang', 'District', 'Taiwan', 'Kaohsiung City', 'Xiaogang', 1010, 93, 100,
                  'TW'],
                 ['Xinxing', 'Xinxing', 'District', 'Taiwan', 'Kaohsiung City', 'Xinxing', 1011, 93, 100, 'TW'],
                 ['Yanchao', 'Yanchao', 'District', 'Taiwan', 'Kaohsiung City', 'Yanchao', 1012, 93, 100, 'TW'],
                 ['Yancheng', 'Yancheng', 'District', 'Taiwan', 'Kaohsiung City', 'Yancheng', 1013, 93, 100,
                  'TW'],
                 ["Yong' an", "Yong' an", 'District', 'Taiwan', 'Kaohsiung City', "Yong' an", 1014, 93, 100,
                  'TW'],
                 ['Ziguan', 'Ziguan', 'District', 'Taiwan', 'Kaohsiung City', 'Ziguan', 1015, 93, 100, 'TW'],
                 ['Zuoying', 'Zuoying', 'District', 'Taiwan', 'Kaohsiung City', 'Zuoying', 1016, 93, 100, 'TW'],
                 ['Dongsha', 'Dongsha', 'Islands', 'Taiwan', 'Kaohsiung City', 'Dongsha', 1017, 93, 100, 'TW'],
                 ['Nansha', 'Nansha', 'Islands', 'Taiwan', 'Kaohsiung City', 'Nansha', 1018, 93, 100, 'TW'],
                 ["Ren'ai", "Ren'ai", 'District', 'Taiwan', 'Keelung City', "Ren'ai", 1019, 93, 101, 'TW'],
                 ['Xinyi', 'Xinyi', 'District', 'Taiwan', 'Keelung City', 'Xinyi', 1020, 93, 101, 'TW'],
                 ['Zhongzheng', 'Zhongzheng', 'District', 'Taiwan', 'Keelung City', 'Zhongzheng', 1021, 93, 101,
                  'TW'],
                 ['Zhongshan', 'Zhongshan', 'District', 'Taiwan', 'Keelung City', 'Zhongshan', 1022, 93, 101,
                  'TW'],
                 ['Anle', 'Anle', 'District', 'Taiwan', 'Keelung City', 'Anle', 1023, 93, 101, 'TW'],
                 ['Nuannuan', 'Nuannuan', 'District', 'Taiwan', 'Keelung City', 'Nuannuan', 1024, 93, 101,
                  'TW'],
                 ['Qidu', 'Qidu', 'District', 'Taiwan', 'Keelung City', 'Qidu', 1025, 93, 101, 'TW'],
                 ['Jincheng', 'Jincheng', 'Township', 'Taiwan', 'Kinmen County', 'Jincheng', 1026, 93, 102,
                  'TW'],
                 ['Jinhu', 'Jinhu', 'Township', 'Taiwan', 'Kinmen County', 'Jinhu', 1027, 93, 102, 'TW'],
                 ['Jinning', 'Jinning', 'Township', 'Taiwan', 'Kinmen County', 'Jinning', 1028, 93, 102, 'TW'],
                 ['Jinsha', 'Jinsha', 'Township', 'Taiwan', 'Kinmen County', 'Jinsha', 1029, 93, 102, 'TW'],
                 ['Lieyu', 'Lieyu', 'Township', 'Taiwan', 'Kinmen County', 'Lieyu', 1030, 93, 102, 'TW'],
                 ['Wuqiu', 'Wuqiu', 'Township', 'Taiwan', 'Kinmen County', 'Wuqiu', 1031, 93, 102, 'TW'],
                 ['Dahu', 'Dahu', 'Township', 'Taiwan', 'Miaoli County', 'Dahu', 1032, 93, 103, 'TW'],
                 ['Gongguan', 'Gongguan', 'Township', 'Taiwan', 'Miaoli County', 'Gongguan', 1033, 93, 103,
                  'TW'],
                 ['Houlong', 'Houlong', 'Township', 'Taiwan', 'Miaoli County', 'Houlong', 1034, 93, 103, 'TW'],
                 ['Miaoli', 'Miaoli', 'City', 'Taiwan', 'Miaoli County', 'Miaoli', 1035, 93, 103, 'TW'],
                 ['Nanzhuang', 'Nanzhuang', 'Township', 'Taiwan', 'Miaoli County', 'Nanzhuang', 1036, 93, 103,
                  'TW'],
                 ['Sanwan', 'Sanwan', 'Township', 'Taiwan', 'Miaoli County', 'Sanwan', 1037, 93, 103, 'TW'],
                 ['Sanyi', 'Sanyi', 'Township', 'Taiwan', 'Miaoli County', 'Sanyi', 1038, 93, 103, 'TW'],
                 ['Shitan', 'Shitan', 'Township', 'Taiwan', 'Miaoli County', 'Shitan', 1039, 93, 103, 'TW'],
                 ["Tai'an", "Tai'an", 'Township', 'Taiwan', 'Miaoli County', "Tai'an", 1040, 93, 103, 'TW'],
                 ['Tongluo', 'Tongluo', 'Township', 'Taiwan', 'Miaoli County', 'Tongluo', 1041, 93, 103, 'TW'],
                 ['Tongxiao', 'Tongxiao', 'Township', 'Taiwan', 'Miaoli County', 'Tongxiao', 1042, 93, 103,
                  'TW'],
                 ['Toufen', 'Toufen', 'City', 'Taiwan', 'Miaoli County', 'Toufen', 1043, 93, 103, 'TW'],
                 ['Touwu', 'Touwu', 'Township', 'Taiwan', 'Miaoli County', 'Touwu', 1044, 93, 103, 'TW'],
                 ['Xihu', 'Xihu', 'Township', 'Taiwan', 'Miaoli County', 'Xihu', 1045, 93, 103, 'TW'],
                 ['Yuanli', 'Yuanli', 'Township', 'Taiwan', 'Miaoli County', 'Yuanli', 1046, 93, 103, 'TW'],
                 ['Zaoqiao', 'Zaoqiao', 'Township', 'Taiwan', 'Miaoli County', 'Zaoqiao', 1047, 93, 103, 'TW'],
                 ['Zhunan', 'Zhunan', 'Township', 'Taiwan', 'Miaoli County', 'Zhunan', 1048, 93, 103, 'TW'],
                 ['Zhuolan', 'Zhuolan', 'Township', 'Taiwan', 'Miaoli County', 'Zhuolan', 1049, 93, 103, 'TW'],
                 ['Caotun', 'Caotun', 'Township', 'Taiwan', 'Nantou County', 'Caotun', 1050, 93, 104, 'TW'],
                 ['Guoxing', 'Guoxing', 'Township', 'Taiwan', 'Nantou County', 'Guoxing', 1051, 93, 104, 'TW'],
                 ['Jiji', 'Jiji', 'Township', 'Taiwan', 'Nantou County', 'Jiji', 1052, 93, 104, 'TW'],
                 ['Lugu', 'Lugu', 'Township', 'Taiwan', 'Nantou County', 'Lugu', 1053, 93, 104, 'TW'],
                 ['Mingjian', 'Mingjian', 'Township', 'Taiwan', 'Nantou County', 'Mingjian', 1054, 93, 104,
                  'TW'],
                 ['Nantou', 'Nantou', 'City', 'Taiwan', 'Nantou County', 'Nantou', 1055, 93, 104, 'TW'],
                 ['Puli', 'Puli', 'Township', 'Taiwan', 'Nantou County', 'Puli', 1056, 93, 104, 'TW'],
                 ["Ren'ai", "Ren'ai", 'Township', 'Taiwan', 'Nantou County', "Ren'ai", 1057, 93, 104, 'TW'],
                 ['Shuili', 'Shuili', 'Township', 'Taiwan', 'Nantou County', 'Shuili', 1058, 93, 104, 'TW'],
                 ['Xinyi', 'Xinyi', 'Township', 'Taiwan', 'Nantou County', 'Xinyi', 1059, 93, 104, 'TW'],
                 ['Yuchi', 'Yuchi', 'Township', 'Taiwan', 'Nantou County', 'Yuchi', 1060, 93, 104, 'TW'],
                 ['Zhongliao', 'Zhongliao', 'Township', 'Taiwan', 'Nantou County', 'Zhongliao', 1061, 93, 104,
                  'TW'],
                 ['Zhushan', 'Zhushan', 'Township', 'Taiwan', 'Nantou County', 'Zhushan', 1062, 93, 104, 'TW'],
                 ['Bali', 'Bali', 'District', 'Taiwan', 'New Taipei City', 'Bali', 1063, 93, 105, 'TW'],
                 ['Banqiao', 'Banqiao', 'District', 'Taiwan', 'New Taipei City', 'Banqiao', 1064, 93, 105,
                  'TW'],
                 ['Gongliao', 'Gongliao', 'District', 'Taiwan', 'New Taipei City', 'Gongliao', 1065, 93, 105,
                  'TW'],
                 ['Linkou', 'Linkou', 'District', 'Taiwan', 'New Taipei City', 'Linkou', 1066, 93, 105, 'TW'],
                 ['Luzhou', 'Luzhou', 'District', 'Taiwan', 'New Taipei City', 'Luzhou', 1067, 93, 105, 'TW'],
                 ['Pinglin', 'Pinglin', 'District', 'Taiwan', 'New Taipei City', 'Pinglin', 1068, 93, 105,
                  'TW'],
                 ['Pingxi', 'Pingxi', 'District', 'Taiwan', 'New Taipei City', 'Pingxi', 1069, 93, 105, 'TW'],
                 ['Ruifang', 'Ruifang', 'District', 'Taiwan', 'New Taipei City', 'Ruifang', 1070, 93, 105,
                  'TW'],
                 ['Sanchong', 'Sanchong', 'District', 'Taiwan', 'New Taipei City', 'Sanchong', 1071, 93, 105,
                  'TW'],
                 ['Sanxia', 'Sanxia', 'District', 'Taiwan', 'New Taipei City', 'Sanxia', 1072, 93, 105, 'TW'],
                 ['Sanzhi', 'Sanzhi', 'District', 'Taiwan', 'New Taipei City', 'Sanzhi', 1073, 93, 105, 'TW'],
                 ['Shenkeng', 'Shenkeng', 'District', 'Taiwan', 'New Taipei City', 'Shenkeng', 1074, 93, 105,
                  'TW'],
                 ['Shiding', 'Shiding', 'District', 'Taiwan', 'New Taipei City', 'Shiding', 1075, 93, 105,
                  'TW'],
                 ['Shimen', 'Shimen', 'District', 'Taiwan', 'New Taipei City', 'Shimen', 1076, 93, 105, 'TW'],
                 ['Shuangxi', 'Shuangxi', 'District', 'Taiwan', 'New Taipei City', 'Shuangxi', 1077, 93, 105,
                  'TW'],
                 ['Shulin', 'Shulin', 'District', 'Taiwan', 'New Taipei City', 'Shulin', 1078, 93, 105, 'TW'],
                 ['Taishan', 'Taishan', 'District', 'Taiwan', 'New Taipei City', 'Taishan', 1079, 93, 105,
                  'TW'],
                 ['Tamsui', 'Tamsui', 'District', 'Taiwan', 'New Taipei City', 'Tamsui', 1080, 93, 105, 'TW'],
                 ['Tucheng', 'Tucheng', 'District', 'Taiwan', 'New Taipei City', 'Tucheng', 1081, 93, 105,
                  'TW'],
                 ['Wugu', 'Wugu', 'District', 'Taiwan', 'New Taipei City', 'Wugu', 1082, 93, 105, 'TW'],
                 ['Wulai', 'Wulai', 'District', 'Taiwan', 'New Taipei City', 'Wulai', 1083, 93, 105, 'TW'],
                 ['Xindian', 'Xindian', 'District', 'Taiwan', 'New Taipei City', 'Xindian', 1084, 93, 105,
                  'TW'],
                 ['Xinzhuang', 'Xinzhuang', 'District', 'Taiwan', 'New Taipei City', 'Xinzhuang', 1085, 93, 105,
                  'TW'],
                 ['Xizhi', 'Xizhi', 'District', 'Taiwan', 'New Taipei City', 'Xizhi', 1086, 93, 105, 'TW'],
                 ['Yingge', 'Yingge', 'District', 'Taiwan', 'New Taipei City', 'Yingge', 1087, 93, 105, 'TW'],
                 ['Yonghe', 'Yonghe', 'District', 'Taiwan', 'New Taipei City', 'Yonghe', 1088, 93, 105, 'TW'],
                 ['Zhonghe', 'Zhonghe', 'District', 'Taiwan', 'New Taipei City', 'Zhonghe', 1089, 93, 105,
                  'TW'],
                 ['Baisha', 'Baisha', 'Township', 'Taiwan', 'Penghu County', 'Baisha', 1090, 93, 106, 'TW'],
                 ['Huxi', 'Huxi', 'Township', 'Taiwan', 'Penghu County', 'Huxi', 1091, 93, 106, 'TW'],
                 ['Magong', 'Magong', 'City', 'Taiwan', 'Penghu County', 'Magong', 1092, 93, 106, 'TW'],
                 ['Qimei', 'Qimei', 'Township', 'Taiwan', 'Penghu County', 'Qimei', 1093, 93, 106, 'TW'],
                 ["Wang'an", "Wang'an", 'Township', 'Taiwan', 'Penghu County', "Wang'an", 1094, 93, 106, 'TW'],
                 ['Xiyu', 'Xiyu', 'Township', 'Taiwan', 'Penghu County', 'Xiyu', 1095, 93, 106, 'TW'],
                 ['Chaozhou', 'Chaozhou', 'Township', 'Taiwan', 'Pingtung County', 'Chaozhou', 1096, 93, 107,
                  'TW'],
                 ['Donggang', 'Donggang', 'Township', 'Taiwan', 'Pingtung County', 'Donggang', 1097, 93, 107,
                  'TW'],
                 ['Hengchun', 'Hengchun', 'Township', 'Taiwan', 'Pingtung County', 'Hengchun', 1098, 93, 107,
                  'TW'],
                 ['Neipu', 'Neipu', 'Township', 'Taiwan', 'Pingtung County', 'Neipu', 1099, 93, 107, 'TW'],
                 ['Pingtung', 'Pingtung', 'City', 'Taiwan', 'Pingtung County', 'Pingtung', 1100, 93, 107, 'TW'],
                 ['Sandimen', 'Sandimen', 'Township', 'Taiwan', 'Pingtung County', 'Sandimen', 1101, 93, 107,
                  'TW'],
                 ['Wutai', 'Wutai', 'Township', 'Taiwan', 'Pingtung County', 'Wutai', 1102, 93, 107, 'TW'],
                 ['Majia', 'Majia', 'Township', 'Taiwan', 'Pingtung County', 'Majia', 1103, 93, 107, 'TW'],
                 ['Jiuru', 'Jiuru', 'Township', 'Taiwan', 'Pingtung County', 'Jiuru', 1104, 93, 107, 'TW'],
                 ['Ligang', 'Ligang', 'Township', 'Taiwan', 'Pingtung County', 'Ligang', 1105, 93, 107, 'TW'],
                 ['Gaoshu', 'Gaoshu', 'Township', 'Taiwan', 'Pingtung County', 'Gaoshu', 1106, 93, 107, 'TW'],
                 ['Yanpu', 'Yanpu', 'Township', 'Taiwan', 'Pingtung County', 'Yanpu', 1107, 93, 107, 'TW'],
                 ['Changzhi', 'Changzhi', 'Township', 'Taiwan', 'Pingtung County', 'Changzhi', 1108, 93, 107,
                  'TW'],
                 ['Linluo', 'Linluo', 'Township', 'Taiwan', 'Pingtung County', 'Linluo', 1109, 93, 107, 'TW'],
                 ['Zhutian', 'Zhutian', 'Township', 'Taiwan', 'Pingtung County', 'Zhutian', 1110, 93, 107,
                  'TW'],
                 ['Wandan', 'Wandan', 'Township', 'Taiwan', 'Pingtung County', 'Wandan', 1111, 93, 107, 'TW'],
                 ['Taiwu', 'Taiwu', 'Township', 'Taiwan', 'Pingtung County', 'Taiwu', 1112, 93, 107, 'TW'],
                 ['Laiyi', 'Laiyi', 'Township', 'Taiwan', 'Pingtung County', 'Laiyi', 1113, 93, 107, 'TW'],
                 ['Wanluan', 'Wanluan', 'Township', 'Taiwan', 'Pingtung County', 'Wanluan', 1114, 93, 107,
                  'TW'],
                 ['Kanding', 'Kanding', 'Township', 'Taiwan', 'Pingtung County', 'Kanding', 1115, 93, 107,
                  'TW'],
                 ['Xinpi', 'Xinpi', 'Township', 'Taiwan', 'Pingtung County', 'Xinpi', 1116, 93, 107, 'TW'],
                 ['Nanzhou', 'Nanzhou', 'Township', 'Taiwan', 'Pingtung County', 'Nanzhou', 1117, 93, 107,
                  'TW'],
                 ['Linbian', 'Linbian', 'Township', 'Taiwan', 'Pingtung County', 'Linbian', 1118, 93, 107,
                  'TW'],
                 ['Liuqiu', 'Liuqiu', 'Township', 'Taiwan', 'Pingtung County', 'Liuqiu', 1119, 93, 107, 'TW'],
                 ['Jiadong', 'Jiadong', 'Township', 'Taiwan', 'Pingtung County', 'Jiadong', 1120, 93, 107,
                  'TW'],
                 ['Xinyuan', 'Xinyuan', 'Township', 'Taiwan', 'Pingtung County', 'Xinyuan', 1121, 93, 107,
                  'TW'],
                 ['Fangliao', 'Fangliao', 'Township', 'Taiwan', 'Pingtung County', 'Fangliao', 1122, 93, 107,
                  'TW'],
                 ['Fangshan', 'Fangshan', 'Township', 'Taiwan', 'Pingtung County', 'Fangshan', 1123, 93, 107,
                  'TW'],
                 ['Chunri', 'Chunri', 'Township', 'Taiwan', 'Pingtung County', 'Chunri', 1124, 93, 107, 'TW'],
                 ['Shizi', 'Shizi', 'Township', 'Taiwan', 'Pingtung County', 'Shizi', 1125, 93, 107, 'TW'],
                 ['Checheng', 'Checheng', 'Township', 'Taiwan', 'Pingtung County', 'Checheng', 1126, 93, 107,
                  'TW'],
                 ['Mudan', 'Mudan', 'Township', 'Taiwan', 'Pingtung County', 'Mudan', 1127, 93, 107, 'TW'],
                 ['Manzhou', 'Manzhou', 'Township', 'Taiwan', 'Pingtung County', 'Manzhou', 1128, 93, 107,
                  'TW'],
                 ['Beitun', 'Beitun', 'District', 'Taiwan', 'Taichung City', 'Beitun', 1129, 93, 108, 'TW'],
                 ['Central', 'Central', 'District', 'Taiwan', 'Taichung City', 'Central', 1130, 93, 108, 'TW'],
                 ["Da'an", "Da'an", 'District', 'Taiwan', 'Taichung City', "Da'an", 1131, 93, 108, 'TW'],
                 ['Dadu', 'Dadu', 'District', 'Taiwan', 'Taichung City', 'Dadu', 1132, 93, 108, 'TW'],
                 ['Dajia', 'Dajia', 'District', 'Taiwan', 'Taichung City', 'Dajia', 1133, 93, 108, 'TW'],
                 ['Dali', 'Dali', 'District', 'Taiwan', 'Taichung City', 'Dali', 1134, 93, 108, 'TW'],
                 ['Daya', 'Daya', 'District', 'Taiwan', 'Taichung City', 'Daya', 1135, 93, 108, 'TW'],
                 ['Dongshi', 'Dongshi', 'District', 'Taiwan', 'Taichung City', 'Dongshi', 1136, 93, 108, 'TW'],
                 ['East', 'East', 'District', 'Taiwan', 'Taichung City', 'East', 1137, 93, 108, 'TW'],
                 ['Fengyuan', 'Fengyuan', 'District', 'Taiwan', 'Taichung City', 'Fengyuan', 1138, 93, 108,
                  'TW'],
                 ['Heping', 'Heping', 'District', 'Taiwan', 'Taichung City', 'Heping', 1139, 93, 108, 'TW'],
                 ['Houli', 'Houli', 'District', 'Taiwan', 'Taichung City', 'Houli', 1140, 93, 108, 'TW'],
                 ['Longjing', 'Longjing', 'District', 'Taiwan', 'Taichung City', 'Longjing', 1141, 93, 108,
                  'TW'],
                 ['Nantun', 'Nantun', 'District', 'Taiwan', 'Taichung City', 'Nantun', 1142, 93, 108, 'TW'],
                 ['North', 'North', 'District', 'Taiwan', 'Taichung City', 'North', 1143, 93, 108, 'TW'],
                 ['Qingshui', 'Qingshui', 'District', 'Taiwan', 'Taichung City', 'Qingshui', 1144, 93, 108,
                  'TW'],
                 ['Shalu', 'Shalu', 'District', 'Taiwan', 'Taichung City', 'Shalu', 1145, 93, 108, 'TW'],
                 ['Shengang', 'Shengang', 'District', 'Taiwan', 'Taichung City', 'Shengang', 1146, 93, 108,
                  'TW'],
                 ['Shigang', 'Shigang', 'District', 'Taiwan', 'Taichung City', 'Shigang', 1147, 93, 108, 'TW'],
                 ['South', 'South', 'District', 'Taiwan', 'Taichung City', 'South', 1148, 93, 108, 'TW'],
                 ['Taiping', 'Taiping', 'District', 'Taiwan', 'Taichung City', 'Taiping', 1149, 93, 108, 'TW'],
                 ['Tanzi', 'Tanzi', 'District', 'Taiwan', 'Taichung City', 'Tanzi', 1150, 93, 108, 'TW'],
                 ['Waipu', 'Waipu', 'District', 'Taiwan', 'Taichung City', 'Waipu', 1151, 93, 108, 'TW'],
                 ['West', 'West', 'District', 'Taiwan', 'Taichung City', 'West', 1152, 93, 108, 'TW'],
                 ['Wufeng', 'Wufeng', 'District', 'Taiwan', 'Taichung City', 'Wufeng', 1153, 93, 108, 'TW'],
                 ['Wuqi', 'Wuqi', 'District', 'Taiwan', 'Taichung City', 'Wuqi', 1154, 93, 108, 'TW'],
                 ['Wuri', 'Wuri', 'District', 'Taiwan', 'Taichung City', 'Wuri', 1155, 93, 108, 'TW'],
                 ['Xinshe', 'Xinshe', 'District', 'Taiwan', 'Taichung City', 'Xinshe', 1156, 93, 108, 'TW'],
                 ['Xitun', 'Xitun', 'District', 'Taiwan', 'Taichung City', 'Xitun', 1157, 93, 108, 'TW'],
                 ['Anding', 'Anding', 'District', 'Taiwan', 'Tainan City', 'Anding', 1158, 93, 109, 'TW'],
                 ['Annan', 'Annan', 'District', 'Taiwan', 'Tainan City', 'Annan', 1159, 93, 109, 'TW'],
                 ['Anping', 'Anping', 'District', 'Taiwan', 'Tainan City', 'Anping', 1160, 93, 109, 'TW'],
                 ['Baihe', 'Baihe', 'District', 'Taiwan', 'Tainan City', 'Baihe', 1161, 93, 109, 'TW'],
                 ['Beimen', 'Beimen', 'District', 'Taiwan', 'Tainan City', 'Beimen', 1162, 93, 109, 'TW'],
                 ['Danei', 'Danei', 'District', 'Taiwan', 'Tainan City', 'Danei', 1163, 93, 109, 'TW'],
                 ['Dongshan', 'Dongshan', 'District', 'Taiwan', 'Tainan City', 'Dongshan', 1164, 93, 109, 'TW'],
                 ['East', 'East', 'District', 'Taiwan', 'Tainan City', 'East', 1165, 93, 109, 'TW'],
                 ['Guanmiao', 'Guanmiao', 'District', 'Taiwan', 'Tainan City', 'Guanmiao', 1166, 93, 109, 'TW'],
                 ['Guantian', 'Guantian', 'District', 'Taiwan', 'Tainan City', 'Guantian', 1167, 93, 109, 'TW'],
                 ['Guiren', 'Guiren', 'District', 'Taiwan', 'Tainan City', 'Guiren', 1168, 93, 109, 'TW'],
                 ['Houbi', 'Houbi', 'District', 'Taiwan', 'Tainan City', 'Houbi', 1169, 93, 109, 'TW'],
                 ['Jiali', 'Jiali', 'District', 'Taiwan', 'Tainan City', 'Jiali', 1170, 93, 109, 'TW'],
                 ['Jiangjun', 'Jiangjun', 'District', 'Taiwan', 'Tainan City', 'Jiangjun', 1171, 93, 109, 'TW'],
                 ['Liujia', 'Liujia', 'District', 'Taiwan', 'Tainan City', 'Liujia', 1172, 93, 109, 'TW'],
                 ['Liuying', 'Liuying', 'District', 'Taiwan', 'Tainan City', 'Liuying', 1173, 93, 109, 'TW'],
                 ['Longqi', 'Longqi', 'District', 'Taiwan', 'Tainan City', 'Longqi', 1174, 93, 109, 'TW'],
                 ['Madou', 'Madou', 'District', 'Taiwan', 'Tainan City', 'Madou', 1175, 93, 109, 'TW'],
                 ['Nanhua', 'Nanhua', 'District', 'Taiwan', 'Tainan City', 'Nanhua', 1176, 93, 109, 'TW'],
                 ['Nanxi', 'Nanxi', 'District', 'Taiwan', 'Tainan City', 'Nanxi', 1177, 93, 109, 'TW'],
                 ['North', 'North', 'District', 'Taiwan', 'Tainan City', 'North', 1178, 93, 109, 'TW'],
                 ['Qigu', 'Qigu', 'District', 'Taiwan', 'Tainan City', 'Qigu', 1179, 93, 109, 'TW'],
                 ['Rende', 'Rende', 'District', 'Taiwan', 'Tainan City', 'Rende', 1180, 93, 109, 'TW'],
                 ['Shanhua', 'Shanhua', 'District', 'Taiwan', 'Tainan City', 'Shanhua', 1181, 93, 109, 'TW',
                  ['Shanshang', 'Shanshang', 'District', 'Taiwan', 'Tainan City', 'Shanshang', 1182, 93, 109,
                   'TW'],
                  ['South', 'South', 'District', 'Taiwan', 'Tainan City', 'South', 1183, 93, 109, 'TW'],
                  ['West Central', 'West Central', 'District', 'Taiwan', 'Tainan City', 'West Central', 1184,
                   93, 109, 'TW'],
                  ['Xiaying', 'Xiaying', 'District', 'Taiwan', 'Tainan City', 'Xiaying', 1185, 93, 109, 'TW'],
                  ['Xigang', 'Xigang', 'District', 'Taiwan', 'Tainan City', 'Xigang', 1186, 93, 109, 'TW'],
                  ['Xinhua', 'Xinhua', 'District', 'Taiwan', 'Tainan City', 'Xinhua', 1187, 93, 109, 'TW'],
                  ['Xinshi', 'Xinshi', 'District', 'Taiwan', 'Tainan City', 'Xinshi', 1188, 93, 109, 'TW'],
                  ['Xinying', 'Xinying', 'District', 'Taiwan', 'Tainan City', 'Xinying', 1189, 93, 109, 'TW'],
                  ['Xuejia', 'Xuejia', 'District', 'Taiwan', 'Tainan City', 'Xuejia', 1190, 93, 109, 'TW'],
                  ['Yanshui', 'Yanshui', 'District', 'Taiwan', 'Tainan City', 'Yanshui', 1191, 93, 109, 'TW'],
                  ['Yongkang', 'Yongkang', 'District', 'Taiwan', 'Tainan City', 'Yongkang', 1192, 93, 109,
                   'TW'],
                  ['Yujing', 'Yujing', 'District', 'Taiwan', 'Tainan City', 'Yujing', 1193, 93, 109, 'TW'],
                  ['Zuozhen', 'Zuozhen', 'District', 'Taiwan', 'Tainan City', 'Zuozhen', 1194, 93, 109, 'TW'],
                  ['Beitou', 'Beitou', 'District', 'Taiwan', 'Taipei City', 'Beitou', 1195, 93, 110, 'TW'],
                  ["Da'an", "Da'an", 'District', 'Taiwan', 'Taipei City', "Da'an", 1196, 93, 110, 'TW'],
                  ['Datong', 'Datong', 'District', 'Taiwan', 'Taipei City', 'Datong', 1197, 93, 110, 'TW,'],
                  ['Nangang', 'Nangang', 'District', 'Taiwan', 'Taipei City', 'Nangang', 1198, 93, 110, 'TW'],
                  ['Neihu', 'Neihu', 'District', 'Taiwan', 'Taipei City', 'Neihu', 1199, 93, 110, 'TW'],
                  ['Shilin', 'Shilin', 'District', 'Taiwan', 'Taipei City', 'Shilin', 1200, 93, 110, 'TW'],
                  ['Songshan', 'Songshan', 'District', 'Taiwan', 'Taipei City', 'Songshan', 1201, 93, 110,
                   'TW'],
                  ['Wanhua', 'Wanhua', 'District', 'Taiwan', 'Taipei City', 'Wanhua', 1202, 93, 110, 'TW'],
                  ['Wenshan', 'Wenshan', 'District', 'Taiwan', 'Taipei City', 'Wenshan', 1203, 93, 110, 'TW'],
                  ['Xinyi', 'Xinyi', 'District', 'Taiwan', 'Taipei City', 'Xinyi', 1204, 93, 110, 'TW'],
                  'Zhongshan', 'Zhongshan', 'District', 'Taiwan', 'Taipei City', 'Zhongshan', 1205, 93, 110,
                  'TW'],
                 [
                     'Zhongzheng', 'Zhongzheng', 'District', 'Taiwan', 'Taipei City', 'Zhongzheng', 1206, 93,
                     110, 'TW'],
                 ['Beinan', 'Beinan', 'Township', 'Taiwan', 'Taitung County', 'Beinan', 1207, 93, 111, 'TW'],
                 [
                     'Changbin', 'Changbin', 'Township', 'Taiwan', 'Taitung County', 'Changbin', 1208, 93, 111,
                     'TW'],
                 [
                     'Chenggong', 'Chenggong', 'Township', 'Taiwan', 'Taitung County', 'Chenggong', 1209, 93,
                     111, 'TW'],
                 [
                     'Chishang', 'Chishang', 'Township', 'Taiwan', 'Taitung County', 'Chishang', 1210, 93, 111,
                     'TW'],
                 ['Daren', 'Daren', 'Township', 'Taiwan', 'Taitung County', 'Daren', 1211, 93, 111, 'TW'],
                 ['Dawu', 'Dawu', 'Township', 'Taiwan', 'Taitung County', 'Dawu', 1212, 93, 111, 'TW'],
                 ['Donghe', 'Donghe', 'Township', 'Taiwan', 'Taitung County', 'Donghe', 1213, 93, 111, 'TW'],
                 [
                     'Guanshan', 'Guanshan', 'Township', 'Taiwan', 'Taitung County', 'Guanshan', 1214, 93, 111,
                     'TW'],
                 ['Haiduan', 'Haiduan', 'Township', 'Taiwan', 'Taitung County', 'Haiduan', 1215, 93, 111, 'TW'],
                 ['Jinfeng', 'Jinfeng', 'Township', 'Taiwan', 'Taitung County', 'Jinfeng', 1216, 93, 111, 'TW'],
                 ['Lanyu', 'Lanyu', 'Township', 'Taiwan', 'Taitung County', 'Lanyu', 1217, 93, 111, 'TW'],
                 ['Ludao', 'Ludao', 'Township', 'Taiwan', 'Taitung County', 'Ludao', 1218, 93, 111, 'TW'],
                 ['Luye', 'Luye', 'Township', 'Taiwan', 'Taitung County', 'Luye', 1219, 93, 111, 'TW'],
                 ['Taimali', 'Taimali', 'Township', 'Taiwan', 'Taitung County', 'Taimali', 1220, 93, 111,
                  'TW'],
                 ['Taitung', 'Taitung', 'City', 'Taiwan', 'Taitung County', 'Taitung', 1221, 93, 111, 'TW'],
                 ['Yanping', 'Yanping', 'Township', 'Taiwan', 'Taitung County', 'Yanping', 1222, 93, 111,
                  'TW'],
                 ['Bade', 'Bade', 'District', 'Taiwan', 'Taoyuan City', 'Bade', 1223, 93, 112, 'TW'],
                 ['Daxi', 'Daxi', 'District', 'Taiwan', 'Taoyuan City', 'Daxi', 1224, 93, 112, 'TW'],
                 ['Dayuan', 'Dayuan', 'District', 'Taiwan', 'Taoyuan City', 'Dayuan', 1225, 93, 112, 'TW'],
                 ['Fuxing', 'Fuxing', 'District', 'Taiwan', 'Taoyuan City', 'Fuxing', 1226, 93, 112, 'TW'],
                 ['Guanyin', 'Guanyin', 'District', 'Taiwan', 'Taoyuan City', 'Guanyin', 1227, 93, 112, 'TW'],
                 ['Guishan', 'Guishan', 'District', 'Taiwan', 'Taoyuan City', 'Guishan', 1228, 93, 112, 'TW'],
                 ['Longtan', 'Longtan', 'District', 'Taiwan', 'Taoyuan City', 'Longtan', 1229, 93, 112, 'TW'],
                 ['Luzhu', 'Luzhu', 'District', 'Taiwan', 'Taoyuan City', 'Luzhu', 1230, 93, 112, 'TW'],
                 ['Pingzhen', 'Pingzhen', 'District', 'Taiwan', 'Taoyuan City', 'Pingzhen', 1231, 93, 112,
                  'TW'],
                 ['Taoyuan', 'Taoyuan', 'District', 'Taiwan', 'Taoyuan City', 'Taoyuan', 1232, 93, 112, 'TW'],
                 ['Xinwu', 'Xinwu', 'District', 'Taiwan', 'Taoyuan City', 'Xinwu', 1233, 93, 112, 'TW'],
                 ['Yangmei', 'Yangmei', 'District', 'Taiwan', 'Taoyuan City', 'Yangmei', 1234, 93, 112, 'TW'],
                 ['Zhongli', 'Zhongli', 'District', 'Taiwan', 'Taoyuan City', 'Zhongli', 1235, 93, 112, 'TW'],
                 ['Datong', 'Datong', 'Township', 'Taiwan', 'Yilan County', 'Datong', 1236, 93, 113, 'TW'],
                 ['Dongshan', 'Dongshan', 'Township', 'Taiwan', 'Yilan County', 'Dongshan', 1237, 93, 113,
                  'TW'],
                 ['Jiaoxi', 'Jiaoxi', 'Township', 'Taiwan', 'Yilan County', 'Jiaoxi', 1238, 93, 113, 'TW'],
                 ['Luodong', 'Luodong', 'Township', 'Taiwan', 'Yilan County', 'Luodong', 1239, 93, 113, 'TW'],
                 ["Nan'ao", "Nan'ao", 'Township', 'Taiwan', 'Yilan County', "Nan'ao", 1240, 93, 113, 'TW'],
                 ['Sanxing', 'Sanxing', 'Township', 'Taiwan', 'Yilan County', 'Sanxing', 1241, 93, 113, 'TW'],
                 ["Su'ao", "Su'ao", 'Township', 'Taiwan', 'Yilan County', "Su'ao", 1242, 93, 113, 'TW'],
                 ['Toucheng', 'Toucheng', 'Township', 'Taiwan', 'Yilan County', 'Toucheng', 1243, 93, 113,
                  'TW'],
                 ['Wujie', 'Wujie', 'Township', 'Taiwan', 'Yilan County', 'Wujie', 1244, 93, 113, 'TW'],
                 ['Yilan', 'Yilan', 'City', 'Taiwan', 'Yilan County', 'Yilan', 1245, 93, 113, 'TW'],
                 ['Yuanshan', 'Yuanshan', 'Township', 'Taiwan', 'Yilan County', 'Yuanshan', 1246, 93, 113,
                  'TW'],
                 ['Zhuangwei', 'Zhuangwei', 'Township', 'Taiwan', 'Yilan County', 'Zhuangwei', 1247, 93, 113,
                  'TW'],
                 ['Baozhong', 'Baozhong', 'Township', 'Taiwan', 'Yunlin County', 'Baozhong', 1248, 93, 114,
                  'TW'],
                 ['Beigang', 'Beigang', 'Township', 'Taiwan', 'Yunlin County', 'Beigang', 1249, 93, 114, 'TW'],
                 ['Citong', 'Citong', 'Township', 'Taiwan', 'Yunlin County', 'Citong', 1250, 93, 114, 'TW'],
                 ['Dapi', 'Dapi', 'Township', 'Taiwan', 'Yunlin County', 'Dapi', 1251, 93, 114, 'TW'],
                 ['Dongshi', 'Dongshi', 'Township', 'Taiwan', 'Yunlin County', 'Dongshi', 1252, 93, 114, 'TW'],
                 ['Douliu', 'Douliu', 'City', 'Taiwan', 'Yunlin County', 'Douliu', 1253, 93, 114, 'TW'],
                 ['Dounan', 'Dounan', 'Township', 'Taiwan', 'Yunlin County', 'Dounan', 1254, 93, 114, 'TW'],
                 ['Erlun', 'Erlun', 'Township', 'Taiwan', 'Yunlin County', 'Erlun', 1255, 93, 114, 'TW'],
                 ['Gukeng', 'Gukeng', 'Township', 'Taiwan', 'Yunlin County', 'Gukeng', 1256, 93, 114, 'TW'],
                 ['Huwei', 'Huwei', 'Township', 'Taiwan', 'Yunlin County', 'Huwei', 1257, 93, 114, 'TW'],
                 ['Kouhu', 'Kouhu', 'Township', 'Taiwan', 'Yunlin County', 'Kouhu', 1258, 93, 114, 'TW'],
                 ['Linnei', 'Linnei', 'Township', 'Taiwan', 'Yunlin County', 'Linnei', 1259, 93, 114, 'TW'],
                 ['Lunbei', 'Lunbei', 'Township', 'Taiwan', 'Yunlin County', 'Lunbei', 1260, 93, 114, 'TW'],
                 ['Mailiao', 'Mailiao', 'Township', 'Taiwan', 'Yunlin County', 'Mailiao', 1261, 93, 114, 'TW'],
                 ['Shuilin', 'Shuilin', 'Township', 'Taiwan', 'Yunlin County', 'Shuilin', 1262, 93, 114, 'TW'],
                 ['Sihu', 'Sihu', 'Township', 'Taiwan', 'Yunlin County', 'Sihu', 1263, 93, 114, 'TW'],
                 ['Taixi', 'Taixi', 'Township', 'Taiwan', 'Yunlin County', 'Taixi', 1264, 93, 114, 'TW'],
                 ['Tuku', 'Tuku', 'Township', 'Taiwan', 'Yunlin County', 'Tuku', 1265, 93, 114, 'TW'],
                 ['Xiluo', 'Xiluo', 'Township', 'Taiwan', 'Yunlin County', 'Xiluo', 1266, 93, 114, 'TW'],
                 ['Yuanzhang', 'Yuanzhang', 'Township', 'Taiwan', 'Yunlin County', 'Yuanzhang', 1267, 93, 114,
                  'TW']]


class TestTWVponGeoService(TestCase):

    def test_match_case2(self):
        service = GeneralVponGeoService()

        google_geo_dict = {
            1012808: GoogleGeoDTO(1012808, 'Chiayi City', ['Taiwan', 'Taiwan', 'Chiayi City'], '90,759,672,158', '',
                                  "TW", 'City')
        }
        result = service.match(google_geo_dict, vpon_geo_list)
        self.assertEqual(result[0].criteria_id, 1012808)
        self.assertEqual(result[0].tier1, 93)
        self.assertEqual(result[0].tier2, 95)
        self.assertEqual(result[0].tier3, None)

    def test_match_case1(self):
        service = GeneralVponGeoService()
        google_geo_dict = {
            1012809: GoogleGeoDTO(1012809, 'Zhudong Township', ['Taiwan', 'Taiwan', 'Zhudong'], '90,759,672,158', '',
                                  "TW", 'City')
        }

        result = service.match(google_geo_dict, vpon_geo_list)
        self.assertEqual(result[0].criteria_id, 1012809)
        self.assertEqual(result[0].tier1, 93)
        self.assertEqual(result[0].tier2, 98)
        self.assertEqual(result[0].tier3, 965)

    def test_match_case3(self):
        service = GeneralVponGeoService()
        google_geo_dict = {
            9040310: GoogleGeoDTO(9040310, 'Kinmen County', ['Taiwan', 'Fujian', 'Kinmen County'], '90,759,672,158', '',
                                  "TW", 'City')
        }
        # 102	93
        # 9040310,Kinmen County,"Kinmen County,Fujian Province,Taiwan","9069534,2158",,TW,County
        result = service.match(google_geo_dict, vpon_geo_list)
        self.assertEqual(result[0].criteria_id, 9040310)
        self.assertEqual(result[0].tier1, 93)
        self.assertEqual(result[0].tier2, 102)

    def test_match_case4(self):
        service = GeneralVponGeoService()
        google_geo_dict = {
            9040379: GoogleGeoDTO(9040379, 'Taipei City', ['Taiwan', 'Taipei City'], '90,759,672,158', '',
                                  "TW", 'City')
        }
        # 110	93
        # 9040379,Taipei City,"Taipei City,Taiwan",2158,,TW,City
        result = service.match(google_geo_dict, vpon_geo_list)
        self.assertEqual(result[0].criteria_id, 9040379)
        self.assertEqual(result[0].tier1, 93)
        self.assertEqual(result[0].tier2, 110)

    def test_match_case5(self):
        service = GeneralVponGeoService()
        google_geo_dict = {
            1012826: GoogleGeoDTO(1012826, 'Taoyuan District', ['Taiwan', 'Taoyuan City', 'Taoyuan'], '90,759,672,158',
                                  '',
                                  "TW", 'City')
        }
        # 110	93
        # 9040379,Taipei City,"Taipei City,Taiwan",2158,,TW,City
        result = service.match(google_geo_dict, vpon_geo_list)
        self.assertEqual(result[0].criteria_id, 1012826)
        self.assertEqual(result[0].tier1, 93)
        self.assertEqual(result[0].tier2, 112)
        self.assertEqual(result[0].tier3, 1232)

    def test_match_case6(self):
        service = GeneralVponGeoService()
        google_geo_dict = {
            1012812: GoogleGeoDTO(1012812, 'Yilan City', ['Taiwan', 'Taiwan', 'Yilan City'], '90,759,672,158',
                                  '',
                                  "TW", 'City')
        }

        result = service.match(google_geo_dict, vpon_geo_list)
        self.assertEqual(result[0].criteria_id, 1012812)
        self.assertEqual(result[0].tier1, 93)
        self.assertEqual(result[0].tier2, 113)
        self.assertEqual(result[0].tier3, 1245)

    def test_match_case7(self):
        # {'criteria_id': 9041334, 'id': 'Taiwan Taoyuan International Airport', 'name': ['Taiwan', 'Taoyuan City', 'Taiwan Taoyuan International Airport'], 'parentId': '9040290,21102,2158', 'region_code': '', 'country_code': 'TW', 'target_type': 'Airport'}
        service = GeneralVponGeoService()
        google_geo_dict = {
            9041334: GoogleGeoDTO(9041334, 'Taiwan Taoyuan International Airport',
                                  ['Taiwan', 'Taoyuan City', 'Taiwan Taoyuan International Airport'], '90,759,672,158',
                                  '',
                                  "TW", 'City')
        }

        result = service.match(google_geo_dict, vpon_geo_list)
        self.assertEqual(result[0].criteria_id, 9041334)
        self.assertEqual(result[0].tier1, 93)
        self.assertEqual(result[0].tier2, 112)

    def test_match_case8(self):
        service = GeneralVponGeoService()
        # {'criteria_id': 9040311, 'id': 'Pingtung City', 'name': ['Taiwan', 'Taiwan', 'Pingtung City'], 'parentId': '9040321,9075967,2158', 'region_code': '', 'country_code': 'TW', 'target_type': 'City'}
        google_geo_dict = {
            9040311: GoogleGeoDTO(9040311, 'Pingtung City', ['Taiwan', 'Taiwan', 'Pingtung City'], '90,759,672,158',
                                  '',
                                  "TW", 'City')
        }

        result = service.match(google_geo_dict, vpon_geo_list)
        print(result[0].__dict__)
        self.assertEqual(result[0].criteria_id, 9040311)
        self.assertEqual(result[0].tier1, 93)
        self.assertEqual(result[0].tier2, 107)
        self.assertEqual(result[0].tier3, 1100)

    def test_match_case9(self):
        service = GeneralVponGeoService()
        # {'criteria_id': 9040309, 'id': 'Miaoli City', 'name': ['Taiwan', 'Taiwan', 'Miaoli City'], 'parentId': '21300,9075967,2158', 'region_code': '', 'country_code': 'TW', 'target_type': 'City'}
        google_geo_dict = {
            9040309: GoogleGeoDTO(9040309, 'Miaoli City', ['Taiwan', 'Taiwan', 'Miaoli City'], '90,759,672,158',
                                  '',
                                  "TW", 'City')
        }

        result = service.match(google_geo_dict, vpon_geo_list)
        print(result[0].__dict__)
        self.assertEqual(result[0].criteria_id, 9040309)
        self.assertEqual(result[0].tier1, 93)
        self.assertEqual(result[0].tier2, 103)
        self.assertEqual(result[0].tier3, 1035)

    def test_match_case9(self):
        service = GeneralVponGeoService()
        # {'criteria_id': 9040304, 'id': 'Changhua City', 'name': ['Taiwan', 'Taiwan', 'Changhua City'], 'parentId': '9040307,9075967,2158', 'region_code': '', 'country_code': 'TW', 'target_type': 'City'}
        google_geo_dict = {
            9040304: GoogleGeoDTO(9040304, 'Changhua City', ['Taiwan', 'Taiwan', 'Changhua City'], '90,759,672,158',
                                  '',
                                  "TW", 'City')
        }

        result = service.match(google_geo_dict, vpon_geo_list)
        print(result[0].__dict__)
        self.assertEqual(result[0].criteria_id, 9040304)
        self.assertEqual(result[0].tier1, 93)
        self.assertEqual(result[0].tier2, 94)
        self.assertEqual(result[0].tier3, 905)

    def test_match_case9(self):
        service = GeneralVponGeoService()
        google_geo_dict = {
            9041336: GoogleGeoDTO(9041336, 'Hualien Airport', ['Taiwan', 'Taiwan', 'Hualien County'], '90,759,672,158',
                                  '',
                                  "TW", 'City')
        }

        result = service.match(google_geo_dict, vpon_geo_list)
        print(result[0].__dict__)
        self.assertEqual(result[0].criteria_id, 9041336)
        self.assertEqual(result[0].tier1, 93)
        self.assertEqual(result[0].tier2, 99)
        self.assertEqual(result[0].tier3, None)
