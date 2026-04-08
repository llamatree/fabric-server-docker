import signal
import subprocess
import sys
import time
from os import getenv

process = None

# Docker停止ハンドラ
def handler(signum, frame):
    global process
    if process and process.poll() is None:
        print("stopping server......")
        # サーバーのプロセスにコマンドを送信します。
        process.stdin.write(b"stop\n")
        process.stdin.flush()
        # セーブが終わるまで待機します。
        print("saving world data......")
        process.wait()
    # セーブ完了後ラッパーを終了する。
    print("exitting wrapper.")
    sys.exit(0)

# シグナルハンドラを登録
signal.signal(signal.SIGTERM, handler)

def start_server():
    global process

    # Dockerfileの環境変数を読み出す
    min_mem = getenv("MIN_MEM")
    max_mem = getenv("MAX_MEM")
    print(min_mem)
    print(max_mem)
    
    # サーバー起動
    process = subprocess.Popen(
            [ "java", "-Xms"+min_mem, "-Xmx"+max_mem, "-XX:+AlwaysPreTouch", "-jar", "server.jar", "nogui" ],
            stdout=sys.stdout,
            stdin=subprocess.PIPE,
            stderr=sys.stderr
    )

    # コマンドを受け付ける
    while True:
        cmd = sys.stdin.readline()
        print("send command")
        process.stdin.write(cmd.encode('utf-8'))
        process.stdin.flush()

    process.wait()
    sys.exit(0)

if __name__ == "__main__":
    start_server()

