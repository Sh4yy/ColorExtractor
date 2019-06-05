from japronto import Application
from uuid import uuid4
from extractor import *
from hashlib import sha256
import os


def primary_colors(request):

    if "image" not in request.files:
        return request.Response(json={"ok": False,
         "msg": "missing image"})

    if "count" not in request.form:
        return request.Response(json={"ok": False,
         "msg": "missing count"})

    count = int(request.form['count'])
    img = request.files['image']

    if img.type == "image/jpeg":
        ext = ".jpg"
    elif img.type == "image/png":
        ext = ".png"
    else:
        return request.Response(json={"ok": False,
         "msg": "image type not supported"})

    img_path = "Images/" + str(uuid4()) + ext
    open(img_path, "wb").write(img.body)
    colors = dom_colors_hex(img_path, num_colors=count)
    os.remove(img_path)
    return request.Response(json={"ok": True, "colors": colors})


app = Application()
app.router.add_route('/image/primary', primary_colors, method='POST')
app.run(debug=False, port=8081, worker_num=10)
