#!/usr/bin/python3
""" 
Write a script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name 
"""

import os
import sys



if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    input_file = args[1]
    output_file = args[2]

    if not os.path.exists(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        exit(1)


    exit(0)