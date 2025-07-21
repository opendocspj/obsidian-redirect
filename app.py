from flask import Flask, request, redirect
import urllib.parse
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Obsidian Redirect Server đang chạy.'

@app.route('/redirect')
def redirect_obsidian():
    vault = request.args.get("vault")
    file = request.args.get("file")

    if vault and file:
        obsidian_link = f"obsidian://open?vault={urllib.parse.quote(vault)}&file={urllib.parse.quote(file)}"
        return redirect(obsidian_link, code=302)

    # Backward compatibility: vẫn hỗ trợ path nếu có
    path = request.args.get("path")
    if path:
        decoded_path = urllib.parse.unquote(path)
        obsidian_link = f"obsidian://open?path={decoded_path}"
        return redirect(obsidian_link, code=302)

    return "Missing 'vault' and 'file' (or 'path') parameter", 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Lấy PORT từ Render hoặc dùng 5000 mặc định
    app.run(host="0.0.0.0", port=port)
