
# import pandas

# data = pandas.read_csv("D:\Code\python\day25\weather-data.csv")

# monday = data[data.day == "Monday"]
# print(int(monday.temp) * 1.8 + 32)



import pandas

data = pandas.read_csv("D:\Code\python\day25\squirrel.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

sq_dict ={
    "Fur_Color": ["Gray", "Cinnamon", "Black"],
    "Count":  [gray, red, black]
}

df = pandas.DataFrame(sq_dict)
df.to_csv("squirel_count.csv")
