"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import Flask
import urllib.request as request
import json

app = Flask(__name__)

@app.route('/')
def safety(): 
  dictionary={}

  key = "f739f2d3948eea92"
  fileName = "http://api.wunderground.com/api/f739f2d3948eea92/geolookup/conditions/q/NC/Cary.json"
  f = request.urlopen(fileName)
  json_string = f.read().decode('utf-8')
  print(json_string)
  parsed_json = json.loads(json_string)
  dictionary['location'] = parsed_json['location']['city']
  dictionary['temp'] = parsed_json['current_observation']['temp_f']
  dictionary['tempc'] = parsed_json['current_observation']['temp_c']
  dictionary['hum']= parsed_json['current_observation']['relative_humidity']
  dictionary['wind']= parsed_json['current_observation']['wind_mph']
  temp=dictionary['temp']
  hum_num=int(dictionary['hum'].strip('%'))
  wind=dictionary['wind']
  tempc=dictionary['tempc']
  if temp>40:
    if temp> 100 or (temp> 90 and hum_num>55):
      dictionary['message'] = "TOO HOT!! DO NOT GO OUTSIDE!!!!"
      dictionary['messagespanish'] = "¡Demasiado mucho caliente! No conseguido fuera!!!!"
      dictionary['image']="hot.jpg" 
    elif 40< temp<= 84 or (84 <= temp <90 and hum_num<65.1):
       dictionary['message'] ="Have fun outside!!"
       dictionary['image']="gooutside.jpg"  
       dictionary['messagespanish'] = "Divertirse fuera!!"
    else: 
      dictionary['message'] ="Caution: Only go outside for 10 minutes!!!"
      dictionary['image']="caution.jpg"  
      dictionary['messagespanish'] = "¡Precaución: debemos jugar fuera de sólo 10 minutoss!!!"
  else:
    if temp< 10 or (10<=temp<= 20 and wind>5):
       dictionary['message'] = "TOO COLD DO NOT GO OUTSIDE!!!!"
       dictionary['image']="tocold.jpg" 
       dictionary['messagespanish'] = "¡Demasiado mucho frío! No conseguido fuera!!!!"
      
    elif 40<=temp<45 and wind<=15:
       dictionary['message'] ="Have fun outside!!"
       dictionary['image']="gooutside.jpg" 
       dictionary['messagespanish'] = "Divertirse fuera!!" 
    else: 
       dictionary['message'] = "Caution: Only go outside for 10 minutes!!!"  
       dictionary['image']="coldwarning.jpg" 
       dictionary['messagespanish'] = "¡Precaución: debemos jugar fuera de sólo 10 minutoss!!!"
  return render_template("index.html", weather=dictionary) 
if __name__=="__main__":
   app.run(debug=True)

@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
