#!/bin/bash

sudo apt update && sudo apt upgrade -y
sudo apt remove --purge -y gdal-bin libgdal-dev python3-gdal
sudo apt autoremove -y
sudo add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable
sudo apt update
sudo apt install -y gdal-bin libgdal-dev python3-gdal

gdalinfo --version

python3 -m venv venv

source venv/bin/activate

GDAL_VERSION=$(gdal-config --version)

pip install --no-cache-dir GDAL==$GDAL_VERSION

python -c "from osgeo import gdal; print('GDAL version:', gdal.__version__)"
