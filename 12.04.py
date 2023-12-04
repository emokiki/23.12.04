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
x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["r", "lime", "b"]

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

plt.barh(x_years, y_data)

#   {x축 데이터}{y축 데이터}{색설정} {위치설정} {테두리색설정} {선두께} {그래프 두께}
plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)

plt.show()