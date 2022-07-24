import tkinter as tk
import math

# ボタンを押したときの処理
def calc_wind():
    # 追い風成分・横風成分の計算
    wind = float(windDeg.get())   # 風向
    spd = float(windSpeed.get())  # 風速
    rwy = float(runwayDeg.get())  # 滑走路方位
    # 差分の計算
    if wind < rwy:
        difference = rwy - wind
    elif wind > rwy:
        difference = wind - rwy
    else:
        difference = 0
    
    if difference > 180:
        difference = 360 - difference
    else:
        difference = difference

    if difference < 0:
        difference = difference * -1
    else:
        difference = difference
    print("difference:"+str(difference))

    # 追い風成分の計算
    tailwind = spd * math.cos(math.radians(difference))
    tailwind = tailwind * -1
    print("radians:"+ str(math.radians(difference)))
    print("tailwind:" + str(tailwind))

    # 横風成分の計算
    if difference == 0:
        crosswind = 0
    elif difference == 180:
        crosswind = 0
    else:
        crosswind = spd * math.cos(math.radians(difference+90))
        crosswind = crosswind * -1
    
    print("crosswind:"+str(crosswind))
    # 結果をラベルに表示
    s = "追い風成分：" + str(round(tailwind,2)) + "kt." + " 横風成分：" + str(round(crosswind,2)) + "kt"
    labelResult['text'] = s

# ウィンドウを作成
win = tk.Tk()
win.title("追い風・横風計算")
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