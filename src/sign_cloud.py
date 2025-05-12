from cloud import load_clound
from config import do_sleep, initBrowser, load_config, quitBrowser
from imp.sign_click_site import do_sign_site
from message import send_message


def do_sign_cloud(debug, config):
    cookie_cloud_config = config.get("cookie_cloud")
    cookid_data = load_clound(cookie_cloud_config)
    if not cookid_data:
        print("cookie_cloud 加载失败")
        return

    cloud_config = load_config("cloud_config.json")
    pt_sites = cloud_config.get("pt_sites", None)
    pt_success_count = 0
    pt_fail_count = 0
    if pt_sites:
        print("do_sign_pt_sites begin")
        for pt_site in pt_sites:
            site_model = {"url": pt_site}
            re = re_try("do_sign_pt_site", debug, config, cookid_data, site_model)
            if re:
                pt_success_count += 1
            else:
                pt_fail_count += 1
        print("do_sign_pt_sites end")
    send_message(
        config.get("qiye_wx", None),
        "pt_sites执行完毕,成功{pt_success_count},失败{pt_fail_count}",
    )
    do_sleep(3)

    click_success_count = 0
    click_fail_count = 0
    click_sites = cloud_config.get("click_sites", None)
    if click_sites:
        print("do_sign_click_sites begin")
        for click_site in click_sites:
            re = re_try("do_sign_click_site", debug, config, cookid_data, click_site)
            if re:
                click_success_count += 1
            else:
                click_fail_count += 1
        print("do_sign_click_sites end")

    send_message(
        config.get("qiye_wx", None),
        "click_sites执行完毕,成功{click_success_count},失败{click_fail_count}",
    )


def re_try(log, debug, config, cookid_data, click_site):
    re_try = True
    for i in range(3):
        browser = initBrowser(debug, config)
        try:
            do_sign_site(browser, cookid_data, click_site)
            re_try = False
        except Exception as e:
            print("第", i, "次", log, " 异常", click_site, e)
            do_sleep(10 * (i + 1))
        finally:
            quitBrowser(browser)
        if not re_try:
            break
    if re_try:
        return False
    return True
