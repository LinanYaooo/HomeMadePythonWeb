# 依赖安装
pip3 install redis==3.5.3
pip3 install PyYAML==5.3.1
pip3 install flask==1.1.2


# 启动任务
gunicorn3 -b 127.0.0.1:80 --workers=4 app:app