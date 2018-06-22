from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("cvector.pyx",
    annotate=True),
)
#python setup.py build_ext --inplace