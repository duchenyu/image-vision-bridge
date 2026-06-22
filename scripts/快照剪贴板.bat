@echo off
chcp 65001 >nul
:: 一键快照剪贴板图片
:: 双击此文件 → 图片保存 → 路径自动复制到剪贴板 → 回到聊天框 Ctrl+V 粘贴

C:\Users\djr82\.workbuddy\binaries\python\versions\3.13.12\python.exe "%~dp0clip_snap.py" %*
echo.
echo 按任意键关闭...
pause >nul
