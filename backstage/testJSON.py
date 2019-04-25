# -*- coding: utf-8 -*-
import random
import json
today = [
            {"time": "00:00", "food": 10, "water": 30},
            {"time": "00:30", "food": 40, "water": None},
            {"time": "01:00", "food": None, "water": None},
            {"time": "01:30", "food": None, "water": None},
            {"time": "02:00", "food": None, "water": 50},
            {"time": "02:30", "food": None, "water": None},
            {"time": "03:00", "food": 10, "water": None},
            {"time": "03:30", "food": None, "water": 13},
            {"time": "04:00", "food": None, "water": None},
            {"time": "04:30", "food": None, "water": None},
            {"time": "05:00", "food": None, "water": None},
            {"time": "05:30", "food": 70, "water": None},
            {"time": "06:00", "food": None, "water": None},
            {"time": "06:30", "food": None, "water": None},
            {"time": "07:00", "food": None, "water": 50},
            {"time": "07:30", "food": None, "water": None},
            {"time": "08:00", "food": None, "water": None},
            {"time": "08:30", "food": 20, "water": None},
            {"time": "09:00", "food": None, "water": 40},
            {"time": "09:30", "food": None, "water": None},
            {"time": "10:00", "food": None, "water": None},
            {"time": "10:30", "food": None, "water": None},
            {"time": "11:00", "food": 45, "water": None},
            {"time": "11:30", "food": None, "water": None},
            {"time": "12:00", "food": None, "water": None},
            {"time": "12:30", "food": None, "water": 89},
            {"time": "13:00", "food": None, "water": None},
            {"time": "13:30", "food": None, "water": None},
            {"time": "14:00", "food": None, "water": None},
            {"time": "14:30", "food": None, "water": None},
            {"time": "15:00", "food": None, "water": 10},
            {"time": "15:30", "food": 78, "water": None},
            {"time": "16:00", "food": None, "water": None},
            {"time": "16:30", "food": None, "water": None},
            {"time": "17:00", "food": None, "water": None},
            {"time": "17:30", "food": 22, "water": None},
            {"time": "18:00", "food": None, "water": None},
            {"time": "18:30", "food": None, "water": 7},
            {"time": "19:00", "food": None, "water": None},
            {"time": "19:30", "food": None, "water": None},
            {"time": "20:00", "food": 44, "water": None},
            {"time": "20:30", "food": None, "water": None},
            {"time": "21:00", "food": None, "water": 20},
            {"time": "21:30", "food": 16, "water": None},
            {"time": "22:00", "food": None, "water": None},
            {"time": "22:30", "food": None, "water": 60},
            {"time": "23:00", "food": None, "water": None},
            {"time": "23:30", "food": 9, "water": None}
        ]

week = [
            {"x": "周一", "food": 30, "water": 60},
            {"x": "周二", "food": 50, "water": 50},
            {"x": "周三", "food": 10, "water": 100},
            {"x": "周四", "food": 30, "water": 90},
            {"x": "周五", "food": 20, "water": 10},
            {"x": "周六", "food": 63, "water": 13},
            {"x": "周日", "food": 17, "water": 57}
        ]

month = [
            {"period": "2019-04-01", "food": None, "water": None},
            {"period": "2019-04-02", "food": None, "water": None},
            {"period": "2019-04-03", "food": None, "water": None},
            {"period": "2019-04-04", "food": None, "water": None},
            {"period": "2019-04-05", "food": None, "water": None},
            {"period": "2019-04-06", "food": None, "water": None},
            {"period": "2019-04-07", "food": None, "water": None},
            {"period": "2019-04-08", "food": None, "water": None},
            {"period": "2019-04-09", "food": None, "water": None},
            {"period": "2019-04-10", "food": None, "water": None},
            {"period": "2019-04-11", "food": None, "water": None},
            {"period": "2019-04-12", "food": None, "water": None},
            {"period": "2019-04-13", "food": None, "water": None},
            {"period": "2019-04-14", "food": None, "water": None},
            {"period": "2019-04-15", "food": None, "water": None},
            {"period": "2019-04-16", "food": None, "water": None},
            {"period": "2019-04-17", "food": None, "water": None},
            {"period": "2019-04-18", "food": None, "water": None},
            {"period": "2019-04-19", "food": None, "water": None},
            {"period": "2019-04-20", "food": None, "water": None},
            {"period": "2019-04-21", "food": None, "water": None},
            {"period": "2019-04-22", "food": None, "water": None},
            {"period": "2019-04-23", "food": None, "water": None},
            {"period": "2019-04-24", "food": None, "water": None},
            {"period": "2019-04-25", "food": None, "water": None},
            {"period": "2019-04-26", "food": None, "water": None},
            {"period": "2019-04-27", "food": None, "water": None},
            {"period": "2019-04-28", "food": None, "water": None},
            {"period": "2019-04-29", "food": None, "water": None},
            {"period": "2019-04-30", "food": None, "water": None},
            {"period": "2019-04-31", "food": None, "water": None}
        ]

for i in range(len(month)):
    month[i]["food"] = int(random.random()*100)
    month[i]["water"] = int(random.random() * 100)

food_total_weight = 50             # 临时赋值，对付bug
water_total_weight = 50            # 临时赋值，对付bug
today_current = [None, None, "00:00"]
residue = [100, 100]
with open("update.json", 'w') as json_file:
    data = {}
    data.update({"food_residue": residue[0], "water_residue": residue[1],
                 "food_total": food_total_weight, "water_total": water_total_weight,
                 "today_data": today, "week_data": week, "month_data": month})
    json_file.write(json.dumps(data))
