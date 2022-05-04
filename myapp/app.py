from flask import Flask, render_template, request, url_for, redirect
import paho.mqtt.client as mqtt

app = Flask(__name__)


# app.config['MQTT_BROKER_URL'] = 'broker.emqx.io'
# app.config['MQTT_BROKER_PORT'] = 1883
# app.config['MQTT_USERNAME'] = ''
# app.config['MQTT_PASSWORD'] = ''
# app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
# # Parameters for SSL enabled
#
# # app.config['MQTT_TLS_ENABLED'] = True
# # app.config['MQTT_TLS_INSECURE'] = True
# # app.config['MQTT_TLS_CA_CERTS'] = 'broker.emqx.io-ca.crt'


@app.route("/", methods=['GET', 'POST'])
def index():
    def on_connect(client, userdata, flags, rc):
        client.subscribe(topic)
        print('connected')

    def on_message(client, userdata, msg):
        print("message received")
    topic = '/raspberrypi/matrix/links'
    port = 1883
    client = mqtt.Client()
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('broker.emqx.io', port, 60)
    client.loop_start()


    if request.method == "POST":
        image = request.form.get("image")
        control = 0
        control = image.find(".gif")
        if control == -1:
            imagePi = 'I:' + image
            print("image got")
            client.publish(topic, imagePi)

        else:
            imagePi = 'G:' + image
            print("gif got")
            client.publish(topic, imagePi)

    return render_template('index.html')


# @mqtt.on_connect()
# def handle_connect(client, userdata, flags, rc):
#     print("connected!")
#     mqtt.subscribe('/raspberrypi/matrix/links')
#     mqtt.publish('/raspberrypi/matrix/links', 'I:https://art.pixilart.com/79dcbd564094d2e.png')
#
#
# # @socketio.on('publish')
# # def handle_publish(imagePi):
# #     mqtt.publish('/raspberrypi/matrix/links', imagePi)
#
#
# # @socketio.on('subscribe')
# # def handle_subscribe():
# #     mqtt.subscribe('/raspberrypi/matrix/links')
# #
# #
# # @socketio.on('unsubscribe_all')
# # def handle_unsubscribe_all():
# #     mqtt.unsubscribe_all()
#
#
# @mqtt.on_message()
# def handle_mqtt_message(client, userdata, message):
#     data = dict(
#         topic=message.topic,
#         payload=message.payload.decode()
#     )
#     socketio.emit('mqtt_message', data=data)


if __name__ == "__main__":

    app.run(host='0.0.0.0')
