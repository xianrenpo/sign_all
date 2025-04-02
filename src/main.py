from config import do_sleep, load_config
from apscheduler.schedulers.blocking import BlockingScheduler
from croniter import croniter
from datetime import datetime

from sign_account import do_sign_account
from sign_cloud import do_sign_cloud

debug = False
# debug = True


def main():
    print("启动程序")
    config = load_config("config.json")
    if debug:
        start_sign()
    else:
        scheduler = BlockingScheduler()
        cron = config.get("cron")
        print("cron表达式：", cron)
        next_run_time = croniter(config.get("cron"), datetime.now()).get_next(datetime)
        print(f"下一次执行时间: {next_run_time}")

        try:
            cron_fields = parse_cron_expression(cron)
            scheduler.add_job(start_sign, "cron", **cron_fields)
            print("添加定时任务成功")
            scheduler.start()
        except:
            scheduler.shutdown()
            print("添加定时任务失败")


def parse_cron_expression(cron_expression):
    fields = cron_expression.split()
    if len(fields) != 5:
        raise ValueError("Invalid cron expression")

    minute, hour, day_of_month, month, day_of_week = fields

    return {
        "minute": minute,
        "hour": hour,
        "day": day_of_month,
        "month": month,
        "day_of_week": day_of_week,
    }


def start_sign():
    print("start_sign")
    config = load_config("config.json")

    try:
        do_sign_cloud(debug, config)
    except Exception as e:
        print("do_sign_cloud 异常 等待重试", e)

    do_sleep(3)

    do_sign_account(debug, config)

    # 计算下一次执行时间
    next_run_time = croniter(config.get("cron"), datetime.now()).get_next(datetime)
    print(f"下一次执行时间: {next_run_time}")


if __name__ == "__main__":
    main()
