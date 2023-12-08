# 데이터 시각화
import matplotlib.pyplot as plt

#기본사용
# y축 데이터 지정 구성
# value = [1, 2, 3, 4]
# value = [2, 4, 5, 7, 10]
# res = plt.plot(value)
# plt.show()


# x, y축 두 축 지정 구성
""" x_value = [2, 3, 6, 7, 10]
y_value = [1, 4, 5, 8, 9]

plt.plot(x_value, y_value)
# res = plt.plot([2, 3, 6, 7, 10], [1, 4, 5, 8, 9])
plt.show() """


#딕셔너리 설정
""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)
plt.show() """



#레이블 설정
""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)
plt.xlabel("x_data")
# plt.ylabel("x_data")
plt.ylabel("y_data")
plt.show() """

# 레이블 여백 조절
""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)

plt.xlabel("x_data", labelpad=15)
plt.ylabel("y_data", labelpad=50)

plt.show() """

#위치 조절
# dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

# plt.plot("x_data", "y_data", data=dic_val)

# plt.xlabel("x_data", labelpad=10)
# plt.ylabel("y_data", labelpad=10)

# """ plt.xlabel("x_data", loc="right")
# plt.ylabel("y_data", loc="top") """

# plt.xlabel("x_data", loc="left") #센터는 디폴트 값
# plt.ylabel("y_data", loc="bottom")

# plt.show()


# 다중데이터 출력
""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)
# plt.plot([1,3,5,7,9], [2,4,6,8,10])
plt.show() """


# 라벨출력
""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.xlabel("x_data")
plt.ylabel("y_data")

plt.legend()
plt.show() """

# 라벨 위치 조절
""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.xlabel("x_data")
plt.ylabel("y_data")

# plt.legend(loc=(1, 1))
# plt.legend(loc=(0.5, 0.5))
# plt.legend(loc="best")

# 키워드로도 조절가능
plt.legend(loc="lower right")
plt.show() """

# 라벨 출력 조절
""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)

plt.xlabel("x_data")
plt.ylabel("y_data")

plt.legend(ncol=1)
# : (ncol=1) 
# : (ncol=2) 
plt.show()
 """
 
# 폰트조절
""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)

plt.xlabel("x_data")
plt.ylabel("y_data")

plt.legend(ncol=2, fontsize=20)
plt.show() """

# 테두리 설정
""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)

plt.xlabel("x_data")
plt.ylabel("y_data")

# plt.legend(ncol=2, fontsize=10, frameon=True)
plt.legend(ncol=2, fontsize=10, frameon=False)
plt.show()
 """
 
# 테두리 음영 설정
""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)

plt.xlabel("x_data")
plt.ylabel("y_data")

plt.legend(ncol=2, fontsize=10, shadow=True)
plt.show() """


# 축 범위 지정
""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)
plt.xlabel("x_data")
plt.ylabel("y_data") """

# plt.xlim()
# plt.ylim()

# plt.show()

# 현재 축 범위 출력
# x_min, x_max = plt.xlim()
# y_min, y_max = plt.ylim()
# print(x_min, x_max)
# print(y_min, y_max)

# 축 계산
# plt.xlim(x_min - 0.6, x_max)
# plt.ylim(y_min - 0.6, y_max)

# 축 범위 지정
# plt.xlim([0, 10])
# plt.ylim([0, 10])

# plt.xlim([0, 50])
# plt.ylim([0, 50])

# plt.xlim([-5, 10])
# plt.ylim([5, 10])

# 두축 값 동시 확인, 두 축을 동시 지정
# x_min, x_max, ymin, ymax = plt.axis()
# print(x_min, x_max, y_min, y_max)
# plt.axis([-5, 10, -5, 10])
# plt.show()

# 축 출력 옵션 지정
# plt.axis("square")
# plt.axis("scaled")
# plt.axis("equal")
# plt.axis("tight")
# plt.axis("auto")
# plt.axis("off")
# plt.show()


# 선 스타일 설정
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "--", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], ":", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "-.", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], ".", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], ".-", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], ".--", label = "PData(km)")


# 선 스타일 지정
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashed", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dotted", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashdot", label="PData(km)")
# plt.show()

# 선 스타일 수동 지정
# linestyle(0, (픽셀크기, 여백간격))
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (1, 0)), label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (5, 10)), label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (3, 1, 1, 1, 1, 1)), label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (1, 10)), label="PData(km)")

# 색 지정
# plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="r", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="yellow", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#F5EC17", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#000000", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C1", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C6", label="Value(m)")

# Shape
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="round", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=3, solid_capstyle="round", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=5, dash_capstyle="round", label="Value(m)")

# 마커 지정
                             	# c=cyan d=diamond
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "cd", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "co--", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "go-", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "yo-.", label="PData(km)")

# 마커 / 선 동시 설정, marker 파라메터 사용
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo-", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo--", label="PData(km)")

# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="H", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker=11, label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="s", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="x", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker=D, label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="$test$", label="PData(km)")


# 그래프 영역 채우기

""" xdata = [2,3,6,7,10]
ydata = [1,4,5,8,9]
y1data = [2,4,6,8,10]

plt.plot(xdata, ydata)
plt.plot(xdata,y1data)
plt.xlabel("x_data")
plt.ylabel("y_data") """

#세로축채우기
# plt.fill_between(xdata[1:4], ydata[1:4], alpha=0.5)
# plt.fill_between(xdata[:4], ydata[:4], alpha=0.5)
# plt.fill_between(xdata[12:4], ydata[2:4], alpha=0.5)
# plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.5)
# plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.3)

#가로축채우기
# plt.fill_betweenx(ydata[1:3], xdata[1:3], alpha=0.3)
# plt.fill_betweenx(ydata[2:3], xdata[2:3], alpha=0.3)
# plt.fill_betweenx(ydata[1:5], xdata[1:5], alpha=0.3)

# 범위 지정 영역 채우기
# plt.fill([2.9, 2.9, 7.1, 7.1], [2.5, 5.0, 8.5, 6.0], alpha=0.5)
# plt.fill([2.9, 2.9, 7.1, 7.1], [2.5, 2.5, 2.5, 6.0], alpha=0.2)
# plt.fill_between(xdata[1:4], ydata[1:4], y1data[1:4], alpha=0.5)

# 배경 설정

""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val, label = "PData(km)")
plt.plot("x1_data", "y1_data", data=dic1_val, label = "value(m)")

plt.xlabel("x_data")
plt.ylabel("y_data")

plt.grid()
 """
# x축 그리드
# plt.grid(axis="x")

# y축 그리드
# plt.grid(axis="y")

# 색상 설정
# plt.grid(axis="y", color="g")
# plt.grid(axis="y", color="b")

# 투명도 설정
# plt.grid(axis="y", color="g", alpha=0.5)

# 선 종류 선택
# plt.grid(axis="y", color="g", alpha=0.5, linestyle="-")
# plt.grid(axis="x", color="r", alpha=0.3, linestyle=":")
# plt.grid(axis="y", color="r", alpha=0.5, linestyle="--")
# plt.grid(axis="y", color="b", alpha=0.5, linestyle="-.")

# 눈금표시
# plt.xticks()
# plt.yticks()

# 임의 데이터 지정
# plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
# plt.yticks([0,1,2,3,4,5,6,7,8,9,10])

# plt.xticks([1,3,5,7,9,11])
# plt.yticks([2,4,6,8,10,12])

# 라벨 지정
# plt.xticks([1,2,3,4,5,6,7,8,9,10], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
# plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# 눈금 안쪽/바깥쪽 지
# plt.tick_params(axis="y", direction="out")
# plt.tick_params(axis="x", direction="in")

#막대그래프 그리기
""" x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["r", "lime", "b"]
 """
# plt.bar(x_years, y_data)

#색 지정
# plt.bar(x_years, y_data, color="g")
# plt.bar(x_years, y_data, color="C7")
# plt.bar(x_years, y_data, color="#000000")

# plt.bar(x_years, y_data, color=clr)

# plt.bar(x_years, y_data, color=clr, width=2)
# plt.bar(x_years, y_data, color=clr, width=0.7)
# plt.bar(x_years, y_data, color=clr, width=0.1)

# plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
# plt.bar(x_years, y_data, color=clr, align="center", width=0.5)

# 라인 색 선택
# plt.bar(x_years, y_data, color=clr, align="edge", edgecolor="black", width=3)

# 테두리 라인 설정
# plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, width=0.5)

# plt.xticks(x_years)
# plt.yticks(y_data, y_data)
# plt.yticks(100,200,300,400,500,600,900)

""" plt.barh(x_years, y_data)

#   {x축 데이터}{y축 데이터}{색설정} {위치설정} {테두리색설정} {선두께} {그래프 두께}
plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)

plt.show() """


#####################################################################
#####################################################################
#####################################################################
##### 23.12.08


#막대그래프 그리기
""" x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["r", "lime", "b"]

plt.bar(x_years, y_data) """

#색 지정
# plt.bar(x_years, y_data, color="g")
# plt.bar(x_years, y_data, color="C7")
# plt.bar(x_years, y_data, color="#000000")

# plt.bar(x_years, y_data, color=clr)

# plt.bar(x_years, y_data, color=clr, width=2)
# plt.bar(x_years, y_data, color=clr, width=0.7)
# plt.bar(x_years, y_data, color=clr, width=0.1)

# plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
# plt.bar(x_years, y_data, color=clr, align="center", width=0.5)

# 라인 색 선택
# plt.bar(x_years, y_data, color=clr, align="edge", edgecolor="black", width=3)

# 테두리 라인 설정
# plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, width=0.5)

# plt.xticks(x_years)
# plt.yticks(y_data, y_data)
# plt.yticks(100,200,300,400,500,600,900)

# plt.barh(x_years, y_data)

#   {x축 데이터}{y축 데이터}{색설정} {위치설정} {테두리색설정} {선두께} {그래프 두께}
# plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)

# 막대 문양 채우기

# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="/")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="//")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="///")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="////")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\\\")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="+")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="*")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="o")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="x")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch=".")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="..")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="...")
# plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="....")

# 산점도 그래프
""" x = 1
y = 1

plt.scatter(1, 1)
plt.scatter(x+1, y+1)
plt.scatter(x+1, y-1)
plt.scatter(x+2, y+1)
plt.scatter(x+1, y+2)
plt.scatter(x+2, y+2)
plt.scatter(x+3, y+5)
plt.scatter(x+1, y+4)

# 색상 크기 변경
# plt.scatter(x+1.5 , y+1.5, 100, 2)
# plt.scatter(x+2.5 , y+1.5, 150, 3)
# plt.scatter(x+3.5 , y+1.5, 200, 4)

plt.scatter(x+1.5 , y+1.5, 100, "C1")
plt.scatter(x+2.5 , y+1.5, 150, "red")
plt.scatter(x+3.5 , y+1.5, 200, 4)

# 포인트 설정
#         {x}{y}{포인트크기}{색상설정}{투명}
plt.scatter(x+1.5, y+1.5, 100, "C6", alpha=0.5)

# Color map setting
plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="cividis")
plt.colorbar() """

# plt.show()

# Histogram
# plt.hist({data}, bins={구간수})
import numpy as np

rn = np.random.randint(1,30,size=20)
print(rn)

# plt.hist(rn, bins=10,label="def")


# plt.hist(rn, bins=20)
# STYLE
# 라벨 설정
# plt.hist(rn,  bins=10, label="def") 

# 투명도 설정
# plt.hist(rn,  bins=10, label="def", alpha=0.5)

# 그래프 스타일 설정
# plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="step")
# plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="stepfilled")
# plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="barstacked")

# plt.legend()

#Pie_Chart
rate = [30, 40, 20, 10]
labels = ["Alpha", "Beta", "Gamma", "Delta"]

# plat.pie({data})
# plt.pie(rate)

# Labels
# plt.pie(rate, labels=labels)

#Percetage
# plt.pie(rate, labels=labels, autopct='%.1d%%')
# plt.pie(rate, labels=labels, autopct='%.1f%%')

# StartAngle
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0)
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=30)
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=90)

# Counterclock
#                                                            시계방향으로 시작
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0, counterclock=False)
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0, counterclock=True)
# plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0, counterclock=False)

# 공백
# plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0.5, 0.5, 0.5, 0.5])

# Style
# 사용가능한 스타일 키
# print(plt.style.available)

# plt.style.use("bmh")
# plt.style.use("ggplot")
# plt.style.use("classic")
# plt.style.use("Solarize_Light2")
# plt.style.use("dark_background")
# plt.style.use("fast")

# 패널 사이즈 적용
# plt.rcParams['figure.figsize'] = (6, 3)

# plt.rcParams['font.size'] = 15

# plt.rcParams['lines.linewidth'] = 5

# plt.rcParams['lines.linestyle'] = '--'

# 위 눈금 설정
# plt.rcParams['xtick.top'] = True

# 오른 눈금 설정
# plt.rcParams['ytick.right'] = True

# 안쪽으로 눈금 설정
# plt.rcParams['xtick.direction'] = 'in'
# plt.rcParams['ytick.direction'] = 'in'

# 눈금 길이
# plt.rcParams['ytick.major.size'] = 12

# 세부 눈금
# plt.rcParams['xtick.minor.visible'] = True

# plt.plot([2,3,6,7,10], [1,4,5,8,9])

# 객체 활용
# fig, ax = plt.subplots()

# [left, bottom, width, height]
# ax = fig.add_axes([1, 1, 0, 0])
# ax = fig.add_axes([1, 1, 1, 1])
# ax = fig.add_axes([0, 0, 0, 0])

# plt.show()

# 다중 패널 객체 생성
# fig, ax = plt.subplots(1, 1)
# fig, ax = plt.subplots(1, 2)
# fig, ax = plt.subplots(2, 1)
# fig, ax = plt.subplots(2, 2)
# fig, ax = plt.subplots(4, 4)

# 다중 패널 그래프 출력
# x = [1,4,5,8,9]
# y1 = [2,3,6,7,10]

# fig, ax = plt.subplots(2, 2)

# ax[0][0].plot(x, y1)
# ax[0][1].plot(x, y1)
# ax[1][1].plot(x, y1)
# ax[1][0].plot(x, y1)

# 축 공유
# fig, ax = plt.subplots(2, 2, sharex=True)
# fig, ax = plt.subplots(2, 2, sharey=True)

# 사용 데이터
""" x = [1,4,5,8,9]

y1 = [2,3,6,7,10]
y2 = [10,8,6,4,2]

fig, ax1 = plt.subplots()
ax1.set_xlabel("X-Data")
ax1.set_ylabel("Y1")
ax1.plot(x, y1, color = "blue",label="y1 Data")
ax1.legend(loc="upper right")

ax2 = ax1.twinx()
ax2.set_ylabel("Y2")
ax2.plot(x, y2, color = "red",label="y2 Data")  # label 출력은 legend 있어야 함
ax2.legend(loc="lower right") """


# 이종 그래프 출력
x = [1,4,5,8,9]
y1 = [2,3,6,7,10]
y2 = [2,3,6,7,10]

fig, ax1 = plt.subplots()

ax1.plot(x, y1, "-o", color="C1",label="XData")
ax1.set_xlabel("X")
ax1.set_ylabel("Ydata")

ax2 = ax1.twinx()
ax2.bar(x, y2, color="C2",label="YData")
ax2.set_ylabel("Y2data")

ax1.legend()
ax2.legend()



# plt.tight_layout()
plt.show()