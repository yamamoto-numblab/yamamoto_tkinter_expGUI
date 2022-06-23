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
root.state('zoomed')#GUI画面の最大化
#center(+)の表示
label = tk.Label(root, text='+',font=("", 150),foreground='#ff0000')#center_markerの表示
label.pack(anchor='center',expand=1)

root.mainloop()