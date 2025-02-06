# Satellite Data Processing Challenge

## Overview
This project addresses a challenge centered around satellite data processing. The objective is to process provided satellite data files, extract useful information, and create meaningful visual and analytical outputs.

## Project Structure
```
📂 satellite-data-processing/
│── 📂 data/                         # Original satellite data files
│── 📂 processed_data/               # Processed files (reprojected, merged, etc.)
│── 📂 notebooks/                    # Jupyter Notebooks for exploratory analysis
│   ├── weather_insights.py          # Extract weather-related insights
│── 📂 scripts/                      # Python scripts for processing
│   ├── extract_metadata.py          # Extract metadata from files
│   ├── reproject.py                 # Reproject images to a common system
│   ├── merge_data.py                # Merge compatible files
│   ├── generate_maps.py             # Generate visualizations (heatmaps, etc.)
│── 📂 docs/                         # Documentation
│   ├── description_of_the_files.md  # Overview of the dataset
│   ├── images_representations.md    # Description of satellite images, their coverage, and representations  
│   ├── reproject_images.md          # Explanation of the reprojection process, methods used
│   ├── merged_files.md              # Details on merging selected files, rationale for selection, and final output specifications  
│── requirements.txt                 # Project dependencies
│── install_gdal.sh                  # Correct installation of GDAL on the operating system and Python environment  
```

# Satellite Data Processing Workflow


### Summary
This workflow covers:
- Extracting metadata using `gdalinfo` and Python scripts.
- Reprojecting files to `EPSG:4326` (or other projections such as `EPSG:3857`, `EPSG:32633`, and `EPSG:32634`).
- Merging multiple TIFF files into one.
- Converting TIFF files into PNG images for visualization.


### Additional Documentation
- [Description of the Files](satellite-data-processing/docs/description_of_the_files.md)
- [Image Representations](satellite-data-processing/docs/images_representations.md)
- [Merged Files](satellite-data-processing/docs/merged_files.md)
- [Reprojected Images](satellite-data-processing/docs/reproject_images.md)


### Installing Dependencies
Before running the processing scripts, install the required dependencies. 

```bash
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
```

or just run `install_gdal.sh`:

```bash
bash install_gdal.sh
```

## Step-by-Step Guide

### 1. Extracting Metadata
#### Using `gdalinfo`
To extract metadata from satellite data files, use the `gdalinfo` command:

```bash
gdalinfo satellite-data-processing/data/file1 >> satellite-data-processing/processed_data/metadata/file1.txt && cat satellite-data-processing/processed_data/metadata/file1.txt
```
```bash
gdalinfo satellite-data-processing/data/file2 >> satellite-data-processing/processed_data/metadata/file2.txt && cat satellite-data-processing/processed_data/metadata/file2.txt
```
```bash
gdalinfo satellite-data-processing/data/file3 >> satellite-data-processing/processed_data/metadata/file3.txt && cat satellite-data-processing/processed_data/metadata/file3.txt
```
```bash
gdalinfo satellite-data-processing/data/file4 >> satellite-data-processing/processed_data/metadata/file4.txt && cat satellite-data-processing/processed_data/metadata/file4.txt
```

#### Using a Python Script
Alternatively, you can use a Python script:

```bash
python3 satellite-data-processing/scripts/extract_metadata.py --input_file satellite-data-processing/data/file1 --output_file satellite-data-processing/processed_data/metadata/file1.json
```
```bash
python3 satellite-data-processing/scripts/extract_metadata.py --input_file satellite-data-processing/data/file2 --output_file satellite-data-processing/processed_data/metadata/file2.json
```
```bash
python3 satellite-data-processing/scripts/extract_metadata.py --input_file satellite-data-processing/data/file3 --output_file satellite-data-processing/processed_data/metadata/file3.json
```
```bash
python3 satellite-data-processing/scripts/extract_metadata.py --input_file satellite-data-processing/data/file4 --output_file satellite-data-processing/processed_data/metadata/file4.json
```

### 2. Reprojecting Data
The script `reproject.py` is used to convert data to the `EPSG:4326` projection:

```bash
python3 satellite-data-processing/scripts/reproject.py --input_file satellite-data-processing/data/file1 \
    --output_file satellite-data-processing/processed_data/tiffs/file1.epsg:4326.tiff \
    --target EPSG:4326
```
```bash
python3 satellite-data-processing/scripts/reproject.py --input_file satellite-data-processing/data/file2 \
    --output_file satellite-data-processing/processed_data/tiffs/file2.epsg:4326.tiff \
    --target EPSG:4326
```
```bash
python3 satellite-data-processing/scripts/reproject.py --input_file satellite-data-processing/data/file3 \
    --output_file satellite-data-processing/processed_data/tiffs/file3.epsg:4326.tiff \
    --target EPSG:4326
```
```bash
python3 satellite-data-processing/scripts/reproject.py --input_file satellite-data-processing/data/file4 \
    --output_file satellite-data-processing/processed_data/tiffs/file4.epsg:4326.tiff \
    --target EPSG:4326
```

### 3. Merging Data
To merge multiple TIFF files into a single output file:

```bash
python3 satellite-data-processing/scripts/merge_data.py \
    --files \
        satellite-data-processing/processed_data/tiffs/file1.epsg:4326.tiff \
        satellite-data-processing/processed_data/tiffs/file2.epsg:4326.tiff \
        satellite-data-processing/processed_data/tiffs/file3.epsg:4326.tiff \
    --output_file satellite-data-processing/processed_data/tiffs/merged.epsg:4326.tiff
```

### 4. Generating PNG Images
To generate PNG images from the processed TIFF files:

```bash
python3 satellite-data-processing/scripts/generate_maps.py \
    --input_file satellite-data-processing/processed_data/tiffs/file1.epsg:4326.tiff \
    --output_file satellite-data-processing/processed_data/pngs/file1.png
```

