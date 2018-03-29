import paho.mqtt.client as mqtt
import sys
import uuid
import time

broker = 'my_iot.mqtt.iot.gz.baidubce.com'
port = 1883
username = 'iotfreetest/thing01'
password = 'YU7Tov8zFW+WuaLx9s9I3MKyclie9SGDuuNkl6o9LXo='
clientid = 'test_mqtt_python_' + str(uuid.uuid4())
topic = 'demoTopic'

should_end = False

def on_connect(client, userdata, rc):
    print('Connected. Client id is: ' + clientid)
    client.subscribe(topic)
    print('Subscribed to topic: ' + topic)

    client.publish(topic, 'Message from Baidu IoT demo')
    print('MQTT message published.')

def on_message(client, userdata, msg):
    msg = str(msg.payload, 'gbk')
    print('MQTT message received: ' + msg)
    if msg == 'exit':
        # client.loop_stop()
        should_end=True
        sys.exit()

client = mqtt.Client(clientid)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username, password)

print('Connecting to broker: ' + broker)
client.connect(broker, port)

# client.loop_forever()
client.loop_start()
while not should_end:
	client.publish(topic, 'Message from Baidu IoT demo=>MSG:'+str(uuid.uuid4()))
	time.sleep(1)
	# client.loop()
# 	# print("loop_forever...")
# print("loop_forever...")