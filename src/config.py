import json
import os
from time import sleep
from selenium import webdriver


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


def initBrowser(debug, config):
    if debug:
        browser = webdriver.Edge()
        browser.implicitly_wait(30)
        return browser
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome = f'{config.get("chrome")}/wd/hub'
        browser = webdriver.Remote(command_executor=chrome, options=chrome_options)
        browser.implicitly_wait(30)
        return browser


def quitBrowser(browser):
    if not browser:
        return

    do_sleep(3)

    try:
        browser.quit()
    except:
        print("browser.quit 错误 暂时忽略")
