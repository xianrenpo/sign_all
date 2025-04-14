from selenium.webdriver.common.by import By
from cloud import add_cookies, find_base_url
from config import do_sleep


def do_sign_site(browser, cookie_data, click_site):
    print("do_sign_site begin")
    url = click_site.get("url", "")
    if not url:
        return

    browser.get(find_base_url(url))
    re_cookies = add_cookies(browser, cookie_data, url)
    if not re_cookies:
        print("do_sign_site end")
        return
    browser.get(url)
    do_sleep(2)

    do_sign_site_input(browser, click_site.get("input", ""))
    do_sleep(2)

    do_sign_site_btn(browser, click_site.get("btn_id", ""), None)
    do_sleep(2)

    do_sign_site_btn(browser, None, click_site.get("btn_xpath", ""))
    do_sleep(2)

    # do_sign_site_captcha(browser, click_site.get("captcha", None))
    # do_sleep(2)

    do_sign_site_btn(browser, click_site.get("sign_id", ""), None)
    do_sleep(2)

    do_sign_site_btn(browser, None, click_site.get("sign_xpath", ""))
    do_sleep(2)

    do_sleep(3)
    print("do_sign_site end")


def do_sign_site_input(browser, input):
    if not input:
        return
    text = find_element(browser, input.get("id", ""), input.get("xpath", ""))
    if text:
        text.send_keys(input.get("text", ""))


def do_sign_site_btn(browser, btn_id, btn_path):
    if btn_id:
        btn = find_element(browser, btn_id, None)
        if not btn:
            print("do_sign_site_btn error btn_id", btn_id)
        try:
            btn.click()
        except:
            browser.execute_script("arguments[0].click();", btn)

    if btn_path:
        btn = find_element(browser, None, btn_path)
        if not btn:
            print("do_sign_site_btn error btn_path", btn_path)
        try:
            btn.click()
        except:
            browser.execute_script("arguments[0].click();", btn)


def find_element(browser, id, xpath):
    if id:
        return browser.find_element(By.ID, id)

    if xpath:
        return browser.find_element(By.XPATH, xpath)
    return None
