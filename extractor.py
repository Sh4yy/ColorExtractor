from PIL import Image, ImageDraw
from time import time


def dom_colors_rgba(image_path, num_colors=5):
    """
    get dominant colors of an image in rgba
    :param image_path: path to the target image
    :param num_colors: number of colors to return
    :returns a list of rgba tuples
    """
    image = Image.open(image_path)
    image = image.resize((100, 100))
    result = image.convert('P', palette=Image.ADAPTIVE, colors=num_colors)
    result.putalpha(0)
    colors = result.getcolors(256)

    colors = sorted(colors, key=lambda x: x[0], reverse=True)
    return list(map(lambda x: x[1], colors))


def dom_colors_hex(image_path, num_colors=5):
    """
    get dominant colors of an image in hex
    :param image_path: path to the target image
    :param num_colors: number of colors to return
    :returns a list of hex colors
    """
    colors = dom_colors_rgba(image_path, num_colors)
    hex_colors = []
    for r, g, b, _ in colors:
        hex_colors.append("#{0:02x}{0:02x}{0:02x}".format(r, g, b))

    return hex_colors


def draw_palette(colors, img_path, swatchsize=100):
    """
    draw the color palette
    :param colors: tuple of rgba colors
    :param img_path: the path to the created palette
    """

    numcolors = len(colors)
    pal = Image.new('RGB', (swatchsize * numcolors, swatchsize))
    draw = ImageDraw.Draw(pal)

    posx = 0
    for col in colors:
        draw.rectangle([posx, 0, posx+swatchsize, swatchsize], fill=col)
        posx = posx + swatchsize

    del draw
    pal.save(img_path, "PNG")
