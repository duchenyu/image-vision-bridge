---
name: image-vision
description: 本地图片视觉理解桥接。当用户发送图片时，调用本地 Ollama 视觉模型（qwen3.5:4b）读取图片内容，以文字描述返回，让不具备多模态能力的推理模型也能"看见"图片。
trigger:
  - 用户发送了图片文件（png/jpg/gif/webp/bmp）
  - 对话中出现图片文件路径
  - 用户要求分析、描述、理解图片内容
---

# Image Vision Bridge

本地视觉桥接 —— 当对话中出现图片时，调用 Ollama 本地视觉模型（qwen3.5:4b / qwen3.5:9b）读图并返回文字描述。

## 使用方式

```bash
C:/Users/djr82/.workbuddy/binaries/python/versions/3.13.12/python.exe "C:/Users/djr82/.workbuddy/skills/image-vision/scripts/describe_image.py" "<图片路径>"
```

### 可选参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--model` | 视觉模型名 | `qwen3.5:4b` |
| `--prompt` | 自定义分析指令 | 详细描述所有细节 |

### 模型选择

- **qwen3.5:4b** (~3.4GB) — 轻量化，首次加载约30秒，后续秒级响应。适合日常读图。
- **qwen3.5:9b** (~6.6GB) — 更高质量，描述更准确细腻。适合需要精准理解的场景。

### 自定义 prompt 示例

```bash
# 提取图中文字
--prompt "请逐字提取图片中所有文字内容，不要遗漏任何文字。"

# 分析 UI 界面
--prompt "这是一个软件界面截图，请分析其布局、按钮、输入框等交互元素。"

# 提取代码
--prompt "完整提取截图中的代码，保留缩进和格式。"

# 中文场景
--prompt "请用中文详细描述这张图片的内容。"
```

## 工作流程

1. 用户发送图片 → 图片路径出现在对话上下文中
2. 检测到图片 → 自动调用本 skill
3. 脚本将图片 base64 编码 → 发送到 Ollama API
4. qwen3.5 视觉模型分析图片 → 返回文字描述
5. 基于描述继续完成任务

## 前置条件

- ✅ Ollama 已安装并运行
- ✅ qwen3.5:4b 已拉取（已就绪）
- ✅ Python 3.13 (managed)

## 绕过模型限制

如果 WorkBuddy 拦截图片发送（提示"当前模型不支持图片输入"），使用剪贴板快照：

```bash
# 1. 截图到剪贴板（Win+Shift+S）
# 2. 运行快照脚本
python "C:/Users/djr82/.workbuddy/skills/image-vision/scripts/clip_snap.py"
# 输出: C:\Users\djr82\.workbuddy\clip-snaps\snap_xxx.png

# 3. 路径已自动复制到剪贴板，Ctrl+V 粘贴到聊天框即可
```

Windows 用户可直接双击 `scripts/快照剪贴板.bat`，零打字。

## 故障排除

如果 Ollama 模型崩溃（"llama-server process has terminated"），需要重启 Ollama 服务：
```powershell
Get-Process -Name "ollama*" -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Process "C:\Users\djr82\AppData\Local\Programs\Ollama\ollama.exe" -ArgumentList "serve" -WindowStyle Hidden
```
