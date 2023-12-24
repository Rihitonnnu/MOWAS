import threading

def func():
    while True:
        print("子スレッド")
        # Check if the user pressed Ctrl+C
        if threading.currentThread().stopped():
            break

if __name__ == "__main__":
    try:
        thread = threading.Thread(target=func)  # 処理を割り当てる
        thread.start()  # スレッドを起動する
        print("親スレッド")
    except KeyboardInterrupt:
        print("プログラムを終了します")
