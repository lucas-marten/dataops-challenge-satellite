## Reprojection Overview  
All files were reprojected to **EPSG:4326 (WGS 84)** using **GDAL** with **bilinear interpolation** to ensure smooth resampling and reduce artifacts. The reprojection process aimed to align all datasets to a common geographic coordinate system for easier analysis and comparison.  

## Reprojected Files  

### File 1 - Meteosat-10  
- **Original Projection:** Plate Carrée (Equidistant Cylindrical)  
- **Target Projection:** EPSG:4326 grid
- **Reprojection Method:** Bilinear interpolation  

### File 2 - Himawari-9  
- **Original Projection:** Plate Carrée (Equidistant Cylindrical)  
- **Target Projection:** EPSG:4326 grid
- **Reprojection Method:** Bilinear interpolation  

### File 3 - GOES-EAST  
- **Original Projection:** Geostationary (Sweep Y)  
- **Target Projection:** EPSG:4326 grid
- **Reprojection Method:** Bilinear interpolation  

### File 4 - MODIS/VIIRS  
- **Original Projection:** Polar Stereographic (Bessel 1841)  
- **Target Projection:** EPSG:4326 grid
- **Reprojection Method:** Bilinear interpolation  

## Processing Details  
- **Software Used:** GDAL  
- **Command Example:**  
  ```shell
  python3 satellite-data-processing/scripts/reproject.py --input_file satellite-data-processing/data/file1 --output_file satellite-data-processing/processed_data/tiffs/file1.epsg:4326.tiff --target EPSG:4326
  ```
