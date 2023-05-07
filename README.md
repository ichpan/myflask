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

docker run -d -p HostPort:ContainerPort --name myflask ImageID
~~~

#### 鉴权
~~~bash
在请求除了登录注册意外的接口,需要在请求头携带令牌

Authorization: Bearer your-token
~~~

#### celery

~~~bash
celery -A application.timed_task.celery_app beat -l info
celery -A application.timed_task.celery_app worker -l info

# 使用multi方式启动定时任务,celery会自动生成任务子节点和自动创建子进程
# work为执行任务的进程名字
# -A main 指定定时任务的启动函数main
# -l info 指定日志等级为info
# -B 将celery定时任务设置为后台守护进程,不占用终端
# --logfile=celerylog.log 指定日志保存的文件名.也可指定路径加文件名

celery multi start work -A main -l info -B --logfile=celerylog.log
# 停止定时任务时,将start换成stop
celery multi stop work -A main -l info -B --logfile=celerylog.log
# 重启定时任务,将start换成restart
celery multi restart work -A main -l info -B --logfile=celerylog.log
~~~
