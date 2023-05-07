<<<<<<< HEAD
from flask import *
from time import *
#导入库

app = Flask(__name__)
train = "G52"
station = [["重庆北", [7, 32], 0, "Chongqingbei"], ["南阳东", [10, 52], 2, "Nanyangdong"],
           ["郑州东", [12, 7], 3, "Zhengzhoudong"], ["石家庄", [13, 25], 2, "Shijiazhuang"],
           ["北京西", [14, 26], -1, "Beijingxi"]]
#站点
#添加开车时间
for i in range(len(station)):
    t = [0, 0]
    t[1] = station[i][1][1] + station[i][2]
    print(t, station[i][2])
    if t[1] >= 60:
        t[0] += station[i][1][0] + int(t[1] / 60)
        t[1] %= 60
    else:
        t[0] = station[i][1][0]
    station[i].append(t)
print(station)


def time__(time_in):
    time_now = [0, 0]
    time_now[0] = int(strftime("%H", localtime()))
    time_now[1] = int(strftime("%M", localtime()))
    if time_in[0] < time_now[0]:
        return False
    elif time_in[0] == time_now[0]:
        if time_in[1] < time_now[1]:
            return False
        else:
            return True
    return True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/train")
def train():
    for i in range(0, len(station) - 1):
        if time__(station[i][1]) == False and time__(station[i][4]):
            return render_template("station_arr.html", list=station[i], time_now=strftime("%H:%M", localtime()))
        if time__(station[i][1]) == False and time__(station[i + 1][1]) == True:
            return render_template("station_go.html", list=station[i + 1], time_now=strftime("%H:%M", localtime()),
                                   ltime=str(int(float(localtime().tm_hour * 60 + localtime().tm_min - (
                                               station[i + 1][1][0] * 60 - station[i + 1][1][1])) / 60)), ltime2=
                                         str(int(float(localtime().tm_hour * 60 + localtime().tm_min - (
                                                     station[i + 1][1][0] * 60 - station[i + 1][1][1])) % 60)) + "分")
        else:
            return render_template("end.html", end=station[len(station) - 1], time_now=strftime("%H:%M", localtime()))


app.run()
=======
from flask import *
from time import *
from xpinyin import *

app = Flask(__name__)
train = "G52"
station = [["重庆北", [7, 32], 0, "Chongqingbei"], ["南阳东", [10, 52], 2, "Nanyangdong"],
           ["郑州东", [12, 7], 3, "Zhengzhoudong"], ["石家庄", [13, 25], 2, "Shijiazhuang"],
           ["北京西", [14, 26], -1, "Beijingxi"]]
for i in range(len(station)):
    t = [0, 0]
    t[1] = station[i][1][1] + station[i][2]
    print(t, station[i][2])
    if t[1] >= 60:
        t[0] += station[i][1][0] + int(t[1] / 60)
        t[1] %= 60
    else:
        t[0] = station[i][1][0]
    station[i].append(t)
print(station)


def time__(time_in):
    time_now = [0, 0]
    time_now[0] = int(strftime("%H", localtime()))
    time_now[1] = int(strftime("%M", localtime()))
    if time_in[0] < time_now[0]:
        return False
    elif time_in[0] == time_now[0]:
        if time_in[1] < time_now[1]:
            return False
        else:
            return True
    return True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/train")
def train():
    for i in range(0, len(station) - 1):
        if time__(station[i][1]) == False and time__(station[i][4]):
            return render_template("station_arr.html", list=station[i], time_now=strftime("%H:%M", localtime()))
        if time__(station[i][1]) == False and time__(station[i + 1][1]) == True:
            return render_template("station_go.html", list=station[i + 1], time_now=strftime("%H:%M", localtime()),
                                   ltime=str(int(float(localtime().tm_hour * 60 + localtime().tm_min - (
                                               station[i + 1][1][0] * 60 - station[i + 1][1][1])) / 60)), ltime2=
                                         str(int(float(localtime().tm_hour * 60 + localtime().tm_min - (
                                                     station[i + 1][1][0] * 60 - station[i + 1][1][1])) % 60)) + "分")
        else:
            return render_template("end.html", end=station[len(station) - 1], time_now=strftime("%H:%M", localtime()))


app.run()
>>>>>>> 9e01e9a (G52 chinese train time website)
