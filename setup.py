from distutils.core import setup, Extension

source_files = ['source/py_driver_wrapper.c', 'source/MyBMP180_RPi_Driver/bmp180_rpi_driver.c', 'source/MyBMP180_RPi_Driver/bmp180.c', 'source/MyBMP180_RPi_Driver/rpi_utils.c']
setup(name          = 'MyPyBMP180', 
        version     = '0.1',  
        author      = 'Stefano Vettor', 
        license     = 'MIT', 
        url         = 'https://github.com/freedom27/MyPyBMP180', 
        description = 'Library to get readings from the Bosch BMP180 pressure and temperature sensor on a Raspberry Pi',
        packages    = ['MyPyBMP180'],
        ext_modules = [Extension('MyPyBMP180.bmp180_driver', source_files, extra_compile_args=['-std=gnu99'])])