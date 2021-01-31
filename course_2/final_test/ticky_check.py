#!/usr/bin/env python3

import sys
import re
import operator
import csv
import subprocess

def filter_error_logs(log_file, csv_filename):
    pattern_error = r"ERROR (\w.*)\s\(" #[1] error description
    error = {}
    #grab the syslog
    with open(log_file) as file:
        #read each line
        for line in file:
            #filter the correct info
            result = re.findall(pattern_error, line.strip())
            if result is None or len(result) < 1:
                continue
            #move to a dictionary
            #if not found pass 0 creating the entry, else add + 1
            error[result[0]] = error.get(result[0], 0) + 1
    error = sorted(error.items(), key=operator.itemgetter(1), reverse=True) 
    #write in csv
    with open(csv_filename, 'w') as f:
        w = csv.writer(f)
        w.writerow(["Error", "Count"])
        for line in error:
            motive, count = line
            w.writerow([motive, count])

def filter_user_logs(log_file, csv_filename):
    pattern_username = r"ticky: ([A-Z]*) .*\(([a-z]*)\)"  #[1] ERROR or INFO [2] username
    per_user = {}
    #grab the syslog
    with open(log_file) as file:
        #read each line
        for line in file:
            #filter the correct info
            result = re.findall(pattern_username, line.strip())
            if result is None or len(result) < 1:
                continue
            #move to a dictionary
            error, user = result[0]
            per_user.setdefault(user, {"INFO":0, "ERROR":0})
            #check where the entry belongs and add 1
            if error == "INFO":
                per_user[user]["INFO"] += 1
            elif error == "ERROR":
                per_user[user]["ERROR"] += 1
    
    per_user = sorted(per_user.items(), key = lambda x: x[1]["INFO"])
    #create user nested dic
    per_user_ordered = []
    for entry in per_user:
        user, errors = entry
        per_user_ordered.append({"Username" : user , "INFO": errors["INFO"], "ERROR":errors["ERROR"]})
    #write in csv
    with open(csv_filename, 'w') as f:
        w = csv.DictWriter(f, ["Username", "INFO", "ERROR"])
        w.writeheader()
        w.writerows(per_user_ordered)


if __name__ == "__main__":
    log_file = sys.argv[1]
    filter_error_logs(log_file, "./error_message.csv")
    filter_user_logs(log_file, "./user_statistics.csv")
    sys.exit(0)