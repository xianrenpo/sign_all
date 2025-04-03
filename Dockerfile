# 基于的基础镜像
FROM python:3.13.2

# 将代码添加到文件夹
ADD . .

# 设置文件夹为工作目录
WORKDIR /sig_all

# 安装项目依赖
COPY requirements.txt /tmp/requirements.txt
RUN ["pip", "install", "-r", "/tmp/requirements.txt"]
# RUN ["pip", "install", "-r", "/tmp/requirements.txt" , "-i" , "https://pypi.tuna.tsinghua.edu.cn/simple"]

# 运行Python脚本
CMD ["python","-u", "/src/main.py"]
