# Satellite Data Processing Challenge

## Overview
This project addresses a challenge centered around satellite data processing. The objective is to process provided satellite data files, extract useful information, and create meaningful visual and analytical outputs.

## Project Structure
```
📂 satellite-data-processing/
│── 📂 data/                         # Original satellite data files
│── 📂 processed_data/               # Processed files (reprojected, merged, etc.)
│── 📂 visualizations/               # Generated maps and visual outputs
│── 📂 notebooks/                    # Jupyter Notebooks for exploratory analysis
│── 📂 scripts/                      # Python scripts for processing
│   ├── extract_metadata.py          # Extract metadata from files
│   ├── reproject.py                 # Reproject images to a common system
│   ├── merge_data.py                # Merge compatible files
│   ├── generate_maps.py             # Generate visualizations (heatmaps, etc.)
│   ├── weather_insights.py          # Extract weather-related insights
│── 📂 docs/                         # Documentation
│   ├── description_of_the_files.md  # Overview of the dataset
│   ├── images_representations.md    # Description of satellite images, their coverage, and representations  
│   ├── reproject_images.md          # Explanation of the reprojection process, methods used
│   ├── merged_files.md              # Details on merging selected files, rationale for selection, and final output specifications  
│── requirements.txt                 # Project dependencies
│── install_gdal.sh                  # Correct installation of GDAL on the operating system and Python environment  
```