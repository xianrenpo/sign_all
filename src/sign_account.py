from imp.sign98 import do_login, do_reply, do_sign
from config import do_sleep, do_sleep_random, initBrowser, load_config, quitBrowser
from imp.sign_account_site import do_sign_account_site


def do_sign_account(debug, config):
    account_config = load_config("account_config.json")

    do_sign_98(debug, config, account_config.get("98"))

    print("common 执行开始")
    common_configs = account_config.get("common", None)
    if not common_configs:
        return
    for common_config in common_configs:
        url = common_config.get("url", "未配置")
        try:
            print(url, "do_sign_account_site 执行开始")
            with initBrowser(debug, config) as browser:
                do_sign_account_site(browser, common_config)
            print(url, "do_sign_account_site 执行结束")
        except Exception as e:
            print(url, "do_sign_account_site 异常 等待重试", e)
    print("common 执行结束")


def do_sign_98(debug, config, config98):
    try:
        do_sleep_random("98签到随机延迟", config98.get("sleepRandomSeconds", 3600))
        with initBrowser(debug, config) as browser:

            print("98 开始登录")
            do_login(browser, config98)
            print("98 登录完毕")
            do_sleep(5)

            print("98 开始回复")
            do_reply(browser, config98)
            print("98 回复完毕")
            do_sleep(5)

            print("98 开始签到")
            do_sign(browser, config98)
            print("98 签到完毕")
            do_sleep(5)

            quitBrowser(browser)
    except Exception as e:
        print("do_sign_98 异常 等待重试", e)
