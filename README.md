# fabric-server-docker
Fabric Loader Minecraft server を Docker 上で起動します。  
Pythonラッパーを使用しているのでコンテナを停止すると自動的にstopコマンドが発動します。  
サーバー管理用ftpサーバも同時起動します。
# 使用方法
>  [!important]
>  起動する前に**必ず**```docker-compose.yml```のFTPユーザー名とパスワードを変更してください!!!!!!
## 設定
- ```docker-compose.yml```
  - ```environment```
    - ```MIN_MEM```: 最小メモリサイズ
    - ```MAX_MEM```: 最大メモリサイズ
    - ```EULA```: MinecraftのEULA (https://aka.ms/MinecraftEULA) に同意する場合はtrueに変更します。**同意しない場合は使用できません!**
  - ```ports```: 公開するポート番号を指定します。(既定値: ```25565:25565```)
## 起動
- 起動する
```
docker compose up -d --build
```
- サーバーコンソールに入る
```
docker attach <コンテナ名>
```
- 停止する
```
docker compose stop
```
- コンテナを削除する
```
# volume(ワールドデータ)を残す
docker compose down

# volume(ワールドデータ)も削除する
docker compose down --volume
```

# FTPサーバー
MODの管理や設定ファイルの編集などに使用できます.
任意のFTPクライアントでログインしてください。

## 設定
- ```docker-compose.yml```
  - ```environment```
    - ```FTP_USER_NAME```: FTPサーバのユーザー名
    - ```FTP_USER_PASS```: FTPのパスワード
    - ```FTP_USER_HOME```: ホームディレクトリ(通常、```/data```から変更する必要はありません。)
    - ```FTP_PASSIVE_PORTS```: FTPパッシブモードで使用するポートの範囲。変更した場合```ports```セクションの公開ポートを合わせる必要があります。
  
> [!NOTE]
> パッシブモードを使用する必要があります
# 注意事項
小規模なマルチプレイ用途を想定しています。不特定多数に公開するなどの用途で使用する場合セキュリティやパフォーマンスに問題が生じる可能性があります。  
Minecraft の公式のサービス,製品ではありません。Mojang または Microsoft から承認を受けておらず、それとの関連性もありません。
