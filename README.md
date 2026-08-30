# Image Optimizer & WebP Converter

A Python command-line tool that dynamically resizes, compresses, and converts images on-the-fly using the [Image Optimizer and WebP Converter API on RapidAPI](https://rapidapi.com/rxmrb699/api/image-optimizer-and-webp-converter).

## Features
* **WebP Conversion:** Reduce image payload size by up to 70% compared to JPEG/PNG .
* **Smart Resizing:** Automatically calculates missing dimensions to preserve the original aspect ratio .
* **Adjustable Quality:** Fine-tune image quality vs. filesize for optimal loading speeds .

## Prerequisites
1. Sign up for a [RapidAPI](https://rapidapi.com/) account.
2. Subscribe to the [Image Optimizer and WebP Converter API](https://rapidapi.com/rxmrb699/api/image-optimizer-and-webp-converter) (The basic tier offers up to 1000 requests/month for free).
3. Obtain your `X-RapidAPI-Key`.

## Setup
Install the required `requests` library if you don't already have it:
```bash
pip install requests

```

Set your RapidAPI Key as an environment variable for security:

```bash
# On Linux/macOS
export RAPIDAPI_KEY="your_actual_api_key_here"

# On Windows (Command Prompt)
set RAPIDAPI_KEY=your_actual_api_key_here

# On Windows (PowerShell)
$env:RAPIDAPI_KEY="your_actual_api_key_here"

```

## Usage

Run the script via the command line. You can pass the source image URL, desired dimensions, format, and quality.

### Basic Example (Convert to WebP)

```bash
python image_optimizer.py --url "[https://picsum.photos/800/600](https://picsum.photos/800/600)" --output "optimized.webp"

```

### Advanced Example (Resize, convert to JPEG, set quality)

```bash
python image_optimizer.py --url "[https://picsum.photos/800/600](https://picsum.photos/800/600)" --output "resized.jpeg" --width 400 --format jpeg --quality 85

```

### CLI Arguments

* `--url` (Required): Source image URL.
* `--output` (Required): Output file path.
* `--width`: Output width in pixels (1-4000). If omitted but height is provided, maintains aspect ratio .


* `--height`: Output height in pixels (1-4000). If omitted but width is provided, maintains aspect ratio .


* `--format`: Output format (`webp`, `jpeg`, or `png`). Defaults to `webp` .


* `--quality`: Compression quality (1-100). Defaults to `80` .

### Quick Start Guide

As requested, before running the Python program, make sure you complete the RapidAPI setup:
1. Go to the [Image Optimizer and WebP Converter API on RapidAPI](https://rapidapi.com/rxmrb699/api/image-optimizer-and-webp-converter).
2. Click **Subscribe to Test** (you will get up to 1000 API calls per month for free).
3. Copy your `X-RapidAPI-Key` from the Endpoints dashboard.
4. Set the environment variable in your terminal to keep your credentials secure:
   ```bash
   export RAPIDAPI_KEY="your_actual_api_key_here"

```

