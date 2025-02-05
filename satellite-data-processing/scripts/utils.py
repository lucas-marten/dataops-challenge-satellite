import numpy as np
import rasterio
import rasterio.merge
from osgeo import gdal, osr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import xarray


def open_tiff(path):
    dataset = gdal.Open(path, gdal.GA_ReadOnly)

    if dataset:
        return dataset
    else:
        print(f"Unable to open {path}")
        exit(1)


def get_shape(dataset):
    t = dataset.RasterCount
    x = dataset.RasterXSize
    y = dataset.RasterYSize
    return (t, x, y)


def get_projection(dataset):
    projection = dataset.GetProjection()
    return projection


def parse_projection_info(projection):
    proj_dict = {}
    proj_parts = projection.split("[")
    for part in proj_parts:
        if "]" in part:
            key_value = part.split("]")
            key = key_value[0].split(",")[0].replace('"', "").strip()
            value = key_value[0].split(",")[1:]
            proj_dict[key] = [v.replace('"', "").strip() for v in value]
    return proj_dict


def get_drivers(dataset):
    return dataset.GetDriver()


def get_metadata(dataset):
    metadata = dataset.GetMetadata()
    return metadata


def get_geotransform(dataset):
    geotransform = dataset.GetGeoTransform()
    return geotransform


def get_band(dataset, band):
    band = dataset.GetRasterBand(band)
    if isinstance(band, gdal.Band):
        return band
    else:
        raise Exception("Band not found")


def get_min_max(band):

    value_min = band.GetMinimum()
    value_max = band.GetMaximum()

    if not value_min or not max:
        value_min, value_max = band.ComputeRasterMinMax(True)

    return value_min, value_max


def get_coords(dataset):
    geotransform = dataset.GetGeoTransform()
    x_min, pixel_width, _, y_max, _, pixel_height = geotransform
    x_max = x_min + (dataset.RasterXSize * pixel_width)
    y_min = y_max + (dataset.RasterYSize * pixel_height)
    
    lon = np.linspace(x_min, x_max, dataset.RasterXSize)
    lat = np.linspace(y_max, y_min, dataset.RasterYSize) 
    
    return np.meshgrid(lon, lat)


def metadata(input_file):
    dataset = open_tiff(input_file)
    projection = get_projection(dataset)
    shape = get_shape(dataset)
    drivers = get_drivers(dataset)
    metadata = get_metadata(dataset)
    geotransform = get_geotransform(dataset)
    band = get_band(dataset, 1)
    value_min, value_max = get_min_max(band)

    metadata_dict = {
        "projection": parse_projection_info(projection),
        "shape": str(shape),
        "drivers": f"Drivers: ({drivers.ShortName}, {drivers.LongName})",
        "metadata": ["{}: {}".format(k, v) for k, v in metadata.items()],
        "geotransform": {
            "top_left_x": geotransform[0],
            "w_e_pixel_resolution": geotransform[1],
            "rotation_1": geotransform[2],
            "top_left_y": geotransform[3],
            "rotation_2": geotransform[4],
            "n_s_pixel_resolution": geotransform[5],
        },
        "value_min": str(value_min),
        "value_max": str(value_max),
    }
    return metadata_dict


def reproject_to_another_file(input_file, output_file, target="EPSG:4326"):
    gdal.Warp(
        output_file, input_file, dstSRS=target, resampleAlg="bilinear"
    )  # to write another file
    return True


def reproject_to_memory_dataset(input_file, target="EPSG:4326"):
    dataset = gdal.Open(input_file)
    warp_options = gdal.WarpOptions(
        dstSRS=target, format="MEM", resampleAlg=gdal.GRA_Bilinear
    )
    newds = gdal.Warp("", dataset, options=warp_options)  # to save in memory
    return newds


def reproject_data(dataset, outputfile, target="EPSG:4326"):

    src_proj = osr.SpatialReference()
    src_proj.ImportFromWkt(get_projection(dataset))

    target_proj = osr.SpatialReference()
    target_proj.ImportFromEPSG(int(target.split(":")[1]))

    if outputfile:
        warp_options = gdal.WarpOptions(dstSRS=target, resampleAlg=gdal.GRA_Bilinear)
        gdal.Warp(outputfile, dataset, options=warp_options)  # to save in another file

    else:
        warp_options = gdal.WarpOptions(
            dstSRS=target, format="MEM", resampleAlg=gdal.GRA_Bilinear
        )
        newds = gdal.Warp("", dataset, options=warp_options)  # to save in memory
        return newds


def merge_files(files):
    dataset = rasterio.merge.merge(files)
    data = dataset[0]
    affine = dataset[1]
    return data, affine


def write_file(output_file, data, metadata):
    with rasterio.open(output_file, "w", **metadata) as dest:
        dest.write(data)

def plot_image(lons, lats, data):
    fig = plt.figure(figsize=(16,8), dpi=300)
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    
    ax.contourf(lons, lats, data, cmap='gray')
    
    plt.show()