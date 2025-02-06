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

