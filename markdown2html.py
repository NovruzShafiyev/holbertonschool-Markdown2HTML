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


def convert_unordered_list(markdown_lines):
    ''' Convert Markdown unordered list to HTML '''
    html_lines = []
    in_list = False
    for line in markdown_lines:
        line = line.strip()
        if line.startswith('-'):
            if not in_list:
                html_lines.append('<ul>\n')
                in_list = True
            line = line.lstrip('-').strip()
            html_lines.append(f'    <li>{line}</li>\n')
        else:
            if in_list:
                html_lines.append('</ul>\n')
                in_list = False
            html_lines.append(line)
    if in_list:
        html_lines.append('</ul>\n')
    return html_lines


if __name__ == "__main__":
    '''the number of arguments is less than 2'''
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)
    '''Markdown file doesn’t exist'''
    if not path.exists(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        sys.exit(1)

    # Convert Markdown to HTML
    with open(sys.argv[1], 'r') as markdown_file:
        markdown_lines = markdown_file.readlines()

    html_lines_heading = [convert_heading(line) for line in markdown_lines]
    html_lines = convert_unordered_list(html_lines_heading)

    # Write HTML to output file
    with open(sys.argv[2], 'w') as html_file:
        html_file.writelines(html_lines)

    sys.exit(0)
