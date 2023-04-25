FROM ubuntu:20.04

# Update source is domestic
RUN sed -i 's/archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get update --fix-missing -o Acquire::http::No-Cache=True

# Update time zone
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && apt-get install -y tzdata

# Installing python3.8 and server
RUN apt-get -y install python3 python3-pip python3-dev python3-venv git && apt-get clean

# Set the Python3 pip mirror to the Tsinghua source
RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/ && pip3 install --upgrade pip

# Set Python3 to use UTF-8 encoding by default
ENV PYTHONIOENCODING utf-8

# Set virtualenv
ENV VIRTUAL=/venv
RUN python3 -m venv $VIRTUAL
ENV PATH="$VIRTUAL/bin:$PATH"

# Application building
WORKDIR /myflask

# Clone the code and authenticate
RUN git clone https://ichpan:acp123523@gitee.com/ichpan/myflask.git .
RUN pip3 install -r requirements.txt

EXPOSE 5001
ENTRYPOINT ["gunicorn", "-c", "gunicorn.conf.py", "manage:app"]