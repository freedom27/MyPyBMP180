import MyPyBMP180.bmp180_driver


class BMP180Exception(Exception):
    def __init__(self, mess):
        self.message = mess

BMP180_OK                   =  0
BMP180_I2C_INIT_ERROR       = -1
BMP180_DRIVER_INIT_ERROR    = -2
BMP180_SENSOR_ERROR         = -3


def sensor_read():
    result, pressure, temperature = MyPyBMP180.bmp180_driver._bmp180_read()
    if result != BMP180_OK:
        if result == BMP180_I2C_INIT_ERROR:
            error_mess = "An error occurred while estabilishing the connection with the I2C bus!"
        elif result == BMP180_DRIVER_INIT_ERROR:
            error_mess = "An error occurred while initializing the bmp180 driver!"
        else:
            # result == BMP180_SENSOR_ERROR
            error_mess = "An error occurred while reading the sensor's data!"
        
        raise BMP180Exception("Error")
        
    return round(pressure, 2), round(temperature, 2)