# Web Scraping Tool

This is a standard web scraping tool designed to fetch HTML content from websites. The tool consists of various components organized within a folder structure.

## Folder Structure


## Components

### `get_links`
This folder contains a Python script (`get_links.py`) to fetch all the links of topics and subtopics from a given URL. The fetched links are stored in CSV format within the `input_data` subfolder.

### `input_data`
This folder stores all the href links from the given HTML page in CSV format. These links are later used for scraping.

### `main2.py`
This Python script utilizes the href links fetched by `get_links.py` to scrape data. The scraped data, including URL, heading, text, links, and code, are outputted to a CSV file named `output.csv` in the `output_data` folder.

### `output_data`
This folder stores the web scraped data fetched from the web pages. The data is stored in CSV format.

### `script.py`
This script combines all the components and runs them automatically in serial order. The input filename can be provided as an argument to the script.

## Usage

1. Manually insert the URL for the required webpage inside `get_links.py` along with its class name.
2. Run `script.py` with the desired input filename as an argument to initiate the scraping process.

## Notes

- All the relative href links are included in the code. Links of third-party websites whose data is not needed are excluded.
- Currently, the data of Tron docs is stored inside the `output_data` folder.
