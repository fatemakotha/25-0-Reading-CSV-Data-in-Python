
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# fur_list_series = data["Primary Fur Color"].to_list
# print(fur_list_series)

grey_squirrel_count = len(data["Primary Fur Color"] == "Gray")
red_squirrel_count = len(data["Primary Fur Color"] == "Cinnamon")
black_squirrel_count = len(data["Primary Fur Color"] == "Black")
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}
print(data_dict) #prints: {'Fur Color': ['Gray', 'Cinnamon', 'Black'], 'Count': [3023, 3023, 3023]}