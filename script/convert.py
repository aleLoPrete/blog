import os
import markdown
from bs4 import BeautifulSoup

# Define the input and output directories
md_dir = "md-posts/"
html_dir = "posts/"

# Create the HTML directory if it doesn't exist
os.makedirs(html_dir, exist_ok=True)

# Iterate through Markdown files in the md_dir
for filename in os.listdir(md_dir):
    if filename.endswith(".md"):
        md_path = os.path.join(md_dir, filename)
        html_filename = os.path.splitext(filename)[0] + ".html"
        html_path = os.path.join(html_dir, html_filename)

        # Read the content of the Markdown file
        with open(md_path, "r", encoding="utf-8") as md_file:
            md_content = md_file.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(
            md_content, extensions=["fenced_code", "codehilite"]
        )
        # Create the HTML structure
        html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Ale Lo Prete</title>
    <link rel="stylesheet" type="text/css" href="../style.css">
    <style>
    </style>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="../index.html">Home</a></li>
                <li><a href="../pages/about.html">About</a></li>
                <!-- Add links to other pages as needed -->
            </ul>
        </nav>
    </header>
    <div class="post-content">
        {html_content}
    </div>
</body>
</html>
        """

        # Write the HTML to the output file
        with open(html_path, "w", encoding="utf-8") as html_file:
            html_file.write(html_template)

print("Conversion and HTML generation completed.")
