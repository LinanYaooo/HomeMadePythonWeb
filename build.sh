# 依赖安装
pip3 install redis==3.5.3
pip3 install PyYAML==5.3.1
pip3 install flask==1.1.2
#pip3 install psycopg2==2.8.6 -i https://mirrors.aliyun.com/pypi/simple/
pip3 install DButils==2.0

# 启动任务 - 通过 root 权限启动
nohup gunicorn3 -b 0.0.0.0:80 --workers=2 app:app &