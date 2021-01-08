# 自动化构建测试
echo "构建"

# 依赖安装
pip3 install redis==3.5.3
pip3 install PyYAML==5.3.1
pip3 install flask==1.1.2
pip3 install psycopg2==2.8.6
pip3 install DBUtils==2.0
pip3 install pandas==1.2.0

# 打印必要环境变量
echo $PG_PWD