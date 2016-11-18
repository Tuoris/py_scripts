#include <Python.h>

static PyObject *
spam_system(PyObject *self, PyObject *args) {
	const char *command;
	int sts;

	if (!PyArg_ParseTuple(args, "s", &command))
		return NULL;

	sts = system(command);
	if (sts < 0) {
		return NULL;
	}
	return PyLong_FromLong(sts);
}

static PyMethodDef functions[] = {
	{	"system", spam_system, METH_VARARGS,
		"Execute command given as parameter"
	},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef spamModule = {
	PyModuleDef_HEAD_INIT,
	"spam",  // module name
	NULL, // means that the module does not support sub-interpreters, because it has global state.
	-1,
	functions
};


PyMODINIT_FUNC PyInit_spam(void) {
	return PyModule_Create(&spamModule);
}
