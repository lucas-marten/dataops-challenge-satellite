# Overview:

### The gdalinfo command is a utility from the GDAL library that provides detailed metadata about a raster dataset, including its format, projection, resolution, coordinate system, and band information. It is commonly used to inspect geospatial files before processing them.

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

#### The files are georeferenced images in GeoTIFF format, each representing different projections and resolutions. These files correspond to different timestamps, indicating they were captured at different moments in time.

#### File1, File2 and File3 are from geostationary satellites but in distinct projections.

#### File1 and File2 are in the Plate Carrée projection, with a spatial resolution of approximately 2km per pixel. File3 is in a Geostationary projection, based on a system with a satellite at 35.786km altitude. 

#### File4 is different from the previous files. It is in a Polar Stereographic projection (Bessel 1841), with a spatial resolution of 1km per pixel. Unline the others, this file has four bands (RGB + Alpha), indicating that it is a color image with transparency channel. 

| File  | Format  | Projection  | Spatial Resolution | Size (pixels) | Coordinate System | Acquisition Date | Bands |
|--------|---------|-------------|--------------------|--------------|-------------------|----------------|-------|
| File 1 | GeoTIFF | Plate Carrée (Equidistant Cylindrical) | ~3 km per pixel | 5666 x 5936 | WGS 84 (EPSG:4326) | 2025-01-22 06:15:00 UTC | 1 (Grayscale) |
| File 2 | GeoTIFF | Plate Carrée (Equidistant Cylindrical) | ~2 km per pixel | 8500 x 8906 | WGS 84 (EPSG:4326) | 2025-01-22 08:00:00 UTC | 1 (Grayscale) |
| File 3 | GeoTIFF | Geostationary (Sweep Y) | ~2 km per pixel | 5424 x 5424 | Custom geostationary projection | Not specified | 1 (Grayscale) |
| File 4 | GeoTIFF | Polar Stereographic (Bessel 1841) | ~1 km per pixel | 2560 x 2088 | PROJCRS["unnamed", BASEGEOGCRS["Bessel 1841"]] | 2025-01-20 12:19:01 UTC | 4 (Red, Green, Blue, Alpha) |

### Another way to extract metadata is by using a Python script. You can do this by running the following command:

```python3
python3 satellite-data-processing/scripts/extract_metadata.py --input_file satellite-data-processing/data/file1 --output_file satellite-data-processing/processed_data/metadata/file1.json
```

```python3
python3 satellite-data-processing/scripts/extract_metadata.py --input_file satellite-data-processing/data/file2 --output_file satellite-data-processing/processed_data/metadata/file2.json
```

```python3
python3 satellite-data-processing/scripts/extract_metadata.py --input_file satellite-data-processing/data/file3 --output_file satellite-data-processing/processed_data/metadata/file3.json
```

```python3
python3 satellite-data-processing/scripts/extract_metadata.py --input_file satellite-data-processing/data/file4 --output_file satellite-data-processing/processed_data/metadata/file4.json
```