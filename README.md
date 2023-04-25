# myflask

#### 介绍
a base flask frame.

#### 数据库迁移
~~~bash
# 设置启动脚本
export FLASK_APP=manage.py

# 创建迁移版本仓库
python -m flask db init
# 创建迁移版本
python -m flask db migrate -m 'initial migration'
# 升级版本库的版本
python -m flask db upgrade
~~~


#### build
~~~bash
docker build --no-cache -f Dockerfile -t myflask:v0.1 .

docker run -d -p HostPort:ContainerPort ImageID
~~~

#### 鉴权
~~~bash
在请求除了登录注册意外的接口,需要在请求头携带令牌

Authorization: Bearer your-token
~~~
