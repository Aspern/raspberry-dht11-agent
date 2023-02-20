# raspberry-dht-agent

simple agent which reads temperature and humidity data from any type of dht sensor.
The data is sent to a mqtt broker on any server or in the public cloud.

## Getting started

### Installation

Connect to your raspberry pi (or any other microcontroller supporting the DHT and Python).

Clone the Git repository using following command

```bash
git clone https://github.com/Aspern/raspberry-dht11-agent.git
```

The `raspberry-dht-agent` needs third party packages to start working.

```bash
pip3 install adafruit-circuitpython-dht
pip3 install paho-mqtt
pip3 install configparser
sudo apt-get install libgpiod2
```

### Configuration

Before starting the client, the configuration in the `config.ini` file needs to be adjusted.

| Parameter                      | Description                                                          | Example     |
|--------------------------------|----------------------------------------------------------------------|-------------|
| `mqtt.host`                    | Hostname of the remote server                                        | localhost   |
| `mqtt.port`                    | Port of the remote mqtt server                                       | 8883        |
| `mqtt.realm`                   | Name of the tenant in the remote server                              | master      |
| `mqtt.client_id`               | Id of the technical client   (client_credential flow)                | my-client   |
| `sensor.gpio_data_pin`         | Number of the GPIO digital pin, where the sensors data port is wired | 23          |
| `sensor.dht_model`             | model number of the DHT sensor. Supported are DHT11, DHT21 and DHT22 | DHT11       |
| `sensor.asset_id`              | Id of the digital twin (asset) on the remote server                  | a6x4rmenu   |
| `sensor.temperature_attribute` | Name of the temperature attribute                                    | temperature |
| `sensor.humidity_attribute`    | Name of the humidity attribute                                       | humidity    |
| `sensor.polling_seconds`       | Time in seconds between data collection and upload                   | 900         |

### Creating crontab

The best way to execute the `raspberry-dht-agent` is to initialize a crontab for it on `@reboot`
Therefore following scripts in the repository can be used.

```bash
chmod +x install_crontab.sh
./install_crontab.sh
```
