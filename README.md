
# HTML Body Content Cleaner

This Python script fetches an HTML page from a provided URL, cleans the content inside the `<body>` tag, and saves it to a local file. The script is designed for extracting clean, readable HTML content by removing all unnecessary tags, attributes, and layout-related elements.

## Features

- Only processes content inside the `<body>` tag
- Removes scripts, styles, SVGs, navs, and titles
- Strips all attributes (like `class`, `id`, `style`)
- Unwraps layout elements (`div`, `section`, etc.) to flatten content
- Removes HTML comments
- Outputs simplified, readable HTML with original semantics

## Usage

### Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

Install dependencies:
```bash
pip install requests beautifulsoup4
```

### Run the script

Edit the `url` and `output_file` fields in the script or pass them dynamically. Then run:
```bash
python html_textonly.py
```

## Example

If `url = "https://example.com"` and `output_file = "cleaned-text.html"`, the resulting file will contain all cleaned content inside the `<body>` tag, without any layout wrappers or extraneous HTML attributes.

## License

MIT
