import tkinter as tk
import datetime
import time
#被験者のNo
subject = "sub1"
#被験者データのname
def subDay():
    dt_now = datetime.datetime.now()
    print(dt_now.strftime('%Y_%m%d')+subject)

#実行時間の計測用
start = time.time()

#実験の時間計測
root = tk.Tk()
root.title('test')#ウインドウネーム
#root.state('zoomed')#GUI画面の最大化
a = root.winfo_screenwidth()
b = root.winfo_screenheight()
root.geometry(str(a)+"x"+str(b))
#center(+)の表示
center = tk.Label(root, text='+',font=("", 150),foreground='#ff0000').place(x = a/2-50, y = b/2-150)
left = tk.Label(root, text='<',font=("", 150),foreground='#000000').place(x = a/2-200, y = b/2-150)
right = tk.Label(root, text='>',font=("", 150),foreground='#000000').place(x = a/2+100, y = b/2-150)

#center_markerの表示

root.mainloop()