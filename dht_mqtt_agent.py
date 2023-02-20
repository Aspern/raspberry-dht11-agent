import ssl
import configparser
import paho.mqtt.client as mqtt
import time
import os
from init_dht_device import init_dht_device

# reading config from environment
config = configparser.ConfigParser()
config.read(f'/home/{os.environ["USER"]}/config/dht_agent_config.ini')


# set variables from config.ini file
mqttHost = config['mqtt']['host']
mqttPort = int(config['mqtt']['port'])
realm = config['mqtt']['realm']
clientId = config['mqtt']['client_id']
clientSecret = config['mqtt']['client_secret']
assetId = config['sensor']['asset_id']
temperatureAttribute = config['sensor']['temperature_attribute']
humidityAttribute = config['sensor']['humidity_attribute']
dhtModel = config['sensor']['dht_model']
gpioDataPin = int(config['sensor']['gpio_data_pin'])
pollingSeconds = float(config['sensor']['polling_seconds'])
username = f'{realm}:{clientId}'

# initializing dht device
dhtDevice = init_dht_device(dhtModel, gpioDataPin)

# initializing and starting mqtt client
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
client = mqtt.Client(clientId)
client.username_pw_set(username, password=clientSecret)
client.tls_set_context(context)
client.connect(mqttHost, port=mqttPort)
client.loop_start()

while True:
    try:
        # reading values from sensor
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity

        print(f'Sending data temperature={temperature}°C, humidity={humidity}%')

        # sending sensor values to digital twin on iot platform
        client.publish(f'{realm}/{clientId}/writeattributevalue/{humidityAttribute}/{assetId}', payload=humidity)
        client.publish(f'{realm}/{clientId}/writeattributevalue/{temperatureAttribute}/{assetId}', payload=temperature)
    except RuntimeError:
        print("Error reading or sending sensor values.", RuntimeError)

    time.sleep(pollingSeconds)
