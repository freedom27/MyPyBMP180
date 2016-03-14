#include <Python.h>

#include "MyBMP180_RPi_Driver/bmp180_rpi_driver.h"

static PyObject *sensor_read(PyObject *self, PyObject *args) {
    int result;

    struct bmp180_sensor_data data;
    result = bmp180_read(&data);
    if(result != BMP180_OK)
        data.pressure = data.temperature = 0.0f;

    return Py_BuildValue("iff", result, data.pressure, data.temperature);
}

static PyMethodDef BMP180Methods[] = {
    {"_bmp180_read", sensor_read, METH_VARARGS, "Read sensor data!"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef mypybmp180module = {
    PyModuleDef_HEAD_INIT,
    "bmp180_driver",  /* name of module */
    NULL,       /* module documentation, may be NULL */
    -1,         /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
    BMP180Methods
};

PyMODINIT_FUNC PyInit_bmp180_driver(void) {
    return PyModule_Create(&mypybmp180module);
}