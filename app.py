from flask import Flask, render_template, request, jsonify
import os
import requests
from datetime import datetime, timedelta, time
import pytz

app = Flask(__name__)

# Route for "/" (frontend):
@app.route('/')
def index():
  return render_template("index.html")


# Route for "/weather" (middleware):
@app.route('/weather', methods=["POST"])
def POST_weather():
  course = request.form["course"]
  course = course.replace(" ","")
  sub = course[:2].upper()
  num = course[2:]
  result = requests.get(f'http://127.0.0.1:24000/{sub}/{num}/')
  if result.status_code != 200:
    res_list = result.json()
    report = {"course": f"{sub} {num}"}
    error = res_list["error"]
    report["error"] = f"{error}"
    return jsonify(report), 400
  met_weekday = list(result.json()["Days of Week"])
  met_hour, met_min = result.json()["Start Time"].split(":")
  if met_hour != "12" and met_min.split(" ")[1] == "PM":
    met_hour = int(met_hour) + 12
  met_min = met_min.split(" ")[0]
  weekday_dic = {'M':0, 'T':1, 'W':2, 'R':3, 'F':4}
  cour_weekday = []
  for i in range(len(met_weekday)):
    cour_weekday.append(weekday_dic.get(met_weekday[i]))
  dt1 = datetime.now(pytz.timezone('America/Chicago'))
  today_weekday = dt1.weekday()
  today_hour = dt1.hour
  print(dt1,today_weekday, dt1.hour)
  day_diff = -1
  for j in range(len(cour_weekday)):
    if today_weekday <= cour_weekday[j] :
      day_diff = cour_weekday[j] - today_weekday
      break
  if day_diff < 0:
    for a in range(len(cour_weekday)):
      if today_weekday < (cour_weekday[a]+7) :
        day_diff = (cour_weekday[a]+7) - today_weekday
        break
  elif day_diff == 0 and today_hour > int(met_hour):
    for a in range(len(cour_weekday)):
      if today_weekday < (cour_weekday[a]+7) :
        day_diff = (cour_weekday[a]+7) - today_weekday
        break
  hour_diff = -1
  if today_hour <= int(met_hour):
    hour_diff = int(met_hour) - today_hour
  else:
    hour_diff = int(met_hour) + 24 - today_hour
    day_diff = day_diff - 1
  print(day_diff, hour_diff)
  total_diff = day_diff * 24 + hour_diff
  dt2 = dt1 + timedelta(days=day_diff, hours=hour_diff)
  print(total_diff)
  print(dt2)
  wea_fore = requests.get('https://api.weather.gov/points/40.1125,-88.2284')
  wea_link = wea_fore.json()["properties"]["forecastHourly"]
  wea_report = requests.get(wea_link)
  if total_diff <= 144:
    temperature = wea_report.json()["properties"]["periods"][total_diff]["temperature"]
    temperature = int(temperature)
    forecast = wea_report.json()["properties"]["periods"][total_diff]["shortForecast"]
    fore_time = wea_report.json()["properties"]["periods"][total_diff]["startTime"][:19].replace("T"," ")
    print(fore_time)
  else:
    temperature = "forecast unavailable"
    forecast = "forecast unavailable"
    fore_time = f"{dt2.date()} {dt2.hour}:00:00"
  report = {"course": f"{sub} {num}"}
  report["nextCourseMeeting"] = f"{dt2.date()} {dt2.hour}:{met_min}:00"
  report["forecastTime"] = f"{fore_time}"
  report["temperature"] = temperature
  report["shortForecast"] = f"{forecast}"
  print(report)
  status_code = 200
  return jsonify(report), status_code
  


