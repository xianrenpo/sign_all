from imp.sign98 import do_login, do_reply, do_sign
from config import do_sleep, load_config


def do_sign_account(browser):
    account_config = load_config("account_config.json")
    do_sign_98(browser, account_config.get("98"))


def do_sign_98(browser, config98):
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
