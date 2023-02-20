import board
import adafruit_dht


def init_dht_device(dht_type, gpio_data_pin):
    if dht_type == 'DHT11':
        return adafruit_dht.DHT11(resolve_board_pin(gpio_data_pin))
    elif dht_type == 'DHT21':
        return adafruit_dht.DHT21(resolve_board_pin(gpio_data_pin))
    elif dht_type == 'DHT22':
        return adafruit_dht.DHT22(resolve_board_pin(gpio_data_pin))
    else:
        raise RuntimeError(f'There is no supported DHT device for type={dht_type}. Supported types are DHT11, DHT21 and '
                           f'DHT22.')


def resolve_board_pin(gpio_data_pin):
    if gpio_data_pin == 3:
        return board.D3
    elif gpio_data_pin == 5:
        return board.D5
    elif gpio_data_pin == 7:
        return board.D7
    elif gpio_data_pin == 8:
        return board.D8
    elif gpio_data_pin == 9:
        return board.D9
    elif gpio_data_pin == 10:
        return board.D10
    elif gpio_data_pin == 11:
        return board.D11
    elif gpio_data_pin == 12:
        return board.D12
    elif gpio_data_pin == 13:
        return board.D13
    elif gpio_data_pin == 15:
        return board.D15
    elif gpio_data_pin == 16:
        return board.D16
    elif gpio_data_pin == 17:
        return board.D17
    elif gpio_data_pin == 18:
        return board.D18
    elif gpio_data_pin == 19:
        return board.D19
    elif gpio_data_pin == 21:
        return board.D21
    elif gpio_data_pin == 22:
        return board.D22
    elif gpio_data_pin == 23:
        return board.D23
    elif gpio_data_pin == 24:
        return board.D24
    elif gpio_data_pin == 25:
        return board.D25
    elif gpio_data_pin == 26:
        return board.D26
    elif gpio_data_pin == 27:
        return board.D27
    elif gpio_data_pin == 28:
        return board.D28
    elif gpio_data_pin == 29:
        return board.D29
    elif gpio_data_pin == 30:
        return board.D30
    elif gpio_data_pin == 31:
        return board.D31
    elif gpio_data_pin == 32:
        return board.D32
    elif gpio_data_pin == 33:
        return board.D33
    elif gpio_data_pin == 34:
        return board.D34
    elif gpio_data_pin == 35:
        return board.D35
    elif gpio_data_pin == 36:
        return board.D36
    elif gpio_data_pin == 37:
        return board.D37
    elif gpio_data_pin == 38:
        return board.D38
    elif gpio_data_pin == 40:
        return board.D40
    else:
        raise RuntimeError(f'gpioDataPin with value {gpio_data_pin} is not supported on platform.')
