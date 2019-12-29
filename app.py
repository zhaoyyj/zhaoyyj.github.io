from flask import Flask, request, render_template, send_from_directory
app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/img/<path>')
def send_assets(path):
    return send_from_directory('img', path)

@app.route('/img/banners/<path>')
def send_banners(path):
    return send_from_directory('img/banners', path)

@app.route('/img/glow_beams/<path>')
def send_glow_beams(path):
    return send_from_directory('img/glow_beams', path)

@app.route('/img/icons/<path>')
def send_icons(path):
    return send_from_directory('img/icons', path)

@app.route('/img/neon-outline/<path>')
def send_neon_outline(path):
    return send_from_directory('img/neon-outline', path)

@app.route('/css/<path>')
def send_style(path):
    return send_from_directory('css', path)

@app.route('/js/<path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/fonts/<path>')
def send_fonts(path):
    return send_from_directory('fonts', path)

@app.route('/PDF/<path>')
def send_pdfs(path):
    return send_from_directory('PDF', path)
