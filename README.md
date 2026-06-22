# 🖼️ Image Vision Bridge

> **Let text-only AI models "see" images — using a local vision model as a bridge. No API keys. No cloud. No model switching.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Ollama](https://img.shields.io/badge/Ollama-Ready-black?logo=ollama)](https://ollama.com)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-green?logo=python)](https://python.org)
[![Model: qwen3.5](https://img.shields.io/badge/Vision-qwen3.5:4b-orange)](https://ollama.com/library/qwen3.5)

---

[English](#english) | [中文](#中文)

---

## English

### The Problem

You're using a powerful reasoning model (DeepSeek-V4, DeepSeek-R1, o1, Qwen-Max...) but it **can't read images**. Every time you need image understanding, you have to switch to a multimodal model, breaking your workflow. Frustrating.

### The Solution

**Image Vision Bridge** is a lightweight skill for AI coding assistants (WorkBuddy, CodeBuddy, Claude Code) that uses a **local** Ollama vision model to describe images in text. Your text-only model gets the description injected back into the conversation — it "sees" the image without you ever switching models.

> 💡 **All processing stays on your machine. No API keys. No data leaves your computer.**

### Features

- 🔒 **100% Local & Private** — runs entirely on your hardware via Ollama
- ⚡ **Tiny footprint** — default model is qwen3.5:4b (~3.4 GB), fits on any modern GPU
- 🌍 **Multi-language** — Qwen models natively support Chinese, English, and more
- 🎯 **Zero config** — install the skill, pull one model, you're done
- 🧩 **Works with any AI assistant** — WorkBuddy, CodeBuddy, Claude Code, Cursor, etc.
- 📝 **Customizable prompts** — extract text, analyze UI, read code screenshots, whatever you need

### Quick Start (2 minutes)

```bash
# 1. Install Ollama (skip if already installed)
#    macOS/Linux: curl -fsSL https://ollama.com/install.sh | sh
#    Windows:     https://ollama.com/download

# 2. Pull the vision model (~3.4 GB)
ollama pull qwen3.5:4b

# 3. Install the skill into your assistant
cp -r image-vision ~/.workbuddy/skills/image-vision
# or: cp -r image-vision ~/.codebuddy/skills/image-vision

# 4. Done! Send an image and watch it work.
```

### How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                     YOUR AI ASSISTANT                       │
│                                                             │
│  "What's in this screenshot?"    ← text-only model          │
│       │                          (can't see images)         │
│       │                                                     │
│       ▼                                                     │
│  ┌─────────────┐   base64    ┌──────────────┐              │
│  │  describe_   │──────────▶ │   Ollama     │              │
│  │  image.py    │            │  qwen3.5:4b  │              │
│  └─────────────┘   text ◀─── │  (local GPU) │              │
│       │          description  └──────────────┘              │
│       ▼                                                     │
│  "The image shows a login form with                        │
│   email/password fields and a blue                         │
│   'Sign In' button in the center..."                       │
│                                                             │
│  ✅ Text model now reasons about the image!                 │
└─────────────────────────────────────────────────────────────┘
```

### Supported Vision Models

| Model | Size | Quality | Best For |
|-------|------|---------|----------|
| `qwen3.5:4b` ⭐ | 3.4 GB | ★★★★☆ | Daily use, fast startup |
| `qwen3.5:9b` | 6.6 GB | ★★★★★ | High-accuracy tasks |
| `minicpm-v` | ~5 GB | ★★★★☆ | Strong Chinese support |
| `llava:7b` | ~4 GB | ★★★☆☆ | Legacy compatibility |
| `gemma3:12b` | ~7 GB | ★★★★★ | Latest Google model |

### Advanced Usage

```bash
# Extract text from a document scan
python scripts/describe_image.py scan.png \
  --prompt "OCR: extract all text from this image, preserving line breaks."

# Analyze a UI design mockup
python scripts/describe_image.py design.png \
  --prompt "Describe this UI mockup: layout, components, colors, and spacing."

# Read a code screenshot and reproduce the code
python scripts/describe_image.py code_screenshot.png \
  --prompt "Extract the complete source code visible in this screenshot, preserving all indentation."

# Summarize a chart or graph
python scripts/describe_image.py chart.png \
  --prompt "Describe what this chart shows, including axes labels, trends, and data points."

# Use a different model
python scripts/describe_image.py photo.jpg --model qwen3.5:9b
```

### Requirements

- **Ollama** v0.3+ ([install guide](https://ollama.com))
- **Python** 3.9+ (standard library only — no pip install needed)
- **VRAM**: ~4 GB for qwen3.5:4b, ~7 GB for qwen3.5:9b
- Works on **macOS, Linux, Windows** (anywhere Ollama runs)

### Why Local?

| | Local (this skill) | Cloud API (GPT-4V, Claude) |
|---|---|---|
| Privacy | ✅ Data never leaves your PC | ❌ Images sent to cloud |
| Cost | ✅ Free | ❌ Pay per image |
| Speed | ✅ ~2-5 sec (after first load) | ⚠️ API latency |
| Internet | ✅ Works offline | ❌ Requires connection |
| Rate limits | ✅ Unlimited | ❌ API quotas |

---

## 中文

### 痛点

你正在用 DeepSeek-V4、DeepSeek-R1、Qwen-Max 这类超强推理模型干活，但它**读不了图片**。每次要看图都得切模型，工作流被打断，烦得要死。

### 解决方案

**Image Vision Bridge** 是一个 AI 编程助手（WorkBuddy / CodeBuddy / Claude Code）的技能插件——用**本地** Ollama 视觉模型把图片翻译成文字描述，再自动注回对话里。你的纯文本模型就"看见"图片了，全程不用切换。

> 💡 **所有处理都在你本地机器上完成，不需要 API Key，数据不离开你的电脑。**

### 特性

- 🔒 **100% 本地运行** — 基于 Ollama，数据不出本机
- ⚡ **极小体积** — 默认模型 qwen3.5:4b 仅 3.4 GB，任何现代 GPU 都跑得动
- 🌍 **多语言原生支持** — Qwen 模型天然支持中英文及更多语言
- 🎯 **零配置** — 装好 skill、拉一个模型，完事
- 🧩 **兼容所有 AI 助手** — WorkBuddy、CodeBuddy、Claude Code、Cursor 等
- 📝 **自定义提示词** — 提取文字、分析 UI、读代码截图，随你定制

### 快速开始（2 分钟）

```bash
# 1. 安装 Ollama（如已装则跳过）
#    macOS/Linux: curl -fsSL https://ollama.com/install.sh | sh
#    Windows:     https://ollama.com/download

# 2. 拉取视觉模型（约 3.4 GB）
ollama pull qwen3.5:4b

# 3. 安装 skill 到你的 AI 助手
cp -r image-vision ~/.workbuddy/skills/image-vision
# 或: cp -r image-vision ~/.codebuddy/skills/image-vision

# 4. 搞定！发张图试试效果。
```

### 工作原理

```
┌─────────────────────────────────────────────────────────────┐
│                      你的 AI 助手                            │
│                                                             │
│  "这张截图里有什么？"          ← 纯文本推理模型               │
│       │                        （原生不支持读图）             │
│       │                                                     │
│       ▼                                                     │
│  ┌─────────────┐   base64    ┌──────────────┐              │
│  │  describe_   │──────────▶ │   Ollama     │              │
│  │  image.py    │            │  qwen3.5:4b  │              │
│  └─────────────┘   文字◀───  │  (本地 GPU)  │              │
│       │          描述         └──────────────┘              │
│       ▼                                                     │
│  "图片显示一个白色背景的登录界面，                          │
│   中间有邮箱和密码输入框，底部是                            │
│   一个蓝色的'登录'按钮..."                                  │
│                                                             │
│  ✅ 推理模型现在能分析图片内容了！                           │
└─────────────────────────────────────────────────────────────┘
```

### 支持的视觉模型

| 模型 | 大小 | 效果 | 适用场景 |
|------|------|------|----------|
| `qwen3.5:4b` ⭐ | 3.4 GB | ★★★★☆ | 日常使用，启动最快 |
| `qwen3.5:9b` | 6.6 GB | ★★★★★ | 高精度需求 |
| `minicpm-v` | ~5 GB | ★★★★☆ | 中文场景最强 |
| `llava:7b` | ~4 GB | ★★★☆☆ | 经典兼容 |
| `gemma3:12b` | ~7 GB | ★★★★★ | Google 最新模型 |

### 高阶用法

```bash
# 提取文档扫描件中的文字（OCR）
python scripts/describe_image.py scan.png \
  --prompt "请逐字提取图片中的所有文字，保留换行。"

# 分析 UI 设计稿
python scripts/describe_image.py design.png \
  --prompt "这是一个UI设计稿，请分析布局、组件、配色和间距。"

# 读取代码截图并还原代码
python scripts/describe_image.py code_screenshot.png \
  --prompt "完整提取截图中可见的源代码，保留所有缩进。"

# 解读图表
python scripts/describe_image.py chart.png \
  --prompt "描述这张图表的内容，包括坐标轴标签、趋势和数据点。"

# 换个模型
python scripts/describe_image.py photo.jpg --model qwen3.5:9b
```

### 为什么选本地？

| | 本地方案（本 skill） | 云端 API（GPT-4V 等） |
|---|---|---|
| 隐私 | ✅ 数据不出本机 | ❌ 图片上传到云端 |
| 费用 | ✅ 完全免费 | ❌ 按张计费 |
| 速度 | ✅ 2-5 秒（首次加载后） | ⚠️ API 延迟 |
| 网络 | ✅ 离线可用 | ❌ 需要联网 |
| 调用限制 | ✅ 无限制 | ❌ API 配额限制 |

---

## Install via SkillHub

```bash
# Coming soon — submit to SkillHub marketplace
# For now, clone and copy:
git clone https://github.com/duchenyu/image-vision-bridge.git
cp -r image-vision-bridge ~/.workbuddy/skills/image-vision
```

## FAQ

**Q: Does this work with any AI assistant?**
A: Yes — it's designed for WorkBuddy/CodeBuddy skill system, but the core script (`describe_image.py`) is a standalone Python script. Any assistant that can run shell commands can use it.

**Q: How fast is it?**
A: First call: ~15-30 sec (model loads into VRAM). Subsequent calls: 2-5 sec. qwen3.5:4b is specifically optimized for fast inference.

**Q: What GPU do I need?**
A: qwen3.5:4b needs ~4 GB VRAM. Works on RTX 2060+, GTX 1660 Ti+, Apple M1+, or any GPU with 4+ GB. Falls back to CPU if VRAM is insufficient (slower but works).

**Q: Can I use it without Ollama?**
A: The script is easy to adapt. Swap `call_ollama_vision()` for OpenAI API, Claude API, or any other vision endpoint.

**Q: Is my data safe?**
A: Yes. Everything runs locally — the image is read from disk, base64-encoded, sent to localhost, and processed on your GPU. Nothing leaves your machine.

---

## Contributing

PRs welcome! Areas where help is especially appreciated:

- More model support (vLLM, llama.cpp direct, etc.)
- Streaming output
- Multi-image conversations
- Web UI for testing

## License

MIT — use it, modify it, ship it. No strings attached.

---

<p align="center">
  <sub>Made for people who hate switching models just to read a screenshot.</sub>
</p>
