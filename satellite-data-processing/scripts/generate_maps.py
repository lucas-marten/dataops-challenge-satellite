#!venv/bin/python3
import argparse
import os
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


def get_argparser():
    parser = argparse.ArgumentParser(description="Get metadata from a satellite image")
    parser.add_argument(
        "--input_file", type=str, help="Path to the input satellite image file"
    )
    parser.add_argument("--output_file", type=str, help="Path to the output file")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_argparser()
    input_file = args.input_file
    output_file = args.output_file

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    if not input_file or not output_file:
        print("Input file is required")
        exit(1)
    
    dataset = xr.open_dataset(input_file, engine="rasterio")

    if 'file2' in input_file:
        dataset = dataset.sel(x=slice(60,180))
    
    elif 'file4' in input_file:
        cmap = None

    else:
        cmap = 'gray'
        
    data = dataset['band_data'].values
    lons, lats = dataset['x'].values, dataset['y'].values

    dataset.close()

    fig = plt.figure(figsize=(16,8), dpi=300)
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    
    ax.contourf(lons, lats, data[0], cmap=cmap)
    
    plt.savefig(output_file)