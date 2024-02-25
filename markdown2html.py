#!/usr/bin/python3

import sys
import os
import markdown2html

def main():
    """Converts a Markdown file to HTML.

    Args:
        sys.argv: List of command-line arguments.

    Returns:
        None. Exits with error code 0 on success, 1 otherwise.
    """

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file.md> <output_file.html>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    with open(input_file, 'r') as file:
        markdown_text = file.read()

    html_content = markdown2html.markdown(markdown_text)

    output_file = sys.argv[2]
    with open(output_file, 'w') as file:
        file.write(html_content)

    # Success
    sys.exit(0)

if __name__ == "__main__":
    main()
