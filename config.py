from distutils.command.config import config


class DevelopmentConfig():
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'V10:L1n3s?'
    MYSQL_DB = 'a2censo'

config ={
    'development' : DevelopmentConfig
}