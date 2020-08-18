"""
多环境下的接口测试
实现原理：
在请求之前对请求的URL进行替换
1.二次封装REQUESTS，对请求定制化
2.将请求结构体的URL从写死的IP地址改为一个（任意的）域名
3.使用一个ENV配置文件，存放各个环境的配置信息
4.将请求结构体中的URL替换为ENV配置文件中个人选择的URL
5.将ENV配置文件使用YAML进行管理
"""
import requests
import yaml


class Api:
    env=yaml.safe_load(open("env.yaml"))
    def send(self,data:dict):
        ##替换
        data["url"]=str(data["url"]).replace("testing-studio",self.env["testing-studio"][self.env["default"]])
        r=requests.request(method=data["method"],url=data["url"],headers=data["headers"])
        return r