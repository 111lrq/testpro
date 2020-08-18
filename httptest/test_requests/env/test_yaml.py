#json格式数据转化为yaml格式
import yaml


def testyaml2():
    env = {
        "default": "dev",
        "testing-studio": {
            "dev": "127.0.0.1",
            "test": "127.0.0.2"
        }
    }
    with open("env.yaml","w") as f:
        yaml.safe_dump(data=env,stream=f)