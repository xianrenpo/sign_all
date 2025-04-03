# 签到适配

## 1.1 新建conf文件夹 
## 1.2 config.json account_config.json cloud_config.json 复制进去 
## 1.3 配置好账号信息

# 注意conf目录的映射是否正确

compsoer.yml
``` 
  chrome:
    container_name: chrome
    image: selenium/standalone-chrome
    ports:
      - 4444:4444

  sign-all:
    container_name: sign-all
    image: xxdojia/sign-all
    environment:
      - TZ=Asia/Shanghai
    volumes:
      - /conf:/src/conf
    depends_on:
      - chrome
    restart: unless-stopped

```

## 附：config.json说明
## account_config.json cloud_config.json参考文件说明
```
{
    "cron":"55 12 12 * *",
    "chrome":"http://192.168.x.x:4444",
    "cookie_cloud":{
        "domain":"http://192.168.x.x:8088/",
        "uuid":"用户KEY · UUID",
        "pwd":"端对端加密密码"
    }
}
```