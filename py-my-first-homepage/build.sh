# 依赖安装
pip install redis

# 启动任务
gunicorn -bind 0.0.0.0:80 --workers 4 app:app