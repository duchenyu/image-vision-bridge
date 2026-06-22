#!/usr/bin/env python3
"""
Local Vision Model Bridge — Describe images using a local Ollama vision model.

Usage:
    python describe_image.py <image_path> [--model qwen3.5:4b] [--prompt "custom prompt"]

Output: Plain text image description printed to stdout.
"""

import sys
import os
import json
import base64
import argparse
import urllib.request
import urllib.error


OLLAMA_API = "http://127.0.0.1:11434/api/chat"
DEFAULT_MODEL = "qwen3.5:4b"
DEFAULT_PROMPT = (
    "Please describe this image in detail. Include: main objects, scene, "
    "text content, colors, layout, atmosphere — everything you can see."
)


def encode_image(image_path: str) -> str:
    """Read an image file and encode it as base64."""
    if not os.path.isfile(image_path):
        print(f"[ERROR] Image file not found: {image_path}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    except Exception as e:
        print(f"[ERROR] Failed to read image: {e}", file=sys.stderr)
        sys.exit(1)


def call_ollama_vision(image_path: str, model: str, prompt: str) -> str:
    """Send image to Ollama vision model and return text description."""
    b64 = encode_image(image_path)

    payload = {
        "model": model,
        "stream": False,
        "messages": [
            {
                "role": "user",
                "content": prompt,
                "images": [b64],
            }
        ],
    }

    try:
        req = urllib.request.Request(
            OLLAMA_API,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            content = result.get("message", {}).get("content", "")
            return content.strip()
    except urllib.error.URLError as e:
        print(
            f"[ERROR] Cannot connect to Ollama (is it running?): {e}",
            file=sys.stderr,
        )
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Vision model call failed: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Describe an image using a local Ollama vision model."
    )
    parser.add_argument("image", help="Path to the image file")
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Ollama model name (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--prompt",
        default=DEFAULT_PROMPT,
        help="Custom prompt for the vision model",
    )
    args = parser.parse_args()

    print(
        f"[INFO] Analyzing image with {args.model}: {args.image}",
        file=sys.stderr,
    )
    description = call_ollama_vision(args.image, args.model, args.prompt)
    print(description)


if __name__ == "__main__":
    main()
