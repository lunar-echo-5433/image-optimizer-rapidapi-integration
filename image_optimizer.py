import argparse
import os

def optimize_image(api_key, image_url, output_file, width=None, height=None, img_format="webp", quality=80):
    \"\"\"
    Optimizes and resizes an image using the Image Optimizer & WebP Converter API.
    \"\"\"
    url = "https://image-optimizer-and-webp-converter.p.rapidapi.com/v1/optimize"
    
    # Build query parameters
    querystring = {
        "url": image_url,
        "format": img_format,
        "quality": quality
    }
    if width:
        querystring["width"] = width
    if height:
        querystring["height"] = height

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "image-optimizer-and-webp-converter.p.rapidapi.com"
    }

    print(f"Sending request to optimize {image_url}...")
    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        with open(output_file, 'wb') as f:
            f.write(response.content)
        print(f"Success! Image saved to {output_file}")
    else:
        print(f"Failed to optimize image. HTTP Status: {response.status_code}")
        print(f"Error details: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Optimize and convert images via RapidAPI.")
    parser.add_argument("--url", required=True, help="Source image URL (e.g., https://picsum.photos/800/600)")
    parser.add_argument("--output", required=True, help="Output file path (e.g., output.webp)")
    parser.add_argument("--width", type=int, help="Output width in pixels (1-4000)")
    parser.add_argument("--height", type=int, help="Output height in pixels (1-4000)")
    parser.add_argument("--format", default="webp", choices=["webp", "jpeg", "png"], help="Output format (webp, jpeg, png)")
    parser.add_argument("--quality", type=int, default=80, help="Compression quality (1-100)")
    
    args = parser.parse_args()
    
    # Ideally, keep the API key in environment variables rather than hardcoding.
    RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
    if not RAPIDAPI_KEY:
        print("Error: Please set the RAPIDAPI_KEY environment variable.")
        exit(1)
        
    optimize_image(
        api_key=RAPIDAPI_KEY,
        image_url=args.url,
        output_file=args.output,
        width=args.width,
        height=args.height,
        img_format=args.format,
        quality=args.quality
    )
