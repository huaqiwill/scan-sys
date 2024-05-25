# 使用官方 Python 镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 并安装 Python 依赖
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 复制 Django 项目代码
COPY .. /app/

# 暴露端口
EXPOSE 8000

# 运行命令来启动 Django 开发服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
