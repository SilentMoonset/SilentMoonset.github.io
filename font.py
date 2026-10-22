from fontTools.ttLib import TTFont

font = TTFont("fonts/NotoSerifSC-VariableFont_wght.ttf")
font.flavor = "woff2"
font.save("fonts/NotoSerifSC-VariableFont_wght.woff2")
