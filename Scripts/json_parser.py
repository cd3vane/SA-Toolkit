import json
from os import listdir
from os.path import isfile, join
import tkinter as tk
from tkinter import filedialog, simpledialog

root = tk.Tk()
root.withdraw()
def json_parse(path, save_location,  key):
    with open(path, encoding="utf8") as current_file:
        with open(save_location, 'a', encoding="utf8") as parsed_file:
            data = current_file.readlines()
            for line in data:
                line = line.replace('\"', '')
                line_split = line.split(':')
                if(line_split[0].strip() == key):
                    print(line_split[0])
                    parsed_file.write('<p>' + line_split[1] + '</p>\n')
                

def get_file_names(directory):
    return [f for f in listdir(directory) if isfile(join(directory, f))]

def parse_directory():
    files_to_parse = filedialog.askopenfilenames(parent=root, title='Choose a file')
    print(files_to_parse)
    slice_path = files_to_parse[0].split('/')
    directory = "/".join(slice_path[:-1])
    
    key = simpledialog.askstring('Enter Key', 'Enter your key: ')
    count = 0
    save_location = filedialog.asksaveasfilename()
    for file in files_to_parse:
        print(file)
        json_parse(file, save_location, key)
        count+=1
    print('Successfully wrote to file parsed.txt ' + str(count) + ' times')

parse_directory()
