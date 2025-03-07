#!venv/bin/python3
import argparse
import os
import rasterio
import rasterio.merge

import utils


def get_argparser():
    parser = argparse.ArgumentParser(description="Get metadata from a satellite image")
    parser.add_argument(
        "--files",
        type=str,
        nargs="+",
        default=[],
        help="Paths to the input satellite image files",
    )
    parser.add_argument(
        "--output_file", type=str, help="Path to the output metadata file"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_argparser()

    if not args.files or not args.output_file:
        print("Input and output file is required")
        exit(1)

    files = [rasterio.open(p) for p in args.files]

    data, affine = utils.merge_files(files)

    metadata = files[0].meta
    metadata = metadata.copy()

    metadata.update(
        {
            "driver": "GTiff",
            "height": data.shape[1],
            "width": data.shape[2],
            "transform": affine,
            "crs": "+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs ",
        }
    )

    os.makedirs(os.path.dirname(args.output_file), exist_ok=True)

    utils.write_file(args.output_file, data, metadata)
