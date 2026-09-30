# Project 1 — NSYSU Course Enrollment Scraper

## Motivation

As a Marketing Management Teaching Assistant (TA), I needed to organize student enrollment information for course management and administrative tasks.

The original process required manually collecting student information from the university's e-learning system and organizing the data into an Excel spreadsheet. This process was repetitive and time-consuming.

To improve efficiency and practice Python automation, I developed this project to automate the data collection and organization process.

## Project Objective

The main objectives of this project are:

* Automatically collect student enrollment information from the e-learning system
* Reduce repetitive manual data entry
* Organize the collected data using Pandas
* Export the final dataset into an Excel spreadsheet
* Improve the efficiency and consistency of the data-processing workflow

## Features

* Automated browser interaction with Selenium
* Automated login using environment variables
* Uses `WebDriverWait` to wait for page elements
* Collects student names and student numbers
* Handles multiple pages through pagination
* Organizes data using Pandas DataFrame
* Exports the final data to Excel

## Technologies

* Python
* Selenium
* Pandas
* openpyxl

## Project Workflow

```text
NSYSU E-learning System
          ↓
       Selenium
          ↓
    Data Collection
          ↓
        Pandas
          ↓
Data Organization
          ↓
        Excel
```

## Security

Login credentials are loaded through environment variables and are not stored directly in the source code.

Sensitive files and generated Excel files are excluded through `.gitignore`.

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

Set your login credentials as environment variables:

```bash
export NSYSU_USERNAME="your_username"
export NSYSU_PASSWORD="your_password"
```

Then run:

```bash
python3 project1.py
```

The program will collect the student enrollment data and export the results to an Excel file.

## Project Structure

```text
project1_github/
│
├── project1.py
├── requirements.txt
├── README.md
├── .gitignore
└── project1.xlsx        # Generated locally, not uploaded to GitHub
```
