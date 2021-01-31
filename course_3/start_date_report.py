#!/usr/bin/env python3


import csv
import datetime
import requests


FILE_URL = "http://marga.com.ar/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer(this_date):
    """Returns the employees that started on the given date, or the closest one."""
    data = requests.get(FILE_URL, allow_redirects=True)
    open("employees-with-date.csv", "wb").write(data.content)
    with open("employees-with-date.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        
        # We want all employees that started at the same date or the closest newer
        # date. To calculate that, we go through all the data and find the
        # employees that started on the smallest date that's equal or bigger than
        # the given start date.
        this_date_employees = []
        reader = sorted(reader, key=lambda d: d['Start Date'], reverse=True)
        
        row_date = datetime.datetime.strptime(row["Start Date"], '%Y-%m-%d')
        
        final_date_employees.append((row["Name"], row["Surname"]))

    return final_date_employees

def list_newer(start_date):
    while start_date < datetime.datetime.today():
        first_name, last_name = get_same_or_newer(start_date)
        print("Started on {}: {} {}".format(start_date.strftime("%b %d, %Y"), first_name, last_name))

        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()