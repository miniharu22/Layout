import pya

layout = pya.Layout()
mosfet = layout.create_cell("MOSFET")


# Well Layer
l1 = layout.layer(1,0)
mosfet.shapes(l1).insert(pya.Box(800, 6750, 4800, 8330))

# Active Layer
l2 = layout.layer(2,0)
mosfet.shapes(l2).insert(pya.Box(1500, 6850, 4000, 8230))


# Gate Layer
l3 = layout.layer(3,0)
mosfet.shapes(l3).insert(pya.Box(1500, 7450, 4000, 7630))

# Contact Layer
l4 = layout.layer(4,0)
mosfet.shapes(l4).insert(pya.Box(2000, 7780, 2300, 8080)) ## Drain Contact
mosfet.shapes(l4).insert(pya.Box(2600, 7780, 2900, 8080))
mosfet.shapes(l4).insert(pya.Box(3200, 7780, 3500, 8080))

mosfet.shapes(l4).insert(pya.Box(2000, 7000, 2300, 7300)) ## Source Contact
mosfet.shapes(l4).insert(pya.Box(2600, 7000, 2900, 7300))
mosfet.shapes(l4).insert(pya.Box(3200, 7000, 3500, 7300))


# Insert Text
gen = pya.TextGenerator()

text = gen.default_generator().text("MOSFET", 0.002)
text.transform(pya.Trans(pya.Point(800, 8400)))
mosfet.shapes(l1).insert(text)

layout.write("mosfet.gds")
