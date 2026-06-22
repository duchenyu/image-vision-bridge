---
name: image-vision
description: >
  Local image vision bridge. When the user sends an image, invoke a local Ollama
  vision model (qwen3.5:4b) to describe the image in text, then feed the
  description back into the conversation. This lets text-only reasoning models
  "see" images without switching models.
trigger:
  - user sends an image file (png / jpg / gif / webp / bmp)
  - an image file path appears in the conversation
  - user asks to analyze, describe, or understand an image
  - the current model lacks native multimodal vision
---

# Image Vision Bridge

Bridge local vision models into text-only AI assistants.

When an image appears in the conversation and the current model cannot read
images natively, this skill automatically invokes a **local** Ollama vision
model to produce a text description, then feeds it back — so the assistant
can reason about the image without switching models.

## Quick Start

```bash
python scripts/describe_image.py "/path/to/image.png"
```

## How It Works

```
User sends image
       │
       ▼
Image path detected in conversation
       │
       ▼
skill: image-vision fires
       │
       ▼
describe_image.py ──▶ Ollama (qwen3.5:4b) ──▶ text description
       │
       ▼
Description injected back into conversation
       │
       ▼
Text-only model now "sees" the image
```

## Requirements

- **Ollama** installed and running (`ollama serve`)
- A vision-capable model pulled (recommended: `qwen3.5:4b`)

```bash
ollama pull qwen3.5:4b
```

## Model Options

| Model          | Size    | Quality      | Notes                        |
|----------------|---------|--------------|------------------------------|
| `qwen3.5:4b`   | ~3.4 GB | Good         | Fast, lightweight (default)  |
| `qwen3.5:9b`   | ~6.6 GB | Excellent    | More accurate, more VRAM     |
| `minicpm-v`    | ~5 GB   | Great        | Strong Chinese support       |
| `llava:7b`     | ~4 GB   | Decent       | Classic choice               |

## Custom Prompts

```bash
# Extract all text from the image
python scripts/describe_image.py photo.png --prompt "Extract ALL text visible in this image, character by character."

# Analyze a UI screenshot
python scripts/describe_image.py ui.png --prompt "This is a software UI screenshot. Describe layout, buttons, inputs, and interactions."

# Extract code from a screenshot
python scripts/describe_image.py code.png --prompt "Extract the complete code from this screenshot, preserving indentation."
```

## Troubleshooting

**Ollama model crashes** ("llama-server process has terminated"):
```powershell
# Windows (PowerShell)
Get-Process -Name "ollama*" | Stop-Process -Force
Start-Process ollama -ArgumentList "serve" -WindowStyle Hidden
```
```bash
# macOS / Linux
pkill ollama && ollama serve &
```

**Permission denied reading image**: make sure the script has read access to the image path.

## License

MIT — do whatever you want with it.
