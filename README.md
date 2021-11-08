# H1B Job Finder
- H1B Job Finder searches for past H1B Visa jobs by **company**, **city**, and **job title**.
- The program uses the [myVisaJobs](https://www.myvisajobs.com/Reports/) Database to retreive up-to-date information.

## Installation
---
1. Download the project folder.
2. Relocate the project folder to a prefered location on your device.

## Running H1B Job Finder
---
### Option 1: Run Program through Terminal
- Nagivate to your terminal.
- Ensure python is up-to-date **(Python 3.9.7)** with `python --version` or `python3 --version`.
- Run `main.py` using the command `python [file path]` or `python3 [file path]`
    - Find the file path by copying from finder, or by draging and droping the file into terminal.
    - For Example, with the file path `/Users/User/Documents/H1B_Job_Finder/main.py`, the code should appear as follows:
    ```
    Computer-Name:~ User$ python /Users/User/Documents/H1B_Job_Finder/main.py
    ```
- Follow the instructions in the program.

    *Please note that using terminal may result in reduced quality for the presentation of data. Use Option 2 for better quality data presentation.*

### Option 2: Run Program through Visual Studio Code
- Download **Visual Studio Code** for your OS version. Please use the [most recent version](https://code.visualstudio.com/Download).
- Open **Visual Studio Code**
- Under the *Extensions* tab, ensure that *Python*, *Pylance*, *Jupyter Keymap*, and *Jupyter* are installed.
- Navigate to the **H1B Job Finder** program folder using VS Code's *File Explorer*.
- Click on `main.py` and run the file using Jupyter.
- Follow the instructions in the program.

### Option X: The Unknown Method
- There are definitely other ways to run this file.
- I am not yet knowledgeable enough to explain them.
- I will report back when I am.

## Project Map
---
The project map describes the files contained therein, their respective purposes, and their functionality.
```
main.py
│   def main(): entry point, guides user through program
│ 
└── databasesearcher.py
    │   Class OverallDataSearcher(): initializes instance for full company database with city locations
    │       def find_job_keyword(): Selects rows that meet keyword requirement
    │       def find_company(): Selects rows that meet company name requirement
    │       def find_exact_job_title(): Selects rows that meet job title requirement
    │   
    │   Class CityDataSearcher(): initializes instance for city company database
    │       def find_city_job_keyword(): Selects rows that meet keyword requirement
    │       def find_city_company(): Selects rows that meet company name requirement
    │       def find_city_exact_job_title(): Selects rows that meet job title requirement
    │
    ├── parsealldata.py
    │   │   def parse_all_data(): Iterates through database for companies, retreives position and total count, appends to DataFrame
    │   │
    │   └── getdata.py
    │       │   def get_data(): Retreives HTML from given URL
    │       │
    │       └── geturl.py
    │               def get_url(): Creates url for companies in myVisaJobs Database based on City input
    │
    └── parsecitydata.py
        │   def parse_city_data(): Iterates through database for companies, retreives position and single-city count, appends to DataFrame
        │
        └── getdata.py
            │   def get_data(): Retreives HTML from given URL
            │
            └── geturl.py
                    def get_url(): Creates url for companies in myVisaJobs Database based on City input
```
