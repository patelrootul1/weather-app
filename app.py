from flask import Flask, render_template, request, redirect, url_for
import joblib
import pandas as pd
import numpy
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler() 
model = joblib.load("rdf_model.pkl")
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        Kitchen_temp = request.form["Kitchen_temp"]
        Kitchen_humidty = request.form["Kitchen_humidty"]
        Livroom_temp = request.form["Livroom_temp"]
        Livroom_humidity = request.form["Livroom_humidity"]
        Laundry_temp = request.form["Laundry_temp"]
        Laundry_humidity = request.form["Laundry_humidity"]
        Office_temp = request.form["Office_temp"]
        Office_humidity = request.form["Office_humidity"]
        Bathroom_temp = request.form["Bathroom_temp"]
        Bathroom_humidity = request.form["Bathroom_humidity"]
        Ironing_temp = request.form["Ironing_temp"]
        Ironing_humidity = request.form["Ironing_humidity"]
        TeenRoom_temp = request.form["TeenRoom_temp"]
        TeenRoom_humidity = request.form["TeenRoom_humidity"]
        ParentRoom_temp = request.form["ParentRoom_temp"]
        ParentRoom_humidity = request.form["ParentRoom_humidity"]
        Outside_temp = request.form["Outside_temp"]
        Outside_humidity = request.form["Outside_humidity"]
        Outside_dewpoint = request.form["Outside_dewpoint"]
        Outside_pressure = request.form["Outside_pressure"]
        Outside_windspeed = request.form["Outside_windspeed"]
        print(Kitchen_temp)
        testinput = [[Kitchen_temp,Livroom_temp,Laundry_temp,Office_temp,Bathroom_temp,Ironing_temp,TeenRoom_temp,Kitchen_humidty,
        Livroom_humidity,Laundry_humidity,Office_humidity,Bathroom_humidity,Outside_humidity,Ironing_humidity,TeenRoom_humidity,ParentRoom_humidity,
        Outside_temp,Outside_dewpoint,Outside_humidity,Outside_pressure,Outside_windspeed]]
        column = ['Kitchen_temp','Livroom_temp','Laundry_temp','Office_temp','Bathroom_temp','Ironing_temp','TeenRoom_temp','Kitchen_humidty',
        'Livroom_humidity','Laundry_humidity','Office_humidity','Bathroom_humidity','Outside_humidity','Ironing_humidity','TeenRoom_humidity','ParentRoom_humidity',
        'Outside_temp','Outside_dewpoint','rh_out','Outside_pressure','Outside_windspeed']
        df = pd.DataFrame(testinput,columns=column)
        
        print(df)

        # std_testinput = scaler.fit_transform(df)
        # print(std_testinput)
        pred = model.predict(testinput)
        # preddf = pd.DataFrame([[pred[0],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],columns=column)
        # inversed = scaler.inverse_transform(preddf)
        print(pred)
        
        return redirect(url_for(".result_fn", data=pred))

    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def result_fn():
    op = request.args['data']
    str1=" "
    for i in op:
        if(i=="["):
            continue
        elif(i=="]"):
            break
        else:
           str1=str1+i
    return render_template('result.html', output=str1)


if __name__ == "__main__":
    app.run(debug=True, port=8000)