#-*- coding: UTF-8 -*-
__author__ = 'minhuaxu'
import configparser
from wpyscripts.common.adb_process import excute_adb

class Account(object):
    QQNAME="" #QQ acount
    QQPWD="" #QQ password
    WECHATNAME="" #wechat account
    WECHATPWD="" #wechat password

class readConfig():
    def getValues(self, value):
        config = configparser.ConfigParser()
        config.read_file(open("config.ini"))
        values = config.get("config", value)

        valuelist = values.split(",")
        if len(valuelist) > 1:
            return valuelist
        else:
            return valuelist[0]


class TestInfo(object):
    r = readConfig()
    PACKAGE=r.getValues("package") # test package name
    DEVICES = r.getValues("devices")
    if DEVICES == "127.0.0.1:7555":
        file = excute_adb("connect 127.0.0.1:7555")
        print(file.read())
    TESTCASE = r.getValues("testcase")

### Engine Type
Unity="unity"
UE4="ue4"

class Engine(object):
    Unity="unity"
    UE4="ue4"

EngineType=Engine.Unity #Type="unity" # unity or ue4



if __name__ == "__main__":
    s = TestInfo()