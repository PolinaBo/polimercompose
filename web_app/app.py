import pickle
import tensorflow as tf
import flask
from flask import Flask, request, render_template
import numpy as np

app = flask. Flask (__name__, template_folder = 'templates')

def prediction(params):
    model = tf.keras.models.load_model('bestNN3')
    pred = model.predict([params])
    return pred

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def predict():
    result=0
    if request.method == 'POST':
        params = []
        for i in range (1, 13):
            param = request.form.get(f'{i}')
            params.append(param)
        params = [float(i) for i in params]

        result = prediction(params)
    return render_template('main.html', result=result)



if __name__ == '__main__':
    app.run()
