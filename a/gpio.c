
#include <Python.h>
#include <wiringPi.h>

//Define 4 GPIO pins
#define gpio    0//physical pin 5
#define gpio1   15//physical pin 8
#define gpio2   21//physical pin 24
#define gpio3   11//physical pin 20


static PyObject* gpioswitch(PyObject* self, PyObject* args){
  // onoff is the toggle value for what ever switch is getting switched
  // int onoff = 0;

  int SwitchNum, status;
  // int word;
  if (!PyArg_ParseTuple(args, "ii", &SwitchNum, &status)) {
    return NULL;
  }
    switch (SwitchNum){
	case 1:
	   digitalWrite(gpio,status);
	   break;
	case 2:
	   digitalWrite(gpio1,status);
	   break;
	case 3:
	   digitalWrite(gpio2,status);
	   break;
	case 4:
	   digitalWrite(gpio3,status);
	   break;
	default:
	   status = 0;
	   digitalWrite(gpio,status);
	   digitalWrite(gpio1,status);
	   digitalWrite(gpio2,status);
	   digitalWrite(gpio3,status);
	   break;
}	
//  printf("This is a C function was passed...%d and %d\n", x, y);
  return Py_None;//Py_BuildValue("s","hello");
}

static PyMethodDef GPIOMethods[] =
{
  {"gpioswitch", gpioswitch, METH_VARARGS, "Pass a number."},
  {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initlibsay(void) {
  (void) Py_InitModule("libgpio", GPIOMethods);
  wiringPiSetup();
  pinMode (gpio, OUTPUT) ;
  pinMode (gpio1, OUTPUT);
  pinMode (gpio2, OUTPUT);
  pinMode (gpio3, OUTPUT);
}
