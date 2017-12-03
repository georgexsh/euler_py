import glob
from distutils.core import setup, Extension

sources = glob.glob('src/*.c')

euler = Extension(
    'euler_py',
    include_dirs=['ext'],
    sources=sources,
    extra_compile_args=['-std=c99']
)

setup(
    name='euler_py',
    version='0.1',
    description='Project Euler Solutions',
    ext_modules=[euler]
)
