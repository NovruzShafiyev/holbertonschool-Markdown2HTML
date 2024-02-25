import os
import sys

if __name__ == "__main__":
    args = sys.argv

    if len(args) < 3:
        sys.stderr.write("Usage: ./markdown2html.py <input_file.md> <output_file.html>\n")
        sys.exit(1)

    input_file = args[1]
    output_file = args[2]

    if not os.path.exists(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    # Add the code for actual Markdown to HTML conversion here
    # For example, using the markdown library:
    import markdown

    with open(input_file, 'r') as md_file, open(output_file, 'w') as html_file:
        html_content = markdown.markdown(md_file.read())
        html_file.write(html_content)

    sys.exit(0)
