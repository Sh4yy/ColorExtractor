from flask import Flask, jsonify, request, url_for
from extractor import *

app = Flask(__name__, static_url_path='/static')


@app.route('/image/primary', methods=['POST'])
def primary_colors():

    if not request.files or "image" not in request.files:
        return jsonify({"ok": False, "msg": "missing image"})

    count = int(request.form['count'])
    file = request.files['image']
    colors = dom_colors_hex(file, num_colors=count)
    return jsonify({"ok": True, "colors": colors})


app.run(port=8081, debug=True)
