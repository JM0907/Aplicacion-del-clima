from flask import Flask,render_template
import requests
from dotenv import load_dotenv,dotenv_values
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped,mapped_column 



config = dotenv_values('.env')
app=Flask(__name__)
app.cong["SQLALCHEMY_DATABASE_URI"] = "sqlite:///weather.sqlite"

db = SQLAlchemy(app)

class City(db.Model):
    id: Mapped [int]= mapped_column(db.Integer, primary_key=True, autoincrement=True)
    name: Mapped [str] = mapped_column(db.String, unique=True, nullable=False)
with app.app_context():
    db.create_all()

app = Flask (__name__)


def get_weather_data (city):
    API_KEY = config['API_KEY']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang&appid={API_KEY}'
    r = requests.get(url).json()
    print(r)
    return r


@app.route('/clima', methods=['GET', 'POST'])
def clima():
    if request.method == 'POST':
        new_city = requests.form.get('city') 
        if new_city:
            obj=city(name=new_city)
            db.session.add(obj)
            db.session.commit()

for city in cities:
    r=get_weather_data(city.name)


    clima=get_weather_data('london')
    temperatura=str(clima['main']['temp'])
    descripcion= str(clima['weather'][0]['description'])
    icono=str(clima['weather'][0]['icon'])
    r_json={
        'ciudad': 'london',
        'temperatura':temperatura,
        'descripcion': descripcion,
        'icono': icono
        }
    return render_template('weather.html', clima = r_json)
   



@app.route('/about')
def hello_CV():
    return render_template('CV.html')


if __name__ == '__main__':
    app.run(debug = True)

@app.route('/clima')
def clima_page():
    return render_template('resultado.json')

@app.route('/clima')
def clima():
    return 'CLIMA'

if __name__ == '__main__':
    app.run(debug = True)

































































































































































































































































































































































































































