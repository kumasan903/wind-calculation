import tkinter as tk

# ボタンを押したときの処理
def calc_wind():
    # かかる時間を計算
    wind = float(windDeg.get())
    spd = float(windSpeed.get())
    rwy = float(runwayDeg.get())
    # 結果をラベルに表示
    s = "風向：" + str(wind) + ",風速：" + str(spd) + ",滑走路方位" + str(rwy)
    labelResult['text'] = s

# ウィンドウを作成
win = tk.Tk()
win.title("到着時間予測")
win.geometry("500x250")

# 部品を作成
# 風方位
labelWinddeg = tk.Label(win, text=u'風方位')
labelWinddeg.pack()

windDeg = tk.Entry(win)
windDeg.insert(tk.END, '160')
windDeg.pack()

# 風速
labelWindSpeed = tk.Label(win, text=u'風速')
labelWindSpeed.pack()

windSpeed = tk.Entry(win)
windSpeed.insert(tk.END, '15')
windSpeed.pack()

# 滑走路方位
labelRWYdeg = tk.Label(win, text=u'滑走路方位')
labelRWYdeg.pack()

runwayDeg = tk.Entry(win)
runwayDeg.insert(tk.END, '360')
runwayDeg.pack()

# 計算結果
labelResult = tk.Label(win, text=u'---')
labelResult.pack()

# 計算ボタン
calcButton = tk.Button(win, text=u'計算')
calcButton["command"] = calc_wind
calcButton.pack()

# ウィンドウを動かす
win.mainloop()