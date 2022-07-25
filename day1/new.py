age=input("What is your current age?\n")
dead=input("How long do u wish to live?")
yr=int(dead)-int(age)
day=yr*365
week=yr*52
month=yr*12
print(f"You have {day} days, {week} weeks and {month} months left to live.")
