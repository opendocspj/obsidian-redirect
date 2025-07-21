from flask import Flask, request, redirect
import urllib.parse
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Obsidian Redirect Server đang chạy.'

@app.route('/redirect')
def redirect_obsidian():
    path = request.args.get("path")
    if not path:
        return "Missing 'path' parameter", 400

    decoded_path = urllib.parse.unquote(path)
    obsidian_link = f"obsidian://open?path={decoded_path}"
    return redirect(obsidian_link, code=302)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Lấy PORT từ Render hoặc dùng 5000 mặc định
    app.run(host="0.0.0.0", port=port)
