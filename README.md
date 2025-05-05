# Climate Power Forecast - Data Processing

This repository contains the data processing pipeline for the Climate Power Forecast project. It downloads and processes climate data from CORDEX, which is then used by the web application to visualize wind power generation forecasts.

> **Web Application**: The processed data from this repository is used by our interactive web platform at [climate-power-forecast-app](https://github.com/gutobenn/climate-power-forecast-app)

## Data

The project uses climate data from CORDEX. The data needs to be downloaded and stored in the `data/` directory. This processed data is then exported in a format suitable for the web application.

## Getting Started

1. Clone this repository
2. Install required dependencies
3. Download the data:
   - Run the scripts in `scripts/download_data/` folder
   - Move the downloaded files to the `data/` folder
4. Run the analysis:
   - Open `8.5 wind power CPF.ipynb`
   - Execute the first cell to set up the environment, load the data and exported the proccess data for the web application