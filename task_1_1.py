duration = 53
print(duration, 'сек')

duration = 153
min_sec = duration // 60
print(min_sec,'мин', duration % 60, 'сек')

duration = 4153
hours_min_sec = duration // 3600
print(hours_min_sec, 'час', duration % 3600 // 60, 'мин', duration % 3600 % 60, 'сек')

duration = 400153
days_hours_min_sec = duration // 86400
print(days_hours_min_sec, 'дн', duration % 86400 // 3600, 'час', duration % 3600 // 60, 'мин', duration % 3600 % 60, 'cек')











