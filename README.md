# Amazon Bestsellers Analysis

A beginner-friendly Python data analysis project using **Pandas** to import Amazon bestseller data from a CSV file and analyze it.

## Features

- Imports data from a `.csv` file using Pandas
- Cleans column names
- Converts common numeric fields such as price, rating, and review count
- Shows:
  - Number of rows and columns
  - Available columns
  - Missing values
  - Statistical summary
  - Top products by rating, reviews, review count, ratings count, or price
  - Most common category/brand/author/genre when available
- Creates simple charts when `rating` or `price` columns exist

## Project Structure

```text
amazon-bestsellers-analysis/
├── amazon_bestsellers_analysis.py
├── amazon_bestsellers.csv
├── requirements.txt
├── README.md
├── .gitignore
└── charts/
```

## Dataset

Put your Amazon bestseller CSV file in the project folder and name it:

```text
amazon_bestsellers.csv
```

The project is designed to work with common columns such as:

- Product
- Price
- Rating
- Reviews
- Category
- Brand

Your exact CSV does not have to contain all of these columns.

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Run

```bash
python amazon_bestsellers_analysis.py
```

The analysis will be printed in the terminal.

Charts will be saved inside the `charts/` folder.

## GitHub

1. Create a new GitHub repository named `amazon-bestsellers-analysis`.
2. Upload the project files.
3. Do not upload private data or credentials.
4. Add your CSV file only if its license/usage terms allow redistribution.

## Technologies

- Python
- Pandas
- Matplotlib
- CSV
