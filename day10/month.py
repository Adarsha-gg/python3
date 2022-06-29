def is_leap(yer):
  if yer % 4 == 0:
    if yer % 100 == 0:
      if yer % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(yr,mon):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if(mon < 1 and mon > 12):
    return "Invalid"
  if(mon == 2 and g == True):
    return f"29 days"
  else:    
    return f"{month_days[mon-1]} days"  

  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
g =is_leap(year)
days = days_in_month(year, month)
print(days)












