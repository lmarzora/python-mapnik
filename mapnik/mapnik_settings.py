import os
import sys
mapnik_data_dir = os.path.dirname(os.path.realpath(__file__))

if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'install')

mapnik_data_dir = os.path.join(base_dir, 'mapnik', 'share')
env = {}
icu_path = os.path.join(mapnik_data_dir, 'icu')
if os.path.isdir(icu_path):
    env['ICU_DATA'] = icu_path
gdal_path = os.path.join(mapnik_data_dir, 'gdal')
if os.path.isdir(gdal_path):
    env['GDAL_DATA'] = gdal_path
proj_path = os.path.join(mapnik_data_dir, 'proj')
if os.path.isdir(proj_path):
    env['PROJ_LIB'] = proj_path
