def add_time(start, duration, testday=''):
  day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

  start = start.split(':')
  duration = duration.split(':')

  shour = int(start[0])
  a = start[1].split(' ')
  AM=a[1]
  smin = int(a[0])

  if 'PM' in AM:
    shour = shour + 12

  ahour = int(duration[0])
  amin = int(duration[1])

  ehour = shour + ahour
  emin = smin + amin

  if (emin) >= 60:
    emin -= 60
    ehour +=  1

  days = int((ehour)/24)
  weeks = int(days/7)
  ehour = ehour - 24*days

  if ehour > 12:
    ehour=ehour-12
    AM = 'PM'
  elif ehour == 12 and shour != 12 and shour != 24:
    if AM =='PM':
      AM = 'AM'
    else:
      AM = 'PM'
  else:
    AM = 'AM'
    if ehour == 0:
      ehour = 12

  if testday !='': 
    if testday.lower() in day:
      sday = day.index(testday.lower())
      weekday=(days-7*weeks)+sday
      if weekday == 7:
        weekday = 0
      if weekday > 6:
        weekday = weekday - 6
      eday = f" {day[weekday]}"
    else:
      eday = ''

  if days == 1:
    days = ' (next day)'
  elif days > 1:
    days = (f" ({str(days)} days later)")
  else:
    days = ''

  if testday != '':
    new_time = (f"{str(ehour)}:{str(emin).zfill(2)} {AM},{eday.title()}{days}")
  else:
    new_time = (f"{str(ehour)}:{str(emin).zfill(2)} {AM}{days}")
  return new_time