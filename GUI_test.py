import tkinter as tk
import datetime

#被験者のNo
subject = "sub1"

dt_now = datetime.datetime.now()
print(dt_now.strftime('%Y_%m%d')+subject)

root = tk.Tk()
root.title('test')#ウインドウネーム
root.state('zoomed')#GUI画面の最大化

label = tk.Label(root, text='+',font=("", 150),foreground='#ff0000')#center_markerの表示
label.pack(anchor='center',expand=1)

root.mainloop()