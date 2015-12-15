#!/usr/bin/python
import sys
import os
import re
import operator

# Populate an empty dictionary with values from a particular log file
def populate(proc_dict, file_path):
    proc_pattern = re.compile("\S*\[\d*\]")
    date_pattern = re.compile(".{3}\d{2} \d{2}:\d{2}")

    with open(file_path, "r") as file:
        lines = file.readlines()

        for line in lines:
            proc = proc_pattern.search(line)
            date = date_pattern.search(line)
            if proc is None or date is None:
                pass
            else:     
                proc_str = proc.group()
                date_str = date.group()

                if(proc_str not in proc_dict.keys()):
                    proc_dict[proc_str] = 0
                proc_dict[proc_str] += 1

# Returns the file path if one is supplied and is valid
# Exits if one of the previous conditions isn't satisfied
def get_file_path():
    # Check if file path is supplied
    if len(sys.argv) < 2:
        print("ERROR:\tNo file path specified")
        sys.exit(0)

    file_path = sys.argv[1]

    # Check if the file exists
    if os.path.exists(file_path) == False:
        print("ERROR:\tFile \"{}\" does not exist.".format(file_path))
        sys.exit(0)

    return file_path

if __name__ == "__main__":

    proc_dict = {}
    populate(proc_dict, get_file_path())

    # Sort the dictionary by value (ascending order)
    sorted = sorted(proc_dict.items(), key=operator.itemgetter(1))

    # Print out formatted tuples of processes and their occurences in the log
    for (proc, count) in sorted:
        print("Count: {}\t\tProcess: {}".format(count, proc))
