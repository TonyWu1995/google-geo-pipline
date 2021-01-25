# ip = '10.0.1.3'
# port = 21
# username = 'adnext'
# password = '28892170'


class FTPConfig:

    def __init__(self, ip: str, username: str, password: str):
        self.__ip = ip
        self.__username = username
        self.__password = password

    @property
    def ip(self):
        return self.__ip

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @staticmethod
    def build(config: dict):
        return FTPConfig(config['ip'], config['username'], config['password'])
