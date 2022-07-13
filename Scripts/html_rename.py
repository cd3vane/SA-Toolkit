import os
import tkinter as tk
from bs4 import BeautifulSoup
from tkinter import filedialog, simpledialog

def main():
    HTML_TAG = 'title'

    root = tk.Tk()
    root.withdraw()

    directory = filedialog.askdirectory(parent=root)

    print(os.listdir(directory))

    for filename in os.listdir(directory):
        if filename.endswith(".html"): 
            full_path = os.path.join(directory, filename)
            with open(full_path, 'r', encoding="utf8") as html:
                soup = BeautifulSoup(html, 'html.parser')
                title = soup.find(HTML_TAG).text
                title = title.lower()
            if(title.__contains__('|')):
                title_split = title.split('|')
                title = title_split[0].replace(' ', '_')
            else:
                title = title.replace(' ', '_')
            os.rename(full_path, os.path.join(directory, title[:-1] + '.html'))


if __name__ == '__main__':
    main()