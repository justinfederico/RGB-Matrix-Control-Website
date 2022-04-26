from flask import Flask, render_template, request, url_for
import flask_mqtt
from datetime import datetime

app = Flask(__name__)
# app.config['MQTT_BROKER_URL'] = 'mybroker.com'
# app.config['MQTT_BROKER_PORT'] = 1883
# app.config['MQTT_USERNAME'] = 'user'
# app.config['MQTT_PASSWORD'] = 'secret'
# app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
#mqtt = flask_mqtt.Mqtt(app)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
