# MyPyBMP180
MyPyBMP180 is a small library in python 3 for the Raspberry Pi (1, 2, 3 and Zero) to interact with the pressure & temperature sensor BMP180

## Installation
Before installing it be sure that your Pi is compatible with Python Extensions. On Raspbian the following commands will ensure it:
````
apt-get update
sudo apt-get install build-essential python-dev
````
Since this library use git submodels use the following command to clone the repository:
````
git clone --recursive https://github.com/freedom27/MyPyBMP180
````
Once the repository has been cloned enter the following command inside the main folder:
````
sudo python setup.py install
````
Now MyPyBMP180 is succesfully installed and ready to be used inside your python projects!

## How to use
In any python file you whish to use the library import the module and call the sensor_read function as follow:
```python
import MyPyBMP180

pressure, temperature = MyPyBMP180.sensor_read()
# pressure = 1016.12 (it's in mbar), temperature = 20.31 (celsius degrees)
```
The function doesn't require any input to work. 
In case of failure it raises a __BMP180Exception__.

The __BMP180Exception__ class has an attribude _message_ describing what issue occurred while attempting to read the sensor.
