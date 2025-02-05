# Merging GeoTIFF Files  

## Overview  
Merging multiple GeoTIFF files allows for seamless analysis across different datasets by combining them into a single raster file. This process is useful for creating mosaics, improving spatial coverage, and ensuring consistency in geospatial data.  

## Files Included in the Merge  
- **File 1** (Meteosat-10) - Plate Carrée Projection  
- **File 2** (Himawari-9) - Plate Carrée Projection  
- **File 3** (GOES-East) - Geostationary Projection  

### **Excluded File:**  
- **File 4** (MODIS/VIIRS) - Polar Stereographic Projection, Multi-band (RGB + Alpha)  

### **Why File 4 Was Not Included?**  
 - **Different Data Type**: File 4 contains 4 bands (RGB + Alpha), whereas the other files contain 1 grayscale band.
 - **Different Spatial Context**: File 4 represents a polar-orbiting satellite dataset, while the others are from geostationary satellites.

## Tools and Methods  
- **Command Used:**  
  ```shell
   python3 satellite-data-processing/scripts/merge_data.py --files satellite-data-processing/processed_data/tiffs/file1.epsg\:4326.tiff satellite-data-processing/processed_data/tiffs/file2.epsg\:4326.tiff satellite-data-processing/processed_data/tiffs/file3.epsg\:4326.tiff
  ``` 