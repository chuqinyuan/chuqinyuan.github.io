#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# 设置端口号
PORT = 8001

# 获取当前目录作为网站根目录
web_dir = os.path.join(os.path.dirname(__file__))
os.chdir(web_dir)

# 配置HTTP请求处理器
Handler = http.server.SimpleHTTPRequestHandler

# 设置MIME类型，确保CSS和JS文件能正确加载
Handler.extensions_map.update({
    '.js': 'application/javascript',
    '.css': 'text/css',
})

print(f"正在启动服务器...")
print(f"网站根目录: {web_dir}")
print(f"访问地址: http://localhost:{PORT}")

# 启动服务器
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"服务器启动成功! 按 Ctrl+C 停止服务器")
    try:
        # 自动打开浏览器
        webbrowser.open(f"http://localhost:{PORT}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
        httpd.server_close()