#! /usr/bin/env python3

import os
import json
import requests


def get_feedback_files(path):
    """Return a list of files from the source dir and return them as a list"""
    # get list of feedback files
    txt_files = []
    for file in os.listdir(path):
        if file[-4:] == ".txt":
            txt_files.append(file)

    return txt_files


def txt_to_dictionary(src_dir, txt_file):
    """From a given feedback txt file that follows template returns a list"""
    # transform file contents to dictionary "title", "name", "date", "feedback"
    dictionary = {}
    with open(src_dir + txt_file) as file:
        print("Processing file: {}".format(file))
        line = file.readline().strip('\n')
        dictionary.update({"title": line})
        line = file.readline().strip('\n')
        dictionary.update({"name": line})
        line = file.readline().strip('\n')
        dictionary.update({"date": line})
        lines = file.readlines()
        dictionary.update({"feedback": "".join(lines).replace('\n', '')})
    return dictionary


def serialize_dict(dictionary):
    """Turn the dicionary into a serialized data (JSON)"""
    # serialize dictionary
    return json.dumps(dictionary)


def send_to_endpoint(serialized_data, url):
    """Send the serialized data to url"""
    # use requests to post to endpoint
    print("Sending JSON to: {}".format(url))
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, headers=headers, data=serialized_data)
    # check for errors response
    r.raise_for_status()
    return r


if __name__ == '__main__':
    src_dir = "/data/feedback/"
    for file in get_feedback_files(src_dir):
        dictio = txt_to_dictionary(src_dir, file)
        serialized_data = serialize_dict(dictio)
        url = "http://35.192.134.141/feedback/"
        response = send_to_endpoint(serialized_data, url)
        print(response.status_code)
