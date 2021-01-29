#!/usr/bin/env python
from multiprocessing import Pool
import subprocess
import os

def dailysync():
    """Grabs the current level of dirs and returns a tupple list with source and destination"""
    src = "../data/prod/"
    dest = "../data/prod_backup/"
    #subprocess.call(["rsync", "-arq", src, dest])
    tasks = []
    for path, dirs, files in os.walk(src):
        #print("{} - {} - {}").format(path, dirs, files)
        for dir in dirs:
            tasks.append((src+dir, dest+dir))
        break
    return tasks

def run(dir_tup):
    """Calls an rsync to run from the source to destination"""
    src, dest = dir_tup
    # Do something with task here
    print("Handling {} [to] {}".format(src, dest))
    subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
    """Run each process of file syncronization in a pool of cpus"""
    tasks = dailysync()
    #print(tasks)
    # Create a pool of specific number of CPUs
    p = Pool(len(tasks))
    # Start each task within the pool	
    p.map(run, tasks)