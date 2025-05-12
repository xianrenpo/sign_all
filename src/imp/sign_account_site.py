from selenium.webdriver.common.by import By

from config import do_sleep


def do_sign_account_site(browser, common_config):
    url = common_config.get("url", None)
    if not url or not url.startswith("http"):
        return
    login = common_config.get("login", None)
    account = common_config.get("account", None)
    browser.get(url)
    if login and account:
        do_sleep(8)
        do_login_account_site(browser, login, account)

    browser.get(url)
    sign_xpath = common_config.get("sign_xpath", None)
    if sign_xpath:
        do_sleep(9)
        browser.find_element(By.XPATH, sign_xpath).click()
        do_sleep(3)


def do_login_account_site(browser, login, account):
    uid_input_xpath = login.get("uid_input_xpath", None)
    pwd_input_xpath = login.get("pwd_input_xpath", None)
    if not uid_input_xpath or not pwd_input_xpath:
        print("uid_input_xpath或者pwd_input_xpath未配置 跳过执行")
        return
    uid = account.get("uid", None)
    pwd = account.get("pwd", None)
    if not uid or not pwd:
        print("uid或者pwd未配置 跳过执行")
        return
    do_sleep(5)
    browser.find_element(By.XPATH, uid_input_xpath).send_keys(uid)
    do_sleep(3)
    browser.find_element(By.XPATH, pwd_input_xpath).send_keys(pwd)
    do_sleep(3)

    btn_xpath = login.get("btn_xpath", None)
    if not btn_xpath:
        print("btn_xpath未配置 跳过执行")
    browser.find_element(By.XPATH, btn_xpath).click()
    do_sleep(3)
