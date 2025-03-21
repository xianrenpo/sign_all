import json
import os
from time import sleep


def load_config(fileName):
    # 获取当前文件所在的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建配置文件的相对路径
    config_path = os.path.join(current_dir, "conf", fileName)

    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)
        return config


def do_sleep(second):
    print(f"等待{second}秒")
    sleep(second)
