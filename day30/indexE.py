# height = float(input("Enter the height:"))
# weight = float(input("Enter the weight:"))

# bmi = weight/height ** 2
# print(bmi)

# if height > 3:
#     raise ValueError("This is abnormal human height")

fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")
    


make_pie(4)


