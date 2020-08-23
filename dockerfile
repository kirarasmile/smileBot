FROM debian:buster-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
		ca-certificates \
		netbase \
	&& rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y --no-install-recommends \
                    dpkg-dev \
                    gcc \
                    libbluetooth-dev \
                    libbz2-dev \
                    libc6-dev \
                    libexpat1-dev \
                    libffi-dev \
                    libgdbm-dev \
                    liblzma-dev \
                    libncursesw5-dev \
                    libreadline-dev \
                    libsqlite3-dev \
                    libssl-dev \
                    make \
                    tk-dev \
                    uuid-dev \
                    wget \
                    xz-utils \
                    zlib1g-dev
                    
COPY Python-3.7.3.tgz /usr/local/src


WORKDIR /usr/local/src
RUN tar -xf Python-3.7.3.tgz
WORKDIR Python-3.7.3
RUN ./configure --prefix=/usr/local/python37 && make && make install
ENV PATH /usr/local/python37/bin:$PATH


WORKDIR /usr/local/src
RUN mkdir /bot
ADD config.py /bot
ADD bot.py /bot
ADD src /bot/src

WORKDIR /bot
RUN pip3 install aiocqhttp
RUN pip3 install requests
RUN pip3 install uvicorn
RUN pip3 install feedparser


CMD ["uvicorn","--host","0.0.0.0","--port","8090","bot:bot.asgi"]
