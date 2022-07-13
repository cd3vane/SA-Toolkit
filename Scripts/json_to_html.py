import json
import re
from os import listdir
from os.path import isfile, join
import tkinter as tk
from tkinter import filedialog, simpledialog

def check_if_plain_quotes(line):
    line = line.strip()
    regex = re.compile(r'^[a-zA-Z \%]{2,}$')
    if(regex.match(line)):
        return True
    else:
        return False

def json_parse(path, save_location,  key_list):
    for key in key_list:
        print('\nFinding nodes with ' + key + '...')
        count = 0
        with open(path, encoding="utf8") as current_file:
            with open(save_location, 'a', encoding="utf8") as parsed_file:
                data = current_file.readlines()
                for line in data:
                    line = line.replace('\"', '')
                    line = line.replace(',', '')
                    
                    if(check_if_plain_quotes(line)):
                        line = "".join(('<p>', line.strip(), '</p>\n'))
                        parsed_file.write(line)
                    else:
                        line_split = line.split(':')

                        if(line_split[0].strip() == key):
                            count += 1
                            line = "".join(('<p>', line_split[1].strip(), '</p>\n'))
                            parsed_file.write(line)

                if(count != 0):
                    print('Found ' + str(count) + ' instances of ' + key + ' in ' + path)
                else:
                    print(key + ' was not found in ' + path + ' either something went wrong or you have a typo')

def main():
    root = tk.Tk()
    root.withdraw()

    files_to_parse = filedialog.askopenfilenames(parent=root, title='Choose a json file to convert', filetypes=[('Json files', '*.json')])
    print('Parsing...')
    print(files_to_parse)

    slice_path = files_to_parse[0].split('/')
    directory = "/".join(slice_path[:-1])

    number_of_keys = simpledialog.askinteger("Input", "How many keys would you like to parse?")
    keys = []
    for i in range(number_of_keys):
        key = simpledialog.askstring("Key", "Enter a key")
        keys.append(key)
    print('\n\nSearching for the following: ')
    print(keys)

    save_location = filedialog.asksaveasfilename(parent=root, title='Save HTML output', filetypes=[('HTML File', '*.html')])

    for file in files_to_parse:
        json_parse(file, save_location, keys)

    print('Successfully wrote to ' + save_location )


if __name__ == '__main__':
    main()