import datetime
import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config import load_config


def send_message(m_config, text):
    if not m_config:
        return
    if not text:
        return
    agentid = m_config.get("agentid", None)
    if not agentid:
        print("agentid is not found")
        return
    try:
        access_token = save_and_load_access_token(m_config)
        url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}"
        data = {
            "touser": "@all",
            "msgtype": "text",
            "agentid": agentid,
            "text": {"content": f"sign-all {text}"},
            "safe": 0,
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            data = response.json()
            errcode = data.get("errcode", "")
            if "errcode" not in data or errcode != 0:
                print("发送失败:", text, errcode, data.get("errmsg", ""))
        else:
            print("发送失败:", text, response.text)
    except Exception as e:
        print("发消息失败", text, e)
        return


def save_and_load_access_token(m_config):
    if not m_config:
        return None
    file_path = "access_token.txt"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            line = file.readline()
            if line:
                timestamp, access_token = line.split("|")
                timestamp = float(timestamp)
                # 判断是否过期
                if (
                    timestamp + 7000 > datetime.datetime.now().timestamp()
                    and access_token
                ):
                    return access_token

    access_token = load_access_token(m_config)
    # 保存到txt
    # 获取当前时间戳
    timestamp = datetime.datetime.now().timestamp()

    with open(file_path, "w") as file:
        file.write(f"{timestamp}|{access_token}")
    return access_token


def load_access_token(m_config):
    corpid = m_config.get("corpid", None)
    secret = m_config.get("secret", None)

    session = requests.Session()
    retries = Retry(
        total=5,  # 重试次数
        backoff_factor=1,  # 退避指数
        status_forcelist=[500, 502, 503, 504],  # 需要重试的HTTP状态码
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))

    try:
        # 发送请求
        response = session.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params={"corpid": corpid, "corpsecret": secret},
            timeout=10,  # 设置超时时间
        )
        response.raise_for_status()  # 检查请求是否成功
        data = response.json()
        if "access_token" in data:
            access_token = data["access_token"]
            return access_token
        else:
            print("Failed to get access token.")
            return None
    except Exception as e:
        print(f"load_access_token 出错: {e}")
        return None
