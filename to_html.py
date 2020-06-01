from PIL import Image

head = """<!DOCTYPE html>
<html lang="en">
<head>
    <!--  Check the source picture  -->
    <!--  https://pavelborisofff.github.io/perfect_pixel/img/source.png  -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body style="margin:0; padding:0">
"""

footer = """</table>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(head)

im = Image.open('img/source.png')
with open('index.html', 'a', encoding='utf-8') as f:
    f.write(f'<table width="{im.size[0]}" height="{im.size[1]}" cellspacing="0" cellpadding="0" style="margin:auto">')

with open('index.html', 'a') as f:
    for y in range(im.size[1]):
        f.write('<tr>\n')
        for x in range(im.size[0]):
            color = im.getpixel((x, y))
            hex_color = '#%02x%02x%02x' % color
            f.write(f'<td bgcolor="{hex_color}"></td>\n')
        f.write('</tr>\n')
    f.write(footer)
