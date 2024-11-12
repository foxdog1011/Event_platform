#!/bin/sh

# 等待数据库服务就绪
/wait-for-it.sh db:3306 --timeout=30 --strict -- echo "Database is up"

# 运行数据库迁移
python manage.py migrate

# 收集静态文件（可选）
python manage.py collectstatic --noinput

# 启动 Django 开发服务器
python manage.py runserver 0.0.0.0:8000
