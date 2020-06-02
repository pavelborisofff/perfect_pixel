from PIL import Image

head = """<!DOCTYPE html>
<html lang="en">
<head>
<!--  Check the source picture  -->
<!--  https://pavelborisofff.github.io/perfect_pixel/img/source.png  -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Document</title>
<style>               
"""

after_style = """</style>
</head>
<body>
<table>
"""

footer = """</table>
</body>
</html>
"""

with open('index_valid.html', 'w', encoding='utf-8') as f:
    f.write(head)

im = Image.open('img/source.png')
with open('index_valid.html', 'a', encoding='utf-8') as f:
    f.write(f'table {{width:{im.size[0]}px;height:{im.size[1]}px;border-collapse: collapse;}}\n\n')

selectors = {}
cells = ''

for y in range(im.size[1]):
    cells += '<tr>'
    for x in range(im.size[0]):
        color = im.getpixel((x, y))
        hex_color = '#%02x%02x%02x' % color
        if hex_color in selectors:
            selectors[hex_color].append((x, y))
        else:
            selectors[hex_color] = [(x, y), ]
        cells += '<td></td>'
    cells += '</tr>\n'

css = ''
for color, pixels in selectors.items():
    tmp_css = ''
    for pixel in pixels:
        tmp_css += f'tr:nth-child({pixel[1]})>td:nth-child({pixel[0]}),'
    tmp_css = tmp_css[:-1] + f'{{background: {color};}}\n'
    css += tmp_css

with open('index_valid.html', 'a') as f:
    f.write(css)
    f.write(after_style)
    f.write(cells)
    f.write(footer)