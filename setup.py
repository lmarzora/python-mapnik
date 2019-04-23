#! /usr/bin/env python
from setuptools import setup

setup(
    name="mapnik",
    version="0.2",
    packages=['mapnik','mapnik.printing'],
    author="Blake Thompson",
    author_email="flippmoke@gmail.com",
    description="Python bindings for Mapnik",
    license="GNU LESSER GENERAL PUBLIC LICENSE",
    keywords="mapnik mapbox mapping cartography",
    url="http://mapnik.org/",
    package_data={
        'mapnik': ['lib/*.*', 'lib/*/*/*', 'share/*/*'],
    }
)
