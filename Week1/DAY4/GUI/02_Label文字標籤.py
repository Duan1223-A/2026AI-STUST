# 教學重點：Label 用來顯示文字（像便利貼）
# 重要觀念：所有元件都要「pack()」或「grid()」才會出現在視窗上

import tkinter as tk

window = tk.Tk()
window.title("Label 練習")
window.geometry("400x300")

# 建立 Label，第一個參數固定是「要放在哪個視窗」
label1 = tk.Label(window, text="哈囉，世界！")

# 文字大小、顏色、背景色
label2 = tk.Label(window, text="我是大字", font=("Arial", 24), fg="red", bg="yellow")

# 把 Label 放上視窗，pack() 會由上往下排
label1.pack()
label2.pack()

window.mainloop()
