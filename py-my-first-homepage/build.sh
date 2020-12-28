# 依赖安装
pip install redis==3.5.3
pip install PyYAML==5.3.1

# 启动任务
gunicorn -b 0.0.0.0:80 --workers=4 app:app &