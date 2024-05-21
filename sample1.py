import tkinter as tk


# メッセージを表示する関数
def display_message():
    user_input = entry.get()
    label.config(text=f"Hello, {user_input}!")


# メインウィンドウの作成
window = tk.Tk()
window.title("Simple GUI App")
window.geometry("300x200")

# 入力フィールドの作成
entry = tk.Entry(window)
entry.pack(pady=10)

# ボタンの作成
button = tk.Button(window, text="Submit", command=display_message)
button.pack(pady=10)

# 出力ラベルの作成
label = tk.Label(window, text="")
label.pack(pady=10)

# ウィンドウの表示とイベントループの開始
window.mainloop()
