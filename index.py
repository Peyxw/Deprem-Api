import re
import json
import time
import threading
import schedule
from urllib.request import urlopen
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from flask import Flask, make_response, request
import random

afadData = []
kandilliData = []


def kandilli():
    array = []
    data = urlopen('http://www.koeri.boun.edu.tr/scripts/sondepremler.asp').read()
    soup = BeautifulSoup(data, 'html.parser')
    data = soup.find_all('pre')
    data = str(data).strip().split('--------------')[2]
    id = random.random()
   

    data = data.split('\n')
    data.pop(0)
    data.pop()
    data.pop()
    for index in range(len(data)):
        element = str(data[index].rstrip())
        element = re.sub(r'\s\s\s', ' ', element)
        element = re.sub(r'\s\s\s\s', ' ', element)
        element = re.sub(r'\s\s', ' ', element)
        element = re.sub(r'\s\s', ' ', element)
        Args=element.split(' ')
        location = Args[8]+element.split(Args[8])[len(element.split(Args[8])) - 1].split('İlksel')[0].split('REVIZE')[0]
        json_data = json.dumps({
            "features" : {
            "type" : "Feature",
            "properties": {
            "mag" :  {
                "md": float(Args[5].replace('-.-', '0')),
                "ml": float(Args[6].replace('-.-', '0')),
                "mw": float(Args[7].replace('-.-', '0')) 
            },
            "place": (float(Args[4]), location.strip()),
            "time" : int(datetime.strptime(Args[0]+" "+Args[1], "%Y.%m.%d %H:%M:%S").timestamp()),
            "updated" : int(datetime.strptime(Args[0]+" "+Args[1], "%Y.%m.%d %H:%M:%S").timestamp()),
            "tz" : "null",
            "url" : "null",
            "detail": "null",
            "felt" : "null",
            "cdi" : "null",
            "mmi" : "null",
            "alert" : "null",
            "status" : element.split(location)[1].split()[0],
            "tsunami" : "0",
            "sig" : "0",
            "net" : "us",
            "code" : id,
            "ids": id,
            "sources" : ",us,",
            "types" : ",origin,phase-data,",
            "nst" : "0",
            "dmin" : "0",
            "rms" : "0",
            "gap" : "0",
            "magType" : "mb",
            "type" : "earthquake",

            "title" : (float(Args[4]), location.strip())

            },
            "geometry" : element.split(location)[1].split()[0],

            "coordinates" : (float(Args[2]), float(Args[3]), float(Args[4])),
            "id": id
            
           
            }
        }, sort_keys=False)

        array.append(json.loads(json_data))
    return array



def afad():
    array = []
    data = urlopen('https://deprem.afad.gov.tr/last-earthquakes.html').read()
    soup = BeautifulSoup(data, 'html.parser')
    data = soup.find_all('tr')
    id = random.random()
    data.pop(0)
    for i in range(len(data)):
        earthquakeType = data[i].find_all('td')[4].text
        json_data = json.dumps({
            
            
            "properties": {
            "mag": {
                "md": float(data[i].find_all('td')[5].text) if earthquakeType == "MD" else  0,
                "ml": float(data[i].find_all('td')[5].text) if earthquakeType == "ML" else 0,
                "mw": float(data[i].find_all('td')[5].text) if earthquakeType == "MW" else 0
            },
            "place" : (float(data[i].find_all('td')[3].text),data[i].find_all('td')[6].text),
            "time" : int(datetime.strptime(data[i].find_all('td')[0].text, "%Y-%m-%d %H:%M:%S").timestamp()),
            "updated" : int(datetime.strptime(data[i].find_all('td')[0].text, "%Y-%m-%d %H:%M:%S").timestamp()),
            "tz" : "null",
            "url" : "null",
            "detail": "null",
            "felt" : "null",
            "cdi" : "null",
            "mmi" : "null",
            "alert" : "null",
            "status" : earthquakeType,
            "tsunami" : "0",
            "sig" : "0",
            "net" : "us",
            "code" :id,
            "ids": id,
            "sources" : ",us,",
            "types" : ",origin,phase-data,",
            "nst" : "0",
            "dmin" : "0",
            "rms" : "0",
            "gap" : "0",
            "magType" : "mb",
            "type" : "earthquake",
            "title" : (float(data[i].find_all('td')[3].text),data[i].find_all('td')[6].text)
            },
            "geometry" : earthquakeType,
            "coordinates" : (float(data[i].find_all('td')[1].text),float(data[i].find_all('td')[2].text),float(data[i].find_all('td')[3].text)),
            "id" : id
            
        }, sort_keys=False)

        array.append(json.loads(json_data))
    return array


def filterbylocation(location,data):
    return list(filter(lambda i: location.upper() in i['location'], data))


def filterbysize(size,data):
    return list(filter(lambda i: float(size) <= float(i['size']['ml']), data))


def filterbysizeandlocation(size,location,data):
    return list(filter(lambda i: float(size) <= float(i['size']['ml']) and location.upper() in i['location'], data))

def filterbytime(hour, data):
    now = datetime.now()
    return [record for record in data if (now - datetime.strptime(record['date'], "%Y.%m.%d %H:%M:%S")) <= timedelta(hours=hour)]

def filterbysizeandtime(size, hour, data):
    filtered_by_time = filterbytime(hour, data)
    filtered_by_size = filterbysize(size, filtered_by_time)
    return filtered_by_size

def filterbysizeandtimeandlocation(size, hour, location, data):
    filtered_by_time = filterbytime(hour, data)
    filtered_by_size = filterbysize(size, filtered_by_time)
    filtered_by_location = filterbylocation(location, filtered_by_size)
    return filtered_by_location

def Data(
    type='kandilli',
):
    if type == 'afad':
        return afadData
    else:
       return kandilliData


def job():
    global afadData
    global kandilliData
    afadData = afad()
    kandilliData = kandilli()

job()
schedule.every(5).minutes.do(job)

def thread_function():
    while True:
        schedule.run_pending()
        time.sleep(1)

x = threading.Thread(target=thread_function)
x.start()





app = Flask(__name__)

@app.route('/')
def index():
    source_type = request.args.get('type') if request.args.get('type') is not None else 'kandilli'
    data = Data(type=source_type)
    location = request.args.get('location')
    size = request.args.get('size')

    if location is not None and size is not None:
        data = filterbysizeandlocation(size,location,data)
    elif location is not None:
        data = filterbylocation(location, data)
    elif size is not None and size.isnumeric():
        data = filterbysize(size,data)
    number_of_elements = len(data)
    print(number_of_elements)
    json_data = json.dumps({ 
         "type" :
         "FeatureCollection" ,
         "metadata": {
               "generated" : "null",
               "url" : "null" , 
               "title" : "PEYXW DEPREM",
               "status" : number_of_elements,
               "api" : "1.0.0",
               "count":  number_of_elements
               
            },
         "features": data  
        }, sort_keys=False)
        
       
    res = make_response(json_data)
    res.headers['Content-Type'] = 'application/json'
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

if __name__ == '__main__':
     app.run(debug=True)
