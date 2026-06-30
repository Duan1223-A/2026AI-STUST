# 教學重點：Entry 單行輸入框，取得使用者打的字
# 重要觀念：用 .get() 拿到使用者輸入的內容

import tkinter as tk

window = tk.Tk()
window.title("Entry 練習")
window.geometry("400x300")

label = tk.Label(window, text="請輸入你的名字：")
label.pack()

# 建立輸入框
entry = tk.Entry(window)
entry.pack()

# 用來顯示結果的 Label
result = tk.Label(window, text="")
result.pack()

def 打招呼():
    # entry.get() 會回傳目前輸入框裡的字串
    名字 = entry.get()
    # .config() 可以改變 Label 的設定
    result.config(text=f"哈囉，{名字}！")

button = tk.Button(window, text="送出", command=打招呼)
button.pack()

window.mainloop()
