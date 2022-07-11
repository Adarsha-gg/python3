from prettytable import PrettyTable
x = PrettyTable()

x.field_names = ["Pokemon", "Type"]
x.add_rows(
    [
        ["Pikachu", "Elec"],
        ["ratta", "normal"],

    ]
)
x.align = "l"
print(x)