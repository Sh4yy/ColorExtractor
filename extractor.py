from PIL import Image, ImageDraw


def dom_colors_rgba(image_path, num_colors=5):
    """
    get dominant colors of an image in rgba
    :param image_path: path to the target image
    :param num_colors: number of colors to return
    :returns a list of rgba tuples
    """
    image = Image.open(image_path)
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
