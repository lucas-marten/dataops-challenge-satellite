#!venv/bin/python3
import argparse
import json

import utils


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

    if not input_file or not output_file:
        print("Input file is required")
        exit(1)

    metadata_dict = utils.metadata(input_file)
    print(metadata_dict)

    with open(output_file, "w") as f:
        json.dump(metadata_dict, f, indent=4)

    print(f"Metadata written to {output_file}")
