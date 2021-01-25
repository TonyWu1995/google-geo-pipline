import logging
from ftplib import FTP

from config.ftp_config import FTPConfig

log = logging.getLogger(__name__)


class FTPService:

    def __init__(self, ftp_config: FTPConfig):
        self.__ftp = FTP(ftp_config.ip)
        self.__ftp.login(ftp_config.username, ftp_config.password)

    def upload_file(self, file_name, file):
        bufsize = 1024
        try:
            self.__ftp.storbinary('STOR ' + file_name, file, bufsize)
        except Exception as e:
            log.error("upload_file() error {}".format(e))
