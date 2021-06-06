import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

USER = config["POSTGRES"]["USER"]
NAME = config["POSTGRES"]["NAME"]
PASSWORD = config["POSTGRES"]["PASSWORD"]
HOST = config["POSTGRES"]["HOST"]
PORT = config["POSTGRES"]["PORT"]
