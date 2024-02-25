#!/usr/bin/python3
""" 
Write a script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name 
"""

import os
import sys
import markdown2html


def convert_markdown_to_html(input_file):
    """Convert Markdown to HTML"""
    with open(input_file, 'r') as md_file:
        markdown_content = md_file.read()
        html_content = markdown2html.markdown(markdown_content)
    return html_content


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

    # Convert Markdown to HTML
    html_content = convert_markdown_to_html(input_file)

    # Write HTML content to the output file
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

    exit(0)
