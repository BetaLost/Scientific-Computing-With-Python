def add_time(start, duration, day=None):
  week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  current_day = 0
  days_passed = 0
  
  if day != None:
    current_day = week_days.index(day.lower().capitalize())

  start_array = start.split()
  start_hours, start_minutes = start_array[0].split(":")

  start_hours = int(start_hours)
  start_minutes = int(start_minutes)
  
  period = start_array[1]

  add_hours, add_minutes = duration.split(":")

  add_hours = int(add_hours)
  add_minutes = int(add_minutes)
  
  while add_hours > 24:
    if days_passed == 0:
        days_passed = 1
    
    add_hours -= 24
    days_passed += 1

  new_hours = start_hours + add_hours
  new_minutes = start_minutes + add_minutes
  new_time = ""

  while new_minutes > 59:
    new_minutes -= 60
    new_hours += 1

  while new_hours > 24:
    new_hours -= 24
    days_passed += 1

  if new_hours > 12:
      new_hours -= 12
      
      if period == "PM":
        period = "AM"
        if days_passed == 0:
            days_passed += 1
      else:
          period = "PM"
          
  elif new_hours == 12:
      if period == "PM":
        days_passed += 1
        period = "AM"
      else:
          period = "PM"
      

  new_time = f"{new_hours}:{new_minutes:02} {period}"
  
  if day != None:
      temp_day = current_day + days_passed
      while temp_day >= 7:
          temp_day -= 7
          
      new_time += f", {week_days[temp_day]}"
  
  if days_passed == 1:
      new_time += " (next day)"
  elif days_passed > 1:
      new_time += f" ({days_passed} days later)"
      
  return new_time
