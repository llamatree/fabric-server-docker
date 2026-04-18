# fabric-server-docker
Fabric Loader Minecraft server を Docker 上で起動します。  
Pythonラッパーを使用しているのでコンテナを停止すると自動的にstopコマンドが発動します。  
File Browser を同時起動します。   
# 使用方法
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

# File Browser
ブラウザからログインできるファイルマネージャーです。   
MODの追加や設定ファイルの編集に使用できます。
> [!important]
> MODを導入する前にMinecraftサーバーを停止してください。   
> ```
> docker compose stop minecraft
> ```   

## ログイン方法
サーバー側で以下のコマンドを実行して初期パスワードを確認します。
```
docker logs fabric-server-docker-filebrowser-1
```
以下のように初期パスワードが表示されます
```
.......
User 'admin' initialized with randomly generated password: xxxxxxxxxxxx
.......
```

ブラウザでサーバーへポート8080(初期設定の場合)で接続します。   
ユーザー名は```admin```,パスワードは上記コマンドで確認した値でログインします。   
ログイン後、設定でユーザーの追加やパスワードの変更ができます。   
詳しくは[公式ドキュメント](https://filebrowser.org/index.html)をご覧ください。

# 注意事項
小規模なマルチプレイ用途を想定しています。不特定多数に公開するなどの用途で使用する場合セキュリティやパフォーマンスに問題が生じる可能性があります。  
Minecraft の公式のサービス,製品ではありません。Mojang または Microsoft から承認を受けておらず、それとの関連性もありません。   
   
