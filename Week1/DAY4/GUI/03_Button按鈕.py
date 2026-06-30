# 教學重點：Button 按鈕，按下去會執行一個函式
# 重要觀念：command= 後面接「函式名稱」，不要加 () 括號！

import tkinter as tk

window = tk.Tk()
window.title("Button 練習")
window.geometry("400x300")

# 先寫一個「按下去要做什麼」的函式
def 按我():
    print("你按了我！")

# 建立按鈕，command 指定按下去要呼叫的函式
button = tk.Button(window, text="按我看看", command=按我)
button.pack()

# 多一顆按按下會關閉視窗
button2 = tk.Button(window, text="關閉視窗", command=window.destroy)
button2.pack()

window.mainloop()
