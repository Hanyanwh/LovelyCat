# -*- coding: utf-8 -*-
from datetime import datetime
import calendar
import time
import json
"""
    异步更新
"""


class DataHanding:
    def __init__(self):
        self.date = ""
        self.jsonPath = "update.json"
        self.food_total_weight = 0
        self.water_total_weight = 0
        self.today_current = [None, None, "00:00"]
        self.residue = []                               # 0 剩余食物    1 剩余水
        self.today_data = [
            {"time": "00:00", "food": None, "water": None},
            {"time": "00:30", "food": None, "water": None},
            {"time": "01:00", "food": None, "water": None},
            {"time": "01:30", "food": None, "water": None},
            {"time": "02:00", "food": None, "water": None},
            {"time": "02:30", "food": None, "water": None},
            {"time": "03:00", "food": None, "water": None},
            {"time": "03:30", "food": None, "water": None},
            {"time": "04:00", "food": None, "water": None},
            {"time": "04:30", "food": None, "water": None},
            {"time": "05:00", "food": None, "water": None},
            {"time": "05:30", "food": None, "water": None},
            {"time": "06:00", "food": None, "water": None},
            {"time": "06:30", "food": None, "water": None},
            {"time": "07:00", "food": None, "water": None},
            {"time": "07:30", "food": None, "water": None},
            {"time": "08:00", "food": None, "water": None},
            {"time": "08:30", "food": None, "water": None},
            {"time": "09:00", "food": None, "water": None},
            {"time": "09:30", "food": None, "water": None},
            {"time": "10:00", "food": None, "water": None},
            {"time": "10:30", "food": None, "water": None},
            {"time": "11:00", "food": None, "water": None},
            {"time": "11:30", "food": None, "water": None},
            {"time": "12:00", "food": None, "water": None},
            {"time": "12:30", "food": None, "water": None},
            {"time": "13:00", "food": None, "water": None},
            {"time": "13:30", "food": None, "water": None},
            {"time": "14:00", "food": None, "water": None},
            {"time": "14:30", "food": None, "water": None},
            {"time": "15:00", "food": None, "water": None},
            {"time": "15:30", "food": None, "water": None},
            {"time": "16:00", "food": None, "water": None},
            {"time": "16:30", "food": None, "water": None},
            {"time": "17:00", "food": None, "water": None},
            {"time": "17:30", "food": None, "water": None},
            {"time": "18:00", "food": None, "water": None},
            {"time": "18:30", "food": None, "water": None},
            {"time": "19:00", "food": None, "water": None},
            {"time": "19:30", "food": None, "water": None},
            {"time": "20:00", "food": None, "water": None},
            {"time": "20:30", "food": None, "water": None},
            {"time": "21:00", "food": None, "water": None},
            {"time": "21:30", "food": None, "water": None},
            {"time": "22:00", "food": None, "water": None},
            {"time": "22:30", "food": None, "water": None},
            {"time": "23:00", "food": None, "water": None},
            {"time": "23:30", "food": None, "water": None}
        ]
        self.week_data = [
            {"x": "周一", "food": None, "water": None},
            {"x": "周二", "food": None, "water": None},
            {"x": "周三", "food": None, "water": None},
            {"x": "周四", "food": None, "water": None},
            {"x": "周五", "food": None, "water": None},
            {"x": "周六", "food": None, "water": None},
            {"x": "周日", "food": None, "water": None}
        ]
        self.month_data = [
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
        self.init()

    def init(self):
        self.food_total_weight = 50             # 临时赋值，对付bug
        self.water_total_weight = 50            # 临时赋值，对付bug
        self.today_current = [None, None, "00:00"]
        self.residue = [100, 100]
        self.date = datetime.today().strftime("%Y-%m-%d")
        with open(self.jsonPath, 'w') as json_file:
            data = {}
            data.update({"food_residue": self.residue[0], "water_residue": self.residue[1],
                         "food_total": self.food_total_weight, "water_total": self.water_total_weight,
                         "today_data": self.today_data, "week_data": self.week_data, "month_data": self.month_data})
            json_file.write(json.dumps(data))

    def init_today(self):

        data = self.load()
        with open(self.jsonPath, 'w') as json_file:
            data["food_residue"] = self.residue[0]
            data["water_residue"] = self.residue[1]
            data["food_total"] = self.food_total_weight
            data["water_total"] = self.water_total_weight

            data["today_data"] = self.today_data
            json_file.write(json.dumps(data))

        today_date = datetime.today().date()
        if today_date.day == 1:
            self.init_month(data)
        elif today_date.weekday() == 0:
            self.init_week(data)

    def init_week(self, data):

        with open(self.jsonPath, 'w') as json_file:
            data["week_data"] = self.week_data
            json_file.write(json.dumps(data))

    def init_month(self, data):

        date = datetime.today().date()
        year = date.year
        month = date.month
        for i in range(1, 32):
            month_date = datetime.strptime(str(year)+"-"+str(month)+"-"+str(i), "%Y-%m-%d")
            self.month_data[i]["period"] = month_date.strftime("%Y-%m-%d")

        with open(self.jsonPath, 'w') as json_file:
            _, day = calendar.monthrange(year, month)
            data["month_data"] = self.month_data[0: day]
            json_file.write(json.dumps(data))

    def set_food_data(self, weight, current_weight, time_now):
        self.food_total_weight += weight
        self.residue[0] = current_weight
        if time_now == self.today_current[2]:
            self.today_current[0] += weight
        else:
            self.today_current[0] = weight
            self.today_current[2] = time_now
        self.write_json("today")

    def set_water_data(self, weight, current_weight, time_now):
        self.water_total_weight += weight
        self.residue[1] = current_weight
        if time_now == self.today_current:
            self.today_current[1] += weight
        else:
            self.today_current[1] = weight
            self.today_current[2] = time_now
        self.write_json("today")

    def set_week_month_chart(self):
        self.write_json("week_month")

    def write_json(self, flag):
        data = self.load()
        with open(self.jsonPath, 'w') as json_file:
            if flag == "today":
                data["food_residue"] = self.residue[0]
                data["water_residue"] = self.residue[1]
                data["food_total"] = self.food_total_weight
                data["water_total"] = self.water_total_weight

                today_index = self.time_mapping(self.today_current[2])
                data["today_data"][today_index]["food"] = self.today_current[0]
                data["today_data"][today_index]["water"] = self.today_current[1]
                json_file.write(json.dumps(data))
            else:
                week_index = datetime.strptime(self.date, "%Y-%m-%d").weekday()
                data["week_data"][week_index]["food"] = self.food_total_weight
                data["week_data"][week_index]["water"] = self.water_total_weight

                month_index = datetime.strptime(self.date, "%Y-%m-%d").day - 1
                data["month_data"][month_index]["food"] = self.food_total_weight
                data["month_data"][month_index]["water"] = self.water_total_weight
                json_file.write(json.dumps(data))

    def load(self):
        with open(self.jsonPath) as json_file:
            data = json.load(json_file)
            return data

    def time_mapping(self, time_data):
        hm = "%H:%M"
        time_object = time.strptime(time_data, hm)
        hour = time_object[3]
        minute = time_object[4]
        index = 2 * hour + (minute >= 30)
        return index
