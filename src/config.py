from datetime import datetime
import json
import os
import random
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
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 等待{second}秒")
    sleep(second)


def do_sleep_random(text, second):
    random_second = random.randint(0, second)
    print(f"{text}等待{random_second}秒")
    sleep(random_second)


def initBrowser(debug, config):
    if debug:
        browser = webdriver.Edge()
        browser.set_page_load_timeout(30)
        browser.set_script_timeout(10)
        return browser
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.images": 2}
        )
        chrome = f'{config.get("chrome")}/wd/hub'
        browser = webdriver.Remote(command_executor=chrome, options=chrome_options)
        browser.set_page_load_timeout(30)
        browser.set_script_timeout(10)
        return browser


def quitBrowser(browser):
    if not browser:
        return

    do_sleep(3)

    try:
        browser.quit()
    except:
        print("browser.quit 错误 暂时忽略")
