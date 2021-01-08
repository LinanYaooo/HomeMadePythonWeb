# 启动构建
echo "构建启动"
echo $(pwd)

# 启动任务 - 通过 root 权限启动
nohup gunicorn3 -b 0.0.0.0:81 --workers=4 application.manage:app > /home/ubuntu/guncorn.log 2>&1 &