#!/usr/bin/python3
''' Markdown to HTML '''
import sys
from os import path


def convert_heading(line):
    ''' Convert Markdown heading to HTML '''
    if line.startswith('#'):
        count = line.count('#')
        tag = 'h' + str(count)
        text = line.strip('#').strip()
        return f'<{tag}>{text}</{tag}>\n'
    else:
        return line


if __name__ == "__main__":
    '''the number of arguments is less than 2'''
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)
    '''Markdown file doesn’t exist'''
    if not path.exists(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], 'r') as markdown_file:
        markdown_lines = markdown_file.readlines()

    html_lines = [convert_heading(line) for line in markdown_lines]

    with open(sys.argv[2], 'w') as html_file:
        html_file.writelines(html_lines)

    sys.exit(0)
