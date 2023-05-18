import threading
import tkinter as tk
import pytchat
import time

# PytchatCoreオブジェクトの取得
livechat = pytchat.create(video_id="XXXXXXXXXXX")

def update_text():
    while True:
        # チャットデータの取得
        chatdata = livechat.get()
        for c in chatdata.items:
            # テキストを追加
            text.insert('end', f"{c.datetime}\n{c.author.name}\n{c.message}\n{c.amountString}\n")
            # スクロールする
            text.see('end')

        time.sleep(1)

# メインウィンドウを作成
root = tk.Tk()

# ウィンドウの背景を透過する
root.attributes("-alpha", 0.5)

# ウィンドウを最前面に固定する
root.attributes("-topmost", True)

# ウィンドウのサイズを変更する
root.geometry("500x700")

# テキストウィジェットを作成して、テキストを設定
text = tk.Text(root, font=("メイリオ", 20, "bold"))
text.pack()

# 別スレッドでupdate_text()関数を実行する
thread = threading.Thread(target=update_text)
thread.start()

# メインループを開始
root.mainloop()