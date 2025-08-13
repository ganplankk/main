import os
import csv
import pandas
from numpy.distutils.from_template import list_re

# with open("weather_data.csv", "r") as f:
#     csvfile=f.readlines()
#     for i in range(len(csvfile)):
#         data =

# with open("weather_data.csv", "r") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# total = 0
# data = pandas.read_csv("weather_data.csv")
# data_dic = data.to_dict()
# list_tmp = data["temp"].to_list()
# temp_avg = sum(list_tmp)/len(list_tmp)
# print(temp_avg)
# print(data["temp"].mean())
# print(data.condition)
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp_F = int(monday.temp) * 9 / 5 + 32
# print(monday_temp_F)

## Color 종류 파악
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# fur_colors = data["Primary Fur Color"].dropna().unique()
#
# for color in fur_colors:
#     count = len(data[data["Primary Fur Color"] == color])
#     print(f"{color} cnt : {count}")
gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

df = pandas.DataFrame(data_dic)
df.to_csv("cnt.csv")

# gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
# print(gray_squirrels)



## Color 별 다람쥐 개수 파악
# def cnt (check):
#     gray_chk=0
#     for i in range(len(color)):
#         if(color[0] == "Gray"):
#             gray_chk += 1
#         if(color[i] == "Gray"):
#




