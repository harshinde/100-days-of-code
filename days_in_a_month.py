def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year.")
        return True
      else:
        print("Not leap year.")
        return False
    else:
      print("Leap year.")
      return True
  else:
    print("Not leap year.")
    return False

def days_in_month(yr_value, m_value):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  leap_yr = is_leap(yr_value)

  if leap_yr == True and m_value == 1:
    return 29
  else:
    return month_days[m_value]


    

      
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
