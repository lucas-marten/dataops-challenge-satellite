# Overview:

#### The files are georeferenced images in GeoTIFF format, each representing different projections and resolutions. These files correspond to different timestamps, indicating they were captured at different moments in time.

#### File1, File2 and File3 are from geostationary satellites but in distinct projections.

#### File1 and File2 are in the Plate Carrée projection, with a spatial resolution of approximately 2km per pixel. File3 is in a Geostationary projection, based on a system with a satellite at 35.786km altitude. 

#### File4 is different from the previous files. It is in a Polar Stereographic projection (Bessel 1841), with a spatial resolution of 1km per pixel. Unline the others, this file has four bands (RGB + Alpha), indicating that it is a color image with transparency channel. 

| File  | Format  | Projection  | Size (pixels) | Coordinate System | Acquisition Date | Bands |
|--------|---------|-------------|--------------|-------------------|----------------|-------|
| File 1 | GeoTIFF | Plate Carrée (Equidistant Cylindrical) | 5666 x 5936 | WGS 84 (EPSG:4326) | 2025-01-22 06:15:00 UTC | 1 (Grayscale) |
| File 2 | GeoTIFF | Plate Carrée (Equidistant Cylindrical) | 8500 x 8906 | WGS 84 (EPSG:4326) | 2025-01-22 08:00:00 UTC | 1 (Grayscale) |
| File 3 | GeoTIFF | Geostationary (Sweep Y) | 5424 x 5424 | Custom geostationary projection | Not specified | 1 (Grayscale) |
| File 4 | GeoTIFF | Polar Stereographic (Bessel 1841) | 2560 x 2088 | PROJCRS["unnamed", BASEGEOGCRS["Bessel 1841"]] | 2025-01-20 12:19:01 UTC | 4 (Red, Green, Blue, Alpha) |
