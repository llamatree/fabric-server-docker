FROM azul-zulu:25-jre-headless-debian13

# サーバーのデータを配置するディレクトリ
WORKDIR /data

# docker-compose.yml で指定した環境変数
ARG EULA
ENV MIN_MEM $MIN_MEM
ENV MAX_MEM $MAX_MEM

# パッケージの更新やインストール、EULAの同意、ユーザー作成と所有権の設定をします。
RUN apt update &&\
    apt upgrade -y &&\
    apt install curl python3 -y &&\
    cd /data &&\
    curl "https://meta.fabricmc.net/v2/versions/loader/26.1/0.18.5/1.1.1/server/jar" -o server.jar &&\
    echo eula=${EULA} > eula.txt &&\
    useradd nonroot -M &&\
    chown -R nonroot:nonroot /data

# セキュリティのため非ルートユーザーでサーバーを起動する
USER nonroot:nonroot

COPY ./wrapper.py /data/wrapper.py

ENTRYPOINT [ "python3", "wrapper.py" ]
