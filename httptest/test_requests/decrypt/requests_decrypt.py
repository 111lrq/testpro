import json
import requests
import base64

class ApiRequest:
    def send(self,data:dict):
        res=requests.request(data["method"],data["url"],headers=data["headers"])
        if data["encoding"]=="base64":
            return json.loads(base64.b64decode(res.content))
        ##把加密过后的响应值发送给第三方服务，让第三方去做解密然后返回
        elif data["encoding"]=="private":
            #此处的url应该是第三方平台的地址，此处暂时随便写一个
            return requests.post("url",data=res.content)

# def test_encode():
#     url = "http://0.0.0.0:999/demo1.txt"
#     r = requests.get(url=url)
#     # print(r.text)
#     # 获取二进制响应结果r.content
#     # res = base64.b64decode(r.content)
#     # print(res)
#     # json格式化
#     res=json.loads(base64.b64decode(r.content))
#     print(res)
