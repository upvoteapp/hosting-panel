import os

def make_html(js_file, css_file):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <link rel="icon" type="image/png" href="/logo.png">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Upvote</title>
        <script type="module" crossorigin src="/assets/{js_file}"></script>
        <link rel="stylesheet" href="/assets/{css_file}">
    </head>
    <body>
        <div id="app"></div>
        
    </body>
    </html>

    """

# Parse all js and css by filtering by .css and .js, then matching them by filtering out '-' before each one in for loop then writing it to a html file named after the view in lowercase.

def parse_all_js_css():
    js_files = []
    css_files = []
    for file in os.listdir('./dist/assets'):
        if file.endswith('.js'):
            js_files.append(file)
        elif file.endswith('.css'):
            css_files.append(file)

    html_files = []
    for js_file, css_file in zip(js_files, css_files):
        html_file = f'./dist/{js_file[:-3].lower()}.html'
        html_files.append(html_file)

    for html_file in html_files:
        with open(html_file, 'w') as f:
            f.write(make_html(js_file, css_file))
            print(f"DONE! {html_file}")
            
if __name__ == '__main__':
    parse_all_js_css()