# 签到适配


# 1 启动依赖的chrome容器和cookiecloud容器

# 1.1 启动chrome容器
``` 
  chrome:
    container_name: chrome
    image: selenium/standalone-chrome
    ports:
      - "4444:4444"

```
# 1.2 启动cookiecloud容器
``` 
  cookiecloud:
    image: easychen/cookiecloud:latest
    container_name: cookiecloud
    environment:
      - PUID=0
      - PGID=0
    ports:
      - 8088:8088
    restart: unless-stopped

```




# 2 sign-all容器
## 2.1 本地构建sign-all镜像
## 2.2 先进入代码目录下 执行以下命令
```
docker build -t sign-all:0.0.1 .

```



## 2.3 新建conf文件夹 config.json account_config.json cloud_config.json 复制进去 并配置好账号信息
## 2.4 再启动构建好的sign-all容器,注意conf目录的映射是否正确
```

  sign-all:
    container_name: sign-all
    image: sign-all:0.0.1
    environment:
      - TZ=Asia/Shanghai
    volumes:
      - /conf:/src/conf
    depends_on:
      - chrome
      - cookiecloud
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