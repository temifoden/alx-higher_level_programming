#include <Python.h>
#include <stdio.h>

/*
 * print_python_bytes - Print basic information about a Python bytes object
 * @p: Pointer to the PyObject representing the bytes object
 *
 * This function prints the size, string representation, and the first
 * few bytes of a Python bytes object. If the provided object is not a
 * valid bytes object, an error message is printed.
 */

void print_python_bytes(PyObject *p)
{
    Py_ssize_t i, size;
    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
    printf(" [ERROR] Invalid Bytes Object\n");
    return;
    }

    size = PyBytes_Size(p);
    printf(" size: %ld\n", size);
    printf(" trying string: %s\n", PyBytes_AsString(p));

    printf(" first %ld bytes: ", (size < 10)? size: 10);
    for (i = 0; i < size && i < 10; i++)
    {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}

/*
 * print_python_list - Print basic information about a Python list object
 * @p: Pointer to the PyObject representing the list object
 *
 * This function prints the size, allocated memory, and the type of each
 * element in a Python list object. If an element is a bytes object, it
 * also prints additional information about the bytes object.
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t i, size;
    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
        if (PyBytes_Check(PyList_GetItem(p, i)))
        {
            print_python_bytes(PyList_GetItem(p, i));
        }
    }
}
