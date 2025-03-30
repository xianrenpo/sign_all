from cloud import load_clound
from config import do_sleep, load_config
from imp.sign_click_sites import do_sign_site


def do_sign_cloud(browser, cookie_cloud_config):
    cookid_data = load_clound(cookie_cloud_config)
    cloud_config = load_config("cloud_config.json")

    pt_sites = cloud_config.get("pt_sites", None)
    if pt_sites:
        print("do_sign_pt_sites begin")
        for pt_site in pt_sites:
            site_model = {"url": pt_site}
            try:
                do_sign_site(browser, cookid_data, site_model)
            except Exception as e:
                print("do_sign_pt_sites 异常", e)
        print("do_sign_pt_sites end")

    click_sites = cloud_config.get("click_sites", None)
    if click_sites:
        print("do_sign_click_sites begin")
        for click_site in click_sites:
            try:
                do_sign_site(browser, cookid_data, click_site)
            except Exception as e:
                print("do_sign_click_sites 异常", e)
        print("do_sign_click_sites end")

    do_sleep(3)

    try:
        browser.quit()
    except Exception as e:
        print("browser.quit 异常 暂时忽略", e)
