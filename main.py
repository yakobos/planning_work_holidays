from datetime import date, timedelta


start_year = 2023
end_year = start_year + 1


great_feasts_fixed = { "Nativity of the Theotokos":     date(start_year,  9,  8),
                       "Elevation of the Holy Cross":   date(start_year,  9, 14),
                       "Presentation of the Theotokos": date(start_year, 11, 21),
                       "Nativity of Christ":            date(start_year, 12, 25),
                       "Theophany":                     date(end_year,    1,  6),
                       "Presentation of Christ":        date(end_year,    2,  2),
                       "The Annunciation":              date(end_year,    3, 25),
                       "The Transfiguration":           date(end_year,    8,  6),
                       "The Dormition":                 date(end_year,    8, 15) }


pascha = date(end_year, 5, 5)
great_feasts_moveable = { "Pascha":                  pascha,
                          "Palm Sunday":             pascha - timedelta(7),
                          "The Ascension of Christ": pascha + timedelta(39),
                          "Pentecost":               pascha + timedelta(49) }


num_weekend_feasts = 0
for i, j in great_feasts_fixed.items():
    if j.weekday() >= 5:
        num_weekend_feasts += 1
        
for x, y in great_feasts_moveable.items():
    if y.weekday() >= 5:
        num_weekend_feasts += 1


print("The number of Great Feasts including Pascha is:        ", "13")
print("The number of Great Feasts that fall on the weekend is:", num_weekend_feasts)
print("The number of Great Feasts to plan work around is:     ", 13-num_weekend_feasts)
