from PyCookieCloud import PyCookieCloud


def load_clound(ccConfig):
    cookie_cloud = PyCookieCloud(
        ccConfig.get("domain"), ccConfig.get("uuid"), ccConfig.get("pwd")
    )
    the_key = cookie_cloud.get_the_key()
    if not the_key:
        print("Failed to get the key")
        return
    decrypted_data = cookie_cloud.get_decrypted_data()
    if not decrypted_data:
        print("Failed to get decrypted data")
        return
    return decrypted_data


def add_cookies(browser, cookie_data, url):
    domain = find_domain(url)
    cookies = cookie_data.get(domain)
    for cookie in cookies:
        cookie_dict = {
            "name": cookie.get("name"),
            "value": cookie.get("value"),
        }
        browser.add_cookie(cookie_dict)


def find_domain(url):
    domain = url.split("/")[2]
    return domain


def find_base_url(url):
    array = url.split("/")
    return array[0] + "//" + array[2]
