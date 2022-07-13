import re
import io
import tkinter as tk
from tkinter import filedialog

def prepare_data_dump(file_path, target):
    regex = re.compile('^\d*.\t')
    with io.open(file_path, 'r', encoding="utf-8", errors='replace') as current_file:
        with io.open(target, 'w', encoding="utf-8") as ready_file:
            print("Preparing file...")
            for line in current_file:
                    new_line = regex.sub("<p>", line)
                    new_line1 = new_line.replace("{[#", '')
                    new_line2 = new_line1.replace("]}", '') 
                    new_line3 = new_line2.replace("\n", '</p>\n')

                    ready_file.write(new_line3)
            ready_file.write('</p>')
    print('Successfully written to ' + target)

def main():
    print(" Select a file to prepare: ")
    file = filedialog.askopenfilename()
    target = filedialog.asksaveasfilename()
    prepare_data_dump(file, target)

main()
    
    
