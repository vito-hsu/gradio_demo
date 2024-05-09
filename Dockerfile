# 使用官方 Python 镜像作为基础镜像
FROM python:3.12.3

# 设置工作目录
WORKDIR /app

# 复制当前目录中的所有文件到工作目录
COPY . .

# 安装所需的 Python 库
RUN pip install -r requirements.txt

# 在容器启动时运行的命令
CMD ["python", "20240507-3.py"] 