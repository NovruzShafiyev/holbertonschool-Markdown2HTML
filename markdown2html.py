
import os
import sys
import markdown2html

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py <input_file.md> <output_file.html>", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

with open(input_file, 'r') as file:
    markdown_text = file.read()

html_content = markdown2html.markdown(markdown_text)

with open(output_file, 'w') as file:
    file.write(html_content)

sys.exit(0)

