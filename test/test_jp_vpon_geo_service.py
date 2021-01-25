from unittest import TestCase

from usecase.dto.google_geo_dto import GoogleGeoDTO
from usecase.jp_vpon_geo_service import JPVponGeoService

vpon_geo_list = [['Japan', 'Japan', 'Country', 'Japan', None, None, 38, 0, 0, 'JP'],
                 ['Aichi Prefecture', 'Aichi Prefecture', 'Prefecture', 'Japan', 'Aichi', None, 39, 38, 0, 'JP'],
                 ['Akita Prefecture', 'Akita Prefecture', 'Prefecture', 'Japan', 'Akita', None, 40, 38, 0, 'JP'],
                 ['Aomori Prefecture', 'Aomori Prefecture', 'Prefecture', 'Japan', 'Aomori', None, 41, 38, 0, 'JP'],
                 ['Chiba Prefecture', 'Chiba Prefecture', 'Prefecture', 'Japan', 'Chiba', None, 42, 38, 0, 'JP'],
                 ['Ehime Prefecture', 'Ehime Prefecture', 'Prefecture', 'Japan', 'Ehime', None, 43, 38, 0, 'JP'],
                 ['Fukui Prefecture', 'Fukui Prefecture', 'Prefecture', 'Japan', 'Fukui', None, 44, 38, 0, 'JP'],
                 ['Fukuoka Prefecture', 'Fukuoka Prefecture', 'Prefecture', 'Japan', 'Fukuoka', None, 45, 38, 0, 'JP'],
                 ['Fukushima Prefecture', 'Fukushima Prefecture', 'Prefecture', 'Japan', 'Fukushima', None, 46, 38, 0,
                  'JP'],
                 ['Gifu Prefecture', 'Gifu Prefecture', 'Prefecture', 'Japan', 'Gifu', None, 47, 38, 0, 'JP'],
                 ['Gunma Prefecture', 'Gunma Prefecture', 'Prefecture', 'Japan', 'Gunma', None, 48, 38, 0, 'JP'],
                 ['Hiroshima Prefecture', 'Hiroshima Prefecture', 'Prefecture', 'Japan', 'Hiroshima', None, 49, 38, 0,
                  'JP'],
                 ['Hokkaido', 'Hokkaido', 'Prefecture', 'Japan', 'Hokkaido', None, 50, 38, 0, 'JP'],
                 ['Hyogo Prefecture', 'Hyogo Prefecture', 'Prefecture', 'Japan', 'Hyogo', None, 51, 38, 0, 'JP'],
                 ['Ibaraki Prefecture', 'Ibaraki Prefecture', 'Prefecture', 'Japan', 'Ibaraki', None, 52, 38, 0, 'JP'],
                 ['Ishikawa Prefecture', 'Ishikawa Prefecture', 'Prefecture', 'Japan', 'Ishikawa', None, 53, 38, 0,
                  'JP'],
                 ['Iwate Prefecture', 'Iwate Prefecture', 'Prefecture', 'Japan', 'Iwate', None, 54, 38, 0, 'JP'],
                 ['Kagawa Prefecture', 'Kagawa Prefecture', 'Prefecture', 'Japan', 'Kagawa', None, 55, 38, 0, 'JP'],
                 ['Kagoshima Prefecture', 'Kagoshima Prefecture', 'Prefecture', 'Japan', 'Kagoshima', None, 56, 38, 0,
                  'JP'],
                 ['Kanagawa Prefecture', 'Kanagawa Prefecture', 'Prefecture', 'Japan', 'Kanagawa', None, 57, 38, 0,
                  'JP'],
                 ['Kochi Prefecture', 'Kochi Prefecture', 'Prefecture', 'Japan', 'Kochi', None, 58, 38, 0, 'JP'],
                 ['Kumamoto Prefecture', 'Kumamoto Prefecture', 'Prefecture', 'Japan', 'Kumamoto', None, 59, 38, 0,
                  'JP'],
                 ['Kyoto Prefecture', 'Kyoto Prefecture', 'Prefecture', 'Japan', 'Kyoto', None, 60, 38, 0, 'JP'],
                 ['Mie Prefecture', 'Mie Prefecture', 'Prefecture', 'Japan', 'Mie', None, 61, 38, 0, 'JP'],
                 ['Miyagi Prefecture', 'Miyagi Prefecture', 'Prefecture', 'Japan', 'Miyagi', None, 62, 38, 0, 'JP'],
                 ['Miyazaki Prefecture', 'Miyazaki Prefecture', 'Prefecture', 'Japan', 'Miyazaki', None, 63, 38, 0,
                  'JP'],
                 ['Nagano Prefecture', 'Nagano Prefecture', 'Prefecture', 'Japan', 'Nagano', None, 64, 38, 0, 'JP'],
                 ['Nagasaki Prefecture', 'Nagasaki Prefecture', 'Prefecture', 'Japan', 'Nagasaki', None, 65, 38, 0,
                  'JP'],
                 ['Nara Prefecture', 'Nara Prefecture', 'Prefecture', 'Japan', 'Nara', None, 66, 38, 0, 'JP'],
                 ['Niigata Prefecture', 'Niigata Prefecture', 'Prefecture', 'Japan', 'Niigata', None, 67, 38, 0, 'JP'],
                 ['Oita Prefecture', 'Oita Prefecture', 'Prefecture', 'Japan', 'Oita', None, 68, 38, 0, 'JP'],
                 ['Okayama Prefecture', 'Okayama Prefecture', 'Prefecture', 'Japan', 'Okayama', None, 69, 38, 0, 'JP'],
                 ['Okinawa Prefecture', 'Okinawa Prefecture', 'Prefecture', 'Japan', 'Okinawa', None, 70, 38, 0, 'JP'],
                 ['Osaka Prefecture', 'Osaka Prefecture', 'Prefecture', 'Japan', 'Osaka', None, 71, 38, 0, 'JP'],
                 ['Saga Prefecture', 'Saga Prefecture', 'Prefecture', 'Japan', 'Saga', None, 72, 38, 0, 'JP'],
                 ['Saitama Prefecture', 'Saitama Prefecture', 'Prefecture', 'Japan', 'Saitama', None, 73, 38, 0, 'JP'],
                 ['Shiga Prefecture', 'Shiga Prefecture', 'Prefecture', 'Japan', 'Shiga', None, 74, 38, 0, 'JP'],
                 ['Shimane Prefecture', 'Shimane Prefecture', 'Prefecture', 'Japan', 'Shimane', None, 75, 38, 0, 'JP'],
                 ['Shizuoka Prefecture', 'Shizuoka Prefecture', 'Prefecture', 'Japan', 'Shizuoka', None, 76, 38, 0,
                  'JP'],
                 ['Tochigi Prefecture', 'Tochigi Prefecture', 'Prefecture', 'Japan', 'Tochigi', None, 77, 38, 0, 'JP'],
                 ['Tokushima Prefecture', 'Tokushima Prefecture', 'Prefecture', 'Japan', 'Tokushima', None, 78, 38, 0,
                  'JP'],
                 ['Tokyo', 'Tokyo', 'Prefecture', 'Japan', 'Tokyo', None, 79, 38, 0, 'JP'],
                 ['Tottori Prefecture', 'Tottori Prefecture', 'Prefecture', 'Japan', 'Tottori', None, 80, 38, 0, 'JP'],
                 ['Toyama Prefecture', 'Toyama Prefecture', 'Prefecture', 'Japan', 'Toyama', None, 81, 38, 0, 'JP'],
                 ['Wakayama Prefecture', 'Wakayama Prefecture', 'Prefecture', 'Japan', 'Wakayama', None, 82, 38, 0,
                  'JP'],
                 ['Yamagata Prefecture', 'Yamagata Prefecture', 'Prefecture', 'Japan', 'Yamagata', None, 83, 38, 0,
                  'JP'],
                 ['Yamaguchi Prefecture', 'Yamaguchi Prefecture', 'Prefecture', 'Japan', 'Yamaguchi', None, 84, 38, 0,
                  'JP'],
                 ['Yamanashi Prefecture', 'Yamanashi Prefecture', 'Prefecture', 'Japan', 'Yamanashi', None, 85, 38, 0,
                  'JP'],
                 ['Aisai', 'Aisai', 'City', 'Japan', 'Aichi', 'Aisai', 1271, 38, 39, 'JP'],
                 ['Anjo', 'Anjo', 'City', 'Japan', 'Aichi', 'Anjo', 1272, 38, 39, 'JP'],
                 ['Chiryu', 'Chiryu', 'City', 'Japan', 'Aichi', 'Chiryu', 1273, 38, 39, 'JP'],
                 ['Chita', 'Chita', 'City', 'Japan', 'Aichi', 'Chita', 1274, 38, 39, 'JP'],
                 ['Gamagori', 'Gamagori', 'City', 'Japan', 'Aichi', 'Gamagori', 1275, 38, 39, 'JP'],
                 ['Handa', 'Handa', 'City', 'Japan', 'Aichi', 'Handa', 1276, 38, 39, 'JP'],
                 ['Hekinan', 'Hekinan', 'City', 'Japan', 'Aichi', 'Hekinan', 1277, 38, 39, 'JP'],
                 ['Higashiura', 'Higashiura', 'City', 'Japan', 'Aichi', 'Higashiura', 1278, 38, 39, 'JP'],
                 ['Ichinomiya', 'Ichinomiya', 'City', 'Japan', 'Aichi', 'Ichinomiya', 1279, 38, 39, 'JP'],
                 ['Inazawa', 'Inazawa', 'City', 'Japan', 'Aichi', 'Inazawa', 1280, 38, 39, 'JP'],
                 ['Inuyama', 'Inuyama', 'City', 'Japan', 'Aichi', 'Inuyama', 1281, 38, 39, 'JP'],
                 ['Kariya', 'Kariya', 'City', 'Japan', 'Aichi', 'Kariya', 1282, 38, 39, 'JP'],
                 ['Kasugai', 'Kasugai', 'City', 'Japan', 'Aichi', 'Kasugai', 1283, 38, 39, 'JP'],
                 ['Komaki', 'Komaki', 'City', 'Japan', 'Aichi', 'Komaki', 1284, 38, 39, 'JP'],
                 ['Konan', 'Konan', 'City', 'Japan', 'Aichi', 'Konan', 1285, 38, 39, 'JP'],
                 ['Kota', 'Kota', 'City', 'Japan', 'Aichi', 'Kota', 1286, 38, 39, 'JP'],
                 ['Mihama', 'Mihama', 'City', 'Japan', 'Aichi', 'Mihama', 1287, 38, 39, 'JP'],
                 ['Miyoshi', 'Miyoshi', 'City', 'Japan', 'Aichi', 'Miyoshi', 1288, 38, 39, 'JP'],
                 ['Nagakute', 'Nagakute', 'City', 'Japan', 'Aichi', 'Nagakute', 1289, 38, 39, 'JP'],
                 ['Nagoya', 'Nagoya', 'City', 'Japan', 'Aichi', 'Nagoya', 1290, 38, 39, 'JP'],
                 ['Nishio', 'Nishio', 'City', 'Japan', 'Aichi', 'Nishio', 1291, 38, 39, 'JP'],
                 ['Nisshin', 'Nisshin', 'City', 'Japan', 'Aichi', 'Nisshin', 1292, 38, 39, 'JP'],
                 ['Obu', 'Obu', 'City', 'Japan', 'Aichi', 'Obu', 1293, 38, 39, 'JP'],
                 ['Oguchi', 'Oguchi', 'City', 'Japan', 'Aichi', 'Oguchi', 1294, 38, 39, 'JP'],
                 ['Okazaki', 'Okazaki', 'City', 'Japan', 'Aichi', 'Okazaki', 1295, 38, 39, 'JP'],
                 ['Seto', 'Seto', 'City', 'Japan', 'Aichi', 'Seto', 1296, 38, 39, 'JP'],
                 ['Shinshiro', 'Shinshiro', 'City', 'Japan', 'Aichi', 'Shinshiro', 1297, 38, 39, 'JP'],
                 ['Shitara', 'Shitara', 'City', 'Japan', 'Aichi', 'Shitara', 1298, 38, 39, 'JP'],
                 ['Tahara', 'Tahara', 'City', 'Japan', 'Aichi', 'Tahara', 1299, 38, 39, 'JP'],
                 ['Takahama', 'Takahama', 'City', 'Japan', 'Aichi', 'Takahama', 1300, 38, 39, 'JP'],
                 ['Taketoyo', 'Taketoyo', 'City', 'Japan', 'Aichi', 'Taketoyo', 1301, 38, 39, 'JP'],
                 ['Tokai', 'Tokai', 'City', 'Japan', 'Aichi', 'Tokai', 1302, 38, 39, 'JP'],
                 ['Tokoname', 'Tokoname', 'City', 'Japan', 'Aichi', 'Tokoname', 1303, 38, 39, 'JP'],
                 ['Toyoake', 'Toyoake', 'City', 'Japan', 'Aichi', 'Toyoake', 1304, 38, 39, 'JP'],
                 ['Toyohashi', 'Toyohashi', 'City', 'Japan', 'Aichi', 'Toyohashi', 1305, 38, 39, 'JP'],
                 ['Toyokawa', 'Toyokawa', 'City', 'Japan', 'Aichi', 'Toyokawa', 1306, 38, 39, 'JP'],
                 ['Toyota', 'Toyota', 'City', 'Japan', 'Aichi', 'Toyota', 1307, 38, 39, 'JP'],
                 ['Tsushima', 'Tsushima', 'City', 'Japan', 'Aichi', 'Tsushima', 1308, 38, 39, 'JP'],
                 ['Akita', 'Akita', 'City', 'Japan', 'Akita', 'Akita', 1309, 38, 40, 'JP'],
                 ['Daisen', 'Daisen', 'City', 'Japan', 'Akita', 'Daisen', 1310, 38, 40, 'JP'],
                 ['Kazuno', 'Kazuno', 'City', 'Japan', 'Akita', 'Kazuno', 1311, 38, 40, 'JP'],
                 ['Noshiro', 'Noshiro', 'City', 'Japan', 'Akita', 'Noshiro', 1312, 38, 40, 'JP'],
                 ['Odate', 'Odate', 'City', 'Japan', 'Akita', 'Odate', 1313, 38, 40, 'JP'],
                 ['Oga', 'Oga', 'City', 'Japan', 'Akita', 'Oga', 1314, 38, 40, 'JP'],
                 ['Omagari', 'Omagari', 'City', 'Japan', 'Akita', 'Omagari', 1315, 38, 40, 'JP'],
                 ['Takanosu', 'Takanosu', 'City', 'Japan', 'Akita', 'Takanosu', 1316, 38, 40, 'JP'],
                 ['Yokote', 'Yokote', 'City', 'Japan', 'Akita', 'Yokote', 1317, 38, 40, 'JP'],
                 ['Yurihonjo', 'Yurihonjo', 'City', 'Japan', 'Akita', 'Yurihonjo', 1318, 38, 40, 'JP'],
                 ['Yuzawa', 'Yuzawa', 'City', 'Japan', 'Akita', 'Yuzawa', 1319, 38, 40, 'JP'],
                 ['Ajigasawa', 'Ajigasawa', 'City', 'Japan', 'Aomori', 'Ajigasawa', 1320, 38, 41, 'JP'],
                 ['Aomori', 'Aomori', 'City', 'Japan', 'Aomori', 'Aomori', 1321, 38, 41, 'JP'],
                 ['Goshogawara', 'Goshogawara', 'City', 'Japan', 'Aomori', 'Goshogawara', 1322, 38, 41, 'JP'],
                 ['Hachinohe', 'Hachinohe', 'City', 'Japan', 'Aomori', 'Hachinohe', 1323, 38, 41, 'JP'],
                 ['Hirosaki', 'Hirosaki', 'City', 'Japan', 'Aomori', 'Hirosaki', 1324, 38, 41, 'JP'],
                 ['Misawa', 'Misawa', 'City', 'Japan', 'Aomori', 'Misawa', 1325, 38, 41, 'JP'],
                 ['Mutsu', 'Mutsu', 'City', 'Japan', 'Aomori', 'Mutsu', 1326, 38, 41, 'JP'],
                 ['Noheji', 'Noheji', 'City', 'Japan', 'Aomori', 'Noheji', 1327, 38, 41, 'JP'],
                 ['Sannohe', 'Sannohe', 'City', 'Japan', 'Aomori', 'Sannohe', 1328, 38, 41, 'JP'],
                 ['Towada', 'Towada', 'City', 'Japan', 'Aomori', 'Towada', 1329, 38, 41, 'JP'],
                 ['Aizuwakamatsu', 'Aizuwakamatsu', 'City', 'Japan', 'Fukushima', 'Aizuwakamatsu', 1330, 38, 46, 'JP'],
                 ['Fukushima', 'Fukushima', 'City', 'Japan', 'Fukushima', 'Fukushima', 1331, 38, 46, 'JP'],
                 ['Ishikawa', 'Ishikawa', 'City', 'Japan', 'Fukushima', 'Ishikawa', 1332, 38, 46, 'JP'],
                 ['Iwaki', 'Iwaki', 'City', 'Japan', 'Fukushima', 'Iwaki', 1333, 38, 46, 'JP'],
                 ['Kitakata', 'Kitakata', 'City', 'Japan', 'Fukushima', 'Kitakata', 1334, 38, 46, 'JP'],
                 ['Koriyama', 'Koriyama', 'City', 'Japan', 'Fukushima', 'Koriyama', 1335, 38, 46, 'JP'],
                 ['Miharu', 'Miharu', 'City', 'Japan', 'Fukushima', 'Miharu', 1336, 38, 46, 'JP'],
                 ['Minamisoma', 'Minamisoma', 'City', 'Japan', 'Fukushima', 'Minamisoma', 1337, 38, 46, 'JP'],
                 ['Nihommatsu', 'Nihommatsu', 'City', 'Japan', 'Fukushima', 'Nihommatsu', 1338, 38, 46, 'JP'],
                 ['Shirakawa', 'Shirakawa', 'City', 'Japan', 'Fukushima', 'Shirakawa', 1339, 38, 46, 'JP'],
                 ['Sukagawa', 'Sukagawa', 'City', 'Japan', 'Fukushima', 'Sukagawa', 1340, 38, 46, 'JP'],
                 ['Tajima', 'Tajima', 'City', 'Japan', 'Fukushima', 'Tajima', 1341, 38, 46, 'JP'],
                 ['Abashiri', 'Abashiri', 'City', 'Japan', 'Hokkaido', 'Abashiri', 1342, 38, 50, 'JP'],
                 ['Akkeshi', 'Akkeshi', 'City', 'Japan', 'Hokkaido', 'Akkeshi', 1343, 38, 50, 'JP'],
                 ['Asahikawa', 'Asahikawa', 'City', 'Japan', 'Hokkaido', 'Asahikawa', 1344, 38, 50, 'JP'],
                 ['Ashibetsu', 'Ashibetsu', 'City', 'Japan', 'Hokkaido', 'Ashibetsu', 1345, 38, 50, 'JP'],
                 ['Ashoro', 'Ashoro', 'City', 'Japan', 'Hokkaido', 'Ashoro', 1346, 38, 50, 'JP'],
                 ['Bibai', 'Bibai', 'City', 'Japan', 'Hokkaido', 'Bibai', 1347, 38, 50, 'JP'],
                 ['Bifuka', 'Bifuka', 'City', 'Japan', 'Hokkaido', 'Bifuka', 1348, 38, 50, 'JP'],
                 ['Bihoro', 'Bihoro', 'City', 'Japan', 'Hokkaido', 'Bihoro', 1349, 38, 50, 'JP'],
                 ['Chitose', 'Chitose', 'City', 'Japan', 'Hokkaido', 'Chitose', 1350, 38, 50, 'JP'],
                 ['Date', 'Date', 'City', 'Japan', 'Hokkaido', 'Date', 1351, 38, 50, 'JP'],
                 ['Ebetsu', 'Ebetsu', 'City', 'Japan', 'Hokkaido', 'Ebetsu', 1352, 38, 50, 'JP'],
                 ['Engaru', 'Engaru', 'City', 'Japan', 'Hokkaido', 'Engaru', 1353, 38, 50, 'JP'],
                 ['Eniwa', 'Eniwa', 'City', 'Japan', 'Hokkaido', 'Eniwa', 1354, 38, 50, 'JP'],
                 ['Erimo', 'Erimo', 'City', 'Japan', 'Hokkaido', 'Erimo', 1355, 38, 50, 'JP'],
                 ['Esashi', 'Esashi', 'City', 'Japan', 'Hokkaido', 'Esashi', 1356, 38, 50, 'JP'],
                 ['Fukagawa', 'Fukagawa', 'City', 'Japan', 'Hokkaido', 'Fukagawa', 1357, 38, 50, 'JP'],
                 ['Furano', 'Furano', 'City', 'Japan', 'Hokkaido', 'Furano', 1358, 38, 50, 'JP'],
                 ['Furencho', 'Furencho', 'Neighborhood', 'Japan', 'Hokkaido', 'Furencho', 1359, 38, 50, 'JP'],
                 ['Haboro', 'Haboro', 'City', 'Japan', 'Hokkaido', 'Haboro', 1360, 38, 50, 'JP'],
                 ['Hakodate', 'Hakodate', 'City', 'Japan', 'Hokkaido', 'Hakodate', 1361, 38, 50, 'JP'],
                 ['Hiroo', 'Hiroo', 'City', 'Japan', 'Hokkaido', 'Hiroo', 1362, 38, 50, 'JP'],
                 ['Ishikari', 'Ishikari', 'City', 'Japan', 'Hokkaido', 'Ishikari', 1363, 38, 50, 'JP'],
                 ['Iwamizawa', 'Iwamizawa', 'City', 'Japan', 'Hokkaido', 'Iwamizawa', 1364, 38, 50, 'JP'],
                 ['Iwanai', 'Iwanai', 'City', 'Japan', 'Hokkaido', 'Iwanai', 1365, 38, 50, 'JP'],
                 ['Kamoenai', 'Kamoenai', 'City', 'Japan', 'Hokkaido', 'Kamoenai', 1366, 38, 50, 'JP'],
                 ['Kikonai', 'Kikonai', 'City', 'Japan', 'Hokkaido', 'Kikonai', 1367, 38, 50, 'JP'],
                 ['Kitami', 'Kitami', 'City', 'Japan', 'Hokkaido', 'Kitami', 1368, 38, 50, 'JP'],
                 ['Kiyota Ward', 'Kiyota Ward', 'Neighborhood', 'Japan', 'Hokkaido', 'Kiyota Ward', 1369, 38, 50, 'JP'],
                 ['Kuriyama', 'Kuriyama', 'City', 'Japan', 'Hokkaido', 'Kuriyama', 1370, 38, 50, 'JP'],
                 ['Kuromatsunai', 'Kuromatsunai', 'City', 'Japan', 'Hokkaido', 'Kuromatsunai', 1371, 38, 50, 'JP'],
                 ['Kushiro', 'Kushiro', 'City', 'Japan', 'Hokkaido', 'Kushiro', 1372, 38, 50, 'JP'],
                 ['Kutchan', 'Kutchan', 'City', 'Japan', 'Hokkaido', 'Kutchan', 1373, 38, 50, 'JP'],
                 ['Matsumae', 'Matsumae', 'City', 'Japan', 'Hokkaido', 'Matsumae', 1374, 38, 50, 'JP'],
                 ['Mombetsu', 'Mombetsu', 'City', 'Japan', 'Hokkaido', 'Mombetsu', 1375, 38, 50, 'JP'],
                 ['Mori', 'Mori', 'City', 'Japan', 'Hokkaido', 'Mori', 1376, 38, 50, 'JP'],
                 ['Moseushi', 'Moseushi', 'City', 'Japan', 'Hokkaido', 'Moseushi', 1377, 38, 50, 'JP'],
                 ['Muroran', 'Muroran', 'City', 'Japan', 'Hokkaido', 'Muroran', 1378, 38, 50, 'JP'],
                 ['Naganuma', 'Naganuma', 'City', 'Japan', 'Hokkaido', 'Naganuma', 1379, 38, 50, 'JP'],
                 ['Nakashibetsu', 'Nakashibetsu', 'City', 'Japan', 'Hokkaido', 'Nakashibetsu', 1380, 38, 50, 'JP'],
                 ['Namporo', 'Namporo', 'City', 'Japan', 'Hokkaido', 'Namporo', 1381, 38, 50, 'JP'],
                 ['Nanae', 'Nanae', 'City', 'Japan', 'Hokkaido', 'Nanae', 1382, 38, 50, 'JP'],
                 ['Nayoro', 'Nayoro', 'City', 'Japan', 'Hokkaido', 'Nayoro', 1383, 38, 50, 'JP'],
                 ['Nemuro', 'Nemuro', 'City', 'Japan', 'Hokkaido', 'Nemuro', 1384, 38, 50, 'JP'],
                 ['Niikappu', 'Niikappu', 'City', 'Japan', 'Hokkaido', 'Niikappu', 1385, 38, 50, 'JP'],
                 ['Noboribetsu', 'Noboribetsu', 'City', 'Japan', 'Hokkaido', 'Noboribetsu', 1386, 38, 50, 'JP'],
                 ['Numata', 'Numata', 'City', 'Japan', 'Hokkaido', 'Numata', 1387, 38, 50, 'JP'],
                 ['Obihiro', 'Obihiro', 'City', 'Japan', 'Hokkaido', 'Obihiro', 1388, 38, 50, 'JP'],
                 ['Oshamambe', 'Oshamambe', 'City', 'Japan', 'Hokkaido', 'Oshamambe', 1389, 38, 50, 'JP'],
                 ['Otaru', 'Otaru', 'City', 'Japan', 'Hokkaido', 'Otaru', 1390, 38, 50, 'JP'],
                 ['Rikubetsu', 'Rikubetsu', 'City', 'Japan', 'Hokkaido', 'Rikubetsu', 1391, 38, 50, 'JP'],
                 ['Rumoi', 'Rumoi', 'City', 'Japan', 'Hokkaido', 'Rumoi', 1392, 38, 50, 'JP'],
                 ['Sapporo', 'Sapporo', 'City', 'Japan', 'Hokkaido', 'Sapporo', 1393, 38, 50, 'JP'],
                 ['Sarufutsu', 'Sarufutsu', 'City', 'Japan', 'Hokkaido', 'Sarufutsu', 1394, 38, 50, 'JP'],
                 ['Setana', 'Setana', 'City', 'Japan', 'Hokkaido', 'Setana', 1395, 38, 50, 'JP'],
                 ['Shari', 'Shari', 'City', 'Japan', 'Hokkaido', 'Shari', 1396, 38, 50, 'JP'],
                 ['Shibecha', 'Shibecha', 'City', 'Japan', 'Hokkaido', 'Shibecha', 1397, 38, 50, 'JP'],
                 ['Shibetsu', 'Shibetsu', 'City', 'Japan', 'Hokkaido', 'Shibetsu', 1398, 38, 50, 'JP'],
                 ['Shikaoi', 'Shikaoi', 'City', 'Japan', 'Hokkaido', 'Shikaoi', 1399, 38, 50, 'JP'],
                 ['Shimizu', 'Shimizu', 'City', 'Japan', 'Hokkaido', 'Shimizu', 1400, 38, 50, 'JP'],
                 ['Shiranuka', 'Shiranuka', 'City', 'Japan', 'Hokkaido', 'Shiranuka', 1401, 38, 50, 'JP'],
                 ['Shiraoi', 'Shiraoi', 'City', 'Japan', 'Hokkaido', 'Shiraoi', 1402, 38, 50, 'JP'],
                 ['Sunagawa', 'Sunagawa', 'City', 'Japan', 'Hokkaido', 'Sunagawa', 1403, 38, 50, 'JP'],
                 ['Suttsu', 'Suttsu', 'City', 'Japan', 'Hokkaido', 'Suttsu', 1404, 38, 50, 'JP'],
                 ['Takikawa', 'Takikawa', 'City', 'Japan', 'Hokkaido', 'Takikawa', 1405, 38, 50, 'JP'],
                 ['Teshikaga', 'Teshikaga', 'City', 'Japan', 'Hokkaido', 'Teshikaga', 1406, 38, 50, 'JP'],
                 ['Teshio', 'Teshio', 'City', 'Japan', 'Hokkaido', 'Teshio', 1407, 38, 50, 'JP'],
                 ['Tobetsu', 'Tobetsu', 'City', 'Japan', 'Hokkaido', 'Tobetsu', 1408, 38, 50, 'JP'],
                 ['Tomakomai', 'Tomakomai', 'City', 'Japan', 'Hokkaido', 'Tomakomai', 1409, 38, 50, 'JP'],
                 ['Tsukigata', 'Tsukigata', 'City', 'Japan', 'Hokkaido', 'Tsukigata', 1410, 38, 50, 'JP'],
                 ['Urakawa', 'Urakawa', 'City', 'Japan', 'Hokkaido', 'Urakawa', 1411, 38, 50, 'JP'],
                 ['Wakkanai', 'Wakkanai', 'City', 'Japan', 'Hokkaido', 'Wakkanai', 1412, 38, 50, 'JP'],
                 ['Yakumo', 'Yakumo', 'City', 'Japan', 'Hokkaido', 'Yakumo', 1413, 38, 50, 'JP'],
                 ['Yoichi', 'Yoichi', 'City', 'Japan', 'Hokkaido', 'Yoichi', 1414, 38, 50, 'JP'],
                 ['Yubari', 'Yubari', 'City', 'Japan', 'Hokkaido', 'Yubari', 1415, 38, 50, 'JP'],
                 ['Hanamaki', 'Hanamaki', 'City', 'Japan', 'Iwate', 'Hanamaki', 1416, 38, 54, 'JP'],
                 ['Hiraizumi', 'Hiraizumi', 'City', 'Japan', 'Iwate', 'Hiraizumi', 1417, 38, 54, 'JP'],
                 ['Ichinoseki', 'Ichinoseki', 'City', 'Japan', 'Iwate', 'Ichinoseki', 1418, 38, 54, 'JP'],
                 ['Iwaizumi', 'Iwaizumi', 'City', 'Japan', 'Iwate', 'Iwaizumi', 1419, 38, 54, 'JP'],
                 ['Kamaishi', 'Kamaishi', 'City', 'Japan', 'Iwate', 'Kamaishi', 1420, 38, 54, 'JP'],
                 ['Kitakami', 'Kitakami', 'City', 'Japan', 'Iwate', 'Kitakami', 1421, 38, 54, 'JP'],
                 ['Kuji', 'Kuji', 'City', 'Japan', 'Iwate', 'Kuji', 1422, 38, 54, 'JP'],
                 ['Miyako', 'Miyako', 'City', 'Japan', 'Iwate', 'Miyako', 1423, 38, 54, 'JP'],
                 ['Morioka', 'Morioka', 'City', 'Japan', 'Iwate', 'Morioka', 1424, 38, 54, 'JP'],
                 ['Ninohe', 'Ninohe', 'City', 'Japan', 'Iwate', 'Ninohe', 1425, 38, 54, 'JP'],
                 ['Ofunato', 'Ofunato', 'City', 'Japan', 'Iwate', 'Ofunato', 1426, 38, 54, 'JP'],
                 ['Oshu', 'Oshu', 'City', 'Japan', 'Iwate', 'Oshu', 1427, 38, 54, 'JP'],
                 ['Tono', 'Tono', 'City', 'Japan', 'Iwate', 'Tono', 1428, 38, 54, 'JP'],
                 ['Fukuchiyama', 'Fukuchiyama', 'City', 'Japan', 'Kyoto', 'Fukuchiyama', 1429, 38, 60, 'JP'],
                 ['Joyo', 'Joyo', 'City', 'Japan', 'Kyoto', 'Joyo', 1430, 38, 60, 'JP'],
                 ['Kameoka', 'Kameoka', 'City', 'Japan', 'Kyoto', 'Kameoka', 1431, 38, 60, 'JP'],
                 ['Kizugawa', 'Kizugawa', 'City', 'Japan', 'Kyoto', 'Kizugawa', 1432, 38, 60, 'JP'],
                 ['Kyotamba', 'Kyotamba', 'City', 'Japan', 'Kyoto', 'Kyotamba', 1433, 38, 60, 'JP'],
                 ['Kyotanabe', 'Kyotanabe', 'City', 'Japan', 'Kyoto', 'Kyotanabe', 1434, 38, 60, 'JP'],
                 ['Kyotango', 'Kyotango', 'City', 'Japan', 'Kyoto', 'Kyotango', 1435, 38, 60, 'JP'],
                 ['Kyoto', 'Kyoto', 'City', 'Japan', 'Kyoto', 'Kyoto', 1436, 38, 60, 'JP'],
                 ['Maizuru', 'Maizuru', 'City', 'Japan', 'Kyoto', 'Maizuru', 1437, 38, 60, 'JP'],
                 ['Miyazu', 'Miyazu', 'City', 'Japan', 'Kyoto', 'Miyazu', 1438, 38, 60, 'JP'],
                 ['Muko', 'Muko', 'City', 'Japan', 'Kyoto', 'Muko', 1439, 38, 60, 'JP'],
                 ['Nagaokakyo', 'Nagaokakyo', 'City', 'Japan', 'Kyoto', 'Nagaokakyo', 1440, 38, 60, 'JP'],
                 ['Nantan', 'Nantan', 'City', 'Japan', 'Kyoto', 'Nantan', 1441, 38, 60, 'JP'],
                 ['Seika', 'Seika', 'City', 'Japan', 'Kyoto', 'Seika', 1442, 38, 60, 'JP'],
                 ['Sonobecho Oyama Higashimachi', 'Sonobecho Oyama Higashimachi', 'Neighborhood', 'Japan', 'Kyoto',
                  'Sonobecho Oyama Higashimachi', 1443, 38, 60, 'JP'],
                 ['Uji', 'Uji', 'City', 'Japan', 'Kyoto', 'Uji', 1444, 38, 60, 'JP'],
                 ['Ukyo Ward', 'Ukyo Ward', 'Neighborhood', 'Japan', 'Kyoto', 'Ukyo Ward', 1445, 38, 60, 'JP'],
                 ['Yagicho Yagi', 'Yagicho Yagi', 'Neighborhood', 'Japan', 'Kyoto', 'Yagicho Yagi', 1446, 38, 60, 'JP'],
                 ['Yawata', 'Yawata', 'City', 'Japan', 'Kyoto', 'Yawata', 1447, 38, 60, 'JP'],
                 ['Yosano', 'Yosano', 'City', 'Japan', 'Kyoto', 'Yosano', 1448, 38, 60, 'JP'],
                 ['Ishinomaki', 'Ishinomaki', 'City', 'Japan', 'Miyagi', 'Ishinomaki', 1449, 38, 62, 'JP'],
                 ['Iwanuma', 'Iwanuma', 'City', 'Japan', 'Miyagi', 'Iwanuma', 1450, 38, 62, 'JP'],
                 ['Kesennuma', 'Kesennuma', 'City', 'Japan', 'Miyagi', 'Kesennuma', 1451, 38, 62, 'JP'],
                 ['Matsushima', 'Matsushima', 'City', 'Japan', 'Miyagi', 'Matsushima', 1452, 38, 62, 'JP'],
                 ['Osaki', 'Osaki', 'City', 'Japan', 'Miyagi', 'Osaki', 1453, 38, 62, 'JP'],
                 ['Sendai', 'Sendai', 'City', 'Japan', 'Miyagi', 'Sendai', 1454, 38, 62, 'JP'],
                 ['Shiroishi', 'Shiroishi', 'City', 'Japan', 'Miyagi', 'Shiroishi', 1455, 38, 62, 'JP'],
                 ['Tagajo', 'Tagajo', 'City', 'Japan', 'Miyagi', 'Tagajo', 1456, 38, 62, 'JP'],
                 ['Tome', 'Tome', 'City', 'Japan', 'Miyagi', 'Tome', 1457, 38, 62, 'JP'],
                 ['Chihayaakasaka', 'Chihayaakasaka', 'City', 'Japan', 'Osaka', 'Chihayaakasaka', 1458, 38, 71, 'JP'],
                 ['Daito', 'Daito', 'City', 'Japan', 'Osaka', 'Daito', 1459, 38, 71, 'JP'],
                 ['Habikino', 'Habikino', 'City', 'Japan', 'Osaka', 'Habikino', 1460, 38, 71, 'JP'],
                 ['Habucho', 'Habucho', 'Neighborhood', 'Japan', 'Osaka', 'Habucho', 1461, 38, 71, 'JP'],
                 ['Hannan', 'Hannan', 'City', 'Japan', 'Osaka', 'Hannan', 1462, 38, 71, 'JP'],
                 ['Higashiosaka', 'Higashiosaka', 'City', 'Japan', 'Osaka', 'Higashiosaka', 1463, 38, 71, 'JP'],
                 ['Hirakata', 'Hirakata', 'City', 'Japan', 'Osaka', 'Hirakata', 1464, 38, 71, 'JP'],
                 ['Hirano Ward', 'Hirano Ward', 'Neighborhood', 'Japan', 'Osaka', 'Hirano Ward', 1465, 38, 71, 'JP'],
                 ['Ibaraki', 'Ibaraki', 'City', 'Japan', 'Osaka', 'Ibaraki', 1466, 38, 71, 'JP'],
                 ['Ikeda', 'Ikeda', 'City', 'Japan', 'Osaka', 'Ikeda', 1467, 38, 71, 'JP'],
                 ['Izumi', 'Izumi', 'City', 'Japan', 'Osaka', 'Izumi', 1468, 38, 71, 'JP'],
                 ['Izumiotsu', 'Izumiotsu', 'City', 'Japan', 'Osaka', 'Izumiotsu', 1469, 38, 71, 'JP'],
                 ['Izumisano', 'Izumisano', 'City', 'Japan', 'Osaka', 'Izumisano', 1470, 38, 71, 'JP'],
                 ['Kadoma', 'Kadoma', 'City', 'Japan', 'Osaka', 'Kadoma', 1471, 38, 71, 'JP'],
                 ['Kaizuka', 'Kaizuka', 'City', 'Japan', 'Osaka', 'Kaizuka', 1472, 38, 71, 'JP'],
                 ['Katano', 'Katano', 'City', 'Japan', 'Osaka', 'Katano', 1473, 38, 71, 'JP'],
                 ['Kawachinagano', 'Kawachinagano', 'City', 'Japan', 'Osaka', 'Kawachinagano', 1474, 38, 71, 'JP'],
                 ['Kishiwada', 'Kishiwada', 'City', 'Japan', 'Osaka', 'Kishiwada', 1475, 38, 71, 'JP'],
                 ['Konohana Ward', 'Konohana Ward', 'Neighborhood', 'Japan', 'Osaka', 'Konohana Ward', 1476, 38, 71,
                  'JP'],
                 ['Matsubara', 'Matsubara', 'City', 'Japan', 'Osaka', 'Matsubara', 1477, 38, 71, 'JP'],
                 ['Minoo', 'Minoo', 'City', 'Japan', 'Osaka', 'Minoo', 1478, 38, 71, 'JP'],
                 ['Moriguchi', 'Moriguchi', 'City', 'Japan', 'Osaka', 'Moriguchi', 1479, 38, 71, 'JP'],
                 ['Naniwa Ward', 'Naniwa Ward', 'Neighborhood', 'Japan', 'Osaka', 'Naniwa Ward', 1480, 38, 71, 'JP'],
                 ['Neyagawa', 'Neyagawa', 'City', 'Japan', 'Osaka', 'Neyagawa', 1481, 38, 71, 'JP'],
                 ['Nishinari Ward', 'Nishinari Ward', 'Neighborhood', 'Japan', 'Osaka', 'Nishinari Ward', 1482, 38, 71,
                  'JP'],
                 ['Osaka', 'Osaka', 'City', 'Japan', 'Osaka', 'Osaka', 1483, 38, 71, 'JP'],
                 ['Osakasayama', 'Osakasayama', 'City', 'Japan', 'Osaka', 'Osakasayama', 1484, 38, 71, 'JP'],
                 ['Sakai', 'Sakai', 'City', 'Japan', 'Osaka', 'Sakai', 1485, 38, 71, 'JP'],
                 ['Suita', 'Suita', 'City', 'Japan', 'Osaka', 'Suita', 1486, 38, 71, 'JP'],
                 ['Tajiri', 'Tajiri', 'City', 'Japan', 'Osaka', 'Tajiri', 1487, 38, 71, 'JP'],
                 ['Takatsuki ', 'Takatsuki ', 'City', 'Japan', 'Osaka', 'Takatsuki', 1488, 38, 71, 'JP'],
                 ['Tondabayashi', 'Tondabayashi', 'City', 'Japan', 'Osaka', 'Tondabayashi', 1489, 38, 71, 'JP'],
                 ['Toyonaka', 'Toyonaka', 'City', 'Japan', 'Osaka', 'Toyonaka', 1490, 38, 71, 'JP'],
                 ['Yao', 'Yao', 'City', 'Japan', 'Osaka', 'Yao', 1491, 38, 71, 'JP'],
                 ['Yodogawa Ward', 'Yodogawa Ward', 'Neighborhood', 'Japan', 'Osaka', 'Yodogawa Ward', 1492, 38, 71,
                  'JP'],
                 ['Adachi', 'Adachi', 'City', 'Japan', 'Tokyo', 'Adachi', 1493, 38, 79, 'JP'],
                 ['Akiruno', 'Akiruno', 'City', 'Japan', 'Tokyo', 'Akiruno', 1494, 38, 79, 'JP'],
                 ['Akishima', 'Akishima', 'City', 'Japan', 'Tokyo', 'Akishima', 1495, 38, 79, 'JP'],
                 ['Arakawa', 'Arakawa', 'City', 'Japan', 'Tokyo', 'Arakawa', 1496, 38, 79, 'JP'],
                 ['Bunkyo', 'Bunkyo', 'City', 'Japan', 'Tokyo', 'Bunkyo', 1497, 38, 79, 'JP'],
                 ['Chiyoda', 'Chiyoda', 'City', 'Japan', 'Tokyo', 'Chiyoda', 1498, 38, 79, 'JP'],
                 ['Chofu', 'Chofu', 'City', 'Japan', 'Tokyo', 'Chofu', 1499, 38, 79, 'JP'],
                 ['Chuo', 'Chuo', 'City', 'Japan', 'Tokyo', 'Chuo', 1500, 38, 79, 'JP'],
                 ['Edogawa', 'Edogawa', 'City', 'Japan', 'Tokyo', 'Edogawa', 1501, 38, 79, 'JP'],
                 ['Fuchu', 'Fuchu', 'City', 'Japan', 'Tokyo', 'Fuchu', 1502, 38, 79, 'JP'],
                 ['Fussa', 'Fussa', 'City', 'Japan', 'Tokyo', 'Fussa', 1503, 38, 79, 'JP'],
                 ['Hachioji', 'Hachioji', 'City', 'Japan', 'Tokyo', 'Hachioji', 1504, 38, 79, 'JP'],
                 ['Hamura', 'Hamura', 'City', 'Japan', 'Tokyo', 'Hamura', 1505, 38, 79, 'JP'],
                 ['Higashikurume', 'Higashikurume', 'City', 'Japan', 'Tokyo', 'Higashikurume', 1506, 38, 79, 'JP'],
                 ['Higashimurayama', 'Higashimurayama', 'City', 'Japan', 'Tokyo', 'Higashimurayama', 1507, 38, 79,
                  'JP'],
                 ['Higashiyamato', 'Higashiyamato', 'City', 'Japan', 'Tokyo', 'Higashiyamato', 1508, 38, 79, 'JP'],
                 ['Hino', 'Hino', 'City', 'Japan', 'Tokyo', 'Hino', 1509, 38, 79, 'JP'],
                 ['Inagi', 'Inagi', 'City', 'Japan', 'Tokyo', 'Inagi', 1510, 38, 79, 'JP'],
                 ['Itabashi', 'Itabashi', 'City', 'Japan', 'Tokyo', 'Itabashi', 1511, 38, 79, 'JP'],
                 ['Katsushika', 'Katsushika', 'City', 'Japan', 'Tokyo', 'Katsushika', 1512, 38, 79, 'JP'],
                 ['Kita', 'Kita', 'City', 'Japan', 'Tokyo', 'Kita', 1513, 38, 79, 'JP'],
                 ['Kiyose', 'Kiyose', 'City', 'Japan', 'Tokyo', 'Kiyose', 1514, 38, 79, 'JP'],
                 ['Kodaira', 'Kodaira', 'City', 'Japan', 'Tokyo', 'Kodaira', 1515, 38, 79, 'JP'],
                 ['Koganei', 'Koganei', 'City', 'Japan', 'Tokyo', 'Koganei', 1516, 38, 79, 'JP'],
                 ['Kokubunji', 'Kokubunji', 'City', 'Japan', 'Tokyo', 'Kokubunji', 1517, 38, 79, 'JP'],
                 ['Komae', 'Komae', 'City', 'Japan', 'Tokyo', 'Komae', 1518, 38, 79, 'JP'],
                 ['Koto', 'Koto', 'City', 'Japan', 'Tokyo', 'Koto', 1519, 38, 79, 'JP'],
                 ['Kunitachi', 'Kunitachi', 'City', 'Japan', 'Tokyo', 'Kunitachi', 1520, 38, 79, 'JP'],
                 ['Machida', 'Machida', 'City', 'Japan', 'Tokyo', 'Machida', 1521, 38, 79, 'JP'],
                 ['Meguro', 'Meguro', 'City', 'Japan', 'Tokyo', 'Meguro', 1522, 38, 79, 'JP'],
                 ['Minato', 'Minato', 'City', 'Japan', 'Tokyo', 'Minato', 1523, 38, 79, 'JP'],
                 ['Mitaka', 'Mitaka', 'City', 'Japan', 'Tokyo', 'Mitaka', 1524, 38, 79, 'JP'],
                 ['Musashimurayama', 'Musashimurayama', 'City', 'Japan', 'Tokyo', 'Musashimurayama', 1525, 38, 79,
                  'JP'],
                 ['Musashino', 'Musashino', 'City', 'Japan', 'Tokyo', 'Musashino', 1526, 38, 79, 'JP'],
                 ['Nakano', 'Nakano', 'City', 'Japan', 'Tokyo', 'Nakano', 1527, 38, 79, 'JP'],
                 ['Nerima', 'Nerima', 'City', 'Japan', 'Tokyo', 'Nerima', 1528, 38, 79, 'JP'],
                 ['Nishitokyo', 'Nishitokyo', 'City', 'Japan', 'Tokyo', 'Nishitokyo', 1529, 38, 79, 'JP'],
                 ['Ome', 'Ome', 'City', 'Japan', 'Tokyo', 'Ome', 1530, 38, 79, 'JP'],
                 ['Ota', 'Ota', 'City', 'Japan', 'Tokyo', 'Ota', 1531, 38, 79, 'JP'],
                 ['Setagaya', 'Setagaya', 'City', 'Japan', 'Tokyo', 'Setagaya', 1532, 38, 79, 'JP'],
                 ['Shibuya', 'Shibuya', 'City', 'Japan', 'Tokyo', 'Shibuya', 1533, 38, 79, 'JP'],
                 ['Shinagawa', 'Shinagawa', 'City', 'Japan', 'Tokyo', 'Shinagawa', 1534, 38, 79, 'JP'],
                 ['Shinjuku', 'Shinjuku', 'City', 'Japan', 'Tokyo', 'Shinjuku', 1535, 38, 79, 'JP'],
                 ['Suginami', 'Suginami', 'City', 'Japan', 'Tokyo', 'Suginami', 1536, 38, 79, 'JP'],
                 ['Sumida', 'Sumida', 'City', 'Japan', 'Tokyo', 'Sumida', 1537, 38, 79, 'JP'],
                 ['Tachikawa', 'Tachikawa', 'City', 'Japan', 'Tokyo', 'Tachikawa', 1538, 38, 79, 'JP'],
                 ['Taito', 'Taito', 'City', 'Japan', 'Tokyo', 'Taito', 1539, 38, 79, 'JP'],
                 ['Tama', 'Tama', 'City', 'Japan', 'Tokyo', 'Tama', 1540, 38, 79, 'JP'],
                 ['Tokyo', 'Tokyo', 'City', 'Japan', 'Tokyo', 'Tokyo', 1541, 38, 79, 'JP'],
                 ['Toshima', 'Toshima', 'City', 'Japan', 'Tokyo', 'Toshima', 1542, 38, 79, 'JP'],
                 ['Murayama', 'Murayama', 'City', 'Japan', 'Yamagata', 'Murayama', 1543, 38, 83, 'JP'],
                 ['Nagai', 'Nagai', 'City', 'Japan', 'Yamagata', 'Nagai', 1544, 38, 83, 'JP'],
                 ['Sagae', 'Sagae', 'City', 'Japan', 'Yamagata', 'Sagae', 1545, 38, 83, 'JP'],
                 ['Sakata', 'Sakata', 'City', 'Japan', 'Yamagata', 'Sakata', 1546, 38, 83, 'JP'],
                 ['Shinjo', 'Shinjo', 'City', 'Japan', 'Yamagata', 'Shinjo', 1547, 38, 83, 'JP'],
                 ['Tsuruoka', 'Tsuruoka', 'City', 'Japan', 'Yamagata', 'Tsuruoka', 1548, 38, 83, 'JP'],
                 ['Yamagata', 'Yamagata', 'City', 'Japan', 'Yamagata', 'Yamagata', 1549, 38, 83, 'JP'],
                 ['Yonezawa', 'Yonezawa', 'City', 'Japan', 'Yamagata', 'Yonezawa', 1550, 38, 83, 'JP']]


class TestJPVponGeoService(TestCase):

    def test_match_case1(self):
        service = JPVponGeoService()
        google_geo_dict = {
            1009023: GoogleGeoDTO(1009023, 'Abashiri', ['Japan', 'Hokkaido', 'Abashiri'], '20624,9073781,2392', '',
                                  "JP", 'City')
        }
        result = service.match(google_geo_dict, vpon_geo_list)
        self.assertEqual(result[0].criteria_id, 1009023)
        self.assertEqual(result[0].tier1, 38)
        self.assertEqual(result[0].tier2, 50)
        self.assertEqual(result[0].tier3, 1342)

    def test_match_case2(self):
        service = JPVponGeoService()
        google_geo_dict = {
            1009161: GoogleGeoDTO(1009161, 'Daigo', ['Japan', 'Ibaraki', 'Daigo'], '20624,9073781,2392', '',
                                  "JP", 'City')
        }
        result = service.match(google_geo_dict, vpon_geo_list)

        self.assertEqual(result[0].criteria_id, 1009161)
        self.assertEqual(result[0].tier1, 38)
        self.assertEqual(result[0].tier2, 52)
        self.assertEqual(result[0].tier3, None)

    def test_match_case3(self):
        service = JPVponGeoService()
        google_geo_dict = {
            9053407: GoogleGeoDTO(9053407, 'Usa', ['Japan', 'Oita', 'Usa'], '20624,9073781,2392', '',
                                  "JP", 'City')
        }
        result = service.match(google_geo_dict, vpon_geo_list)

        self.assertEqual(result[0].criteria_id, 9053407)
        self.assertEqual(result[0].tier1, 38)
        self.assertEqual(result[0].tier2, 68)
        self.assertEqual(result[0].tier3, None)

    def test_match_case4(self):
        service = JPVponGeoService()
        google_geo_dict = {
            9073781: GoogleGeoDTO(9073781, 'JP_OTHER', ['Japan', 'JP_OTHER'], '20624,9073781,2392', '',
                                  "JP", 'City')
        }
        result = service.match(google_geo_dict, vpon_geo_list)

        self.assertEqual(result[0].criteria_id, 9073781)
        self.assertEqual(result[0].tier1, 38)
        self.assertEqual(result[0].tier2, None)
        self.assertEqual(result[0].tier3, None)

    def test_match_case5(self):
        service = JPVponGeoService()
        google_geo_dict = {
            9053411: GoogleGeoDTO(9053411, 'Yabu', ['Japan', 'Hyogo', 'Yabu'], '20624,9073781,2392', '',
                                  "JP", 'City')
        }
        result = service.match(google_geo_dict, vpon_geo_list)

        self.assertEqual(result[0].criteria_id, 9053411)
        self.assertEqual(result[0].tier1, 38)
        self.assertEqual(result[0].tier2, 51)
        self.assertEqual(result[0].tier3, None)

    def test_match_case6(self):
        service = JPVponGeoService()
        google_geo_dict = {
            9053263: GoogleGeoDTO(9053263, 'Chuo', ['Japan', 'Yamanashi', 'Chuo'], '20624,9073781,2392', '',
                                  "JP", 'City')
        }
        result = service.match(google_geo_dict, vpon_geo_list)

        self.assertEqual(result[0].criteria_id, 9053263)
        self.assertEqual(result[0].tier1, 38)
        self.assertEqual(result[0].tier2, 85)
        self.assertEqual(result[0].tier3, None)

    def test_match_case7(self):
        service = JPVponGeoService()
        google_geo_dict = {
            9053291: GoogleGeoDTO(9053291, 'Ikeda', ['Japan', 'Gifu', 'Ikeda'], '20624,9073781,2392', '',
                                  "JP", 'City')
        }
        result = service.match(google_geo_dict, vpon_geo_list)

        self.assertEqual(result[0].criteria_id, 9053291)
        self.assertEqual(result[0].tier1, 38)
        self.assertEqual(result[0].tier2, 47)
        self.assertEqual(result[0].tier3, None)

    def test_match_case8(self):
        service = JPVponGeoService()
        google_geo_dict = {
            9053317: GoogleGeoDTO(9053317, 'Konan', ['Japan', 'Shiga', 'Konan'], '20624,9073781,2392', '',
                                  "JP", 'City')
        }
        result = service.match(google_geo_dict, vpon_geo_list)

        self.assertEqual(result[0].criteria_id, 9053317)
        self.assertEqual(result[0].tier1, 38)
        self.assertEqual(result[0].tier2, 74)
        self.assertEqual(result[0].tier3, None)
