import configparser

#获取配置文件中的参数配置
class GetConfig(object):

    def configures(self,filename,section,option):
        conf = configparser.ConfigParser()
        self.filename = filename
        self.section = section
        self.option = option
        conf.read(self.filename)
        val = conf.get(self.section,self.option)
        return val

#eg.
# getconf = GetConfig()
# print(getconf.configures("configures.ini","db","host"))