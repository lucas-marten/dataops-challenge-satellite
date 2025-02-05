import argparse
import os

import utils


def get_argparser():
    parser = argparse.ArgumentParser(description="Reproject satellite image")
    parser.add_argument(
        "--input_file", type=str, help="Path to the input satellite image file"
    )
    parser.add_argument("--output_file", type=str, help="Path to the output file")
    parser.add_argument(
        "--target_project",
        type=str,
        help="Project to the output file",
        default="EPSG:4326",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_argparser()
    input_file = args.input_file
    output_file = args.output_file
    target_project = args.target_project

    if not input_file or not output_file:
        print("Input file is required")
        exit(1)

    utils.reproject_to_another_file(input_file, output_file, target=target_project)
