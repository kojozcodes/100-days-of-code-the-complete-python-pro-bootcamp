###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    print(color)
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    colo = (r, g, b)
    rgb_colors.append(colo)

print(rgb_colors)