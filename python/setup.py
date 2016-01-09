#!/usr/bin/python
from distutils.core import setup, Extension

core_ext = Extension(
    name                = 'core',
    sources             = ['rgbmatrix/core.cpp'],
    include_dirs        = ['../include'],
    library_dirs        = ['../lib'],
    libraries           = ['rgbmatrix'],
    extra_compile_args  = ["-O3", "-Wall"],
    language            = 'c++'
)

graphics_ext = Extension(
    name                = 'graphics',
    sources             = ['rgbmatrix/graphics.cpp'],
    include_dirs        = ['../include'],
    library_dirs        = ['../lib'],
    libraries           = ['rgbmatrix'],
    extra_compile_args  = ["-O3", "-Wall"],
    language            = 'c++'
)

setup(
    name                = 'rgbmatrix',
    ext_package         = 'rgbmatrix',
    ext_modules         = [core_ext, graphics_ext],
    packages            = ['rgbmatrix']
)