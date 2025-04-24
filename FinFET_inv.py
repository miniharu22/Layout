import pya

layout = pya.Layout()
finfet = layout.create_cell("FinFET")

# Fin Layer
l1 = layout.layer(1,0)
finfet.shapes(l1).insert(pya.Box(0, 0, 8, 144))  ## NMOS
finfet.shapes(l1).insert(pya.Box(48, 0, 56, 144))
finfet.shapes(l1).insert(pya.Box(96, 0, 104, 144))

finfet.shapes(l1).insert(pya.Box(170, 0, 178, 144))  ## PMOS
finfet.shapes(l1).insert(pya.Box(218, 0, 226, 144))
finfet.shapes(l1).insert(pya.Box(266, 0, 274, 144))

# Gate Layer
l2 = layout.layer(2,0)
finfet.shapes(l2).insert(pya.Box(-70, 61, 344, 83))

# Contact Layer
l3 = layout.layer(3,0)
finfet.shapes(l3).insert(pya.Box(-5, 20, 13, 40)) ## NMOS Drain Contact
finfet.shapes(l3).insert(pya.Box(43, 20, 61, 40))
finfet.shapes(l3).insert(pya.Box(91, 20, 109, 40))

finfet.shapes(l3).insert(pya.Box(165, 20, 183, 40)) ## PMOS Drain Contact
finfet.shapes(l3).insert(pya.Box(213, 20, 231, 40))
finfet.shapes(l3).insert(pya.Box(261, 20, 279, 40))

finfet.shapes(l3).insert(pya.Box(-5, 104, 13, 124)) ## NMOS Source Contact
finfet.shapes(l3).insert(pya.Box(43, 104, 61, 124))
finfet.shapes(l3).insert(pya.Box(91, 104, 109, 124))

finfet.shapes(l3).insert(pya.Box(165, 104, 183, 124)) ## PMOS Source Contact
finfet.shapes(l3).insert(pya.Box(213, 104, 231, 124))
finfet.shapes(l3).insert(pya.Box(261, 104, 279, 124))

# Gate Interconnection Layer
l4 = layout.layer(4,0)
finfet.shapes(l4).insert(pya.Box(128, 61, 146, 106))

# Vin Via Layer 
l5 = layout.layer(5,0)
finfet.shapes(l5).insert(pya.Box(128, 88, 146, 106))

# Vout Via Layer    
l6 = layout.layer(6,0)
finfet.shapes(l6).insert(pya.Box(128, 0, 146, 18))

# Drain Interconnection Layer
l7 = layout.layer(7,0)
finfet.shapes(l7).insert(pya.Box(-5, 20, 280, 40))
finfet.shapes(l7).insert(pya.Box(128, 0, 146, 40))

# GND Interconnection Layer 
l8 = layout.layer(8,0)
finfet.shapes(l8).insert(pya.Box(-70, 104, 109, 124)) ## NMOS GND
finfet.shapes(l8).insert(pya.Box(-90, 0, -70, 144))

finfet.shapes(l8).insert(pya.Box(165, 104, 344, 124)) ## PMOS GND
finfet.shapes(l8).insert(pya.Box(344, 0, 364, 144))

# Insert Text
gen = pya.TextGenerator

t1 = gen.default_generator().text("NMOS", 0.05) ## NMOS
t1.transform(pya.Trans(pya.Point(30, -20)))
finfet.shapes(l1).insert(t1)

t2 = gen.default_generator().text("PMOS", 0.05) ## PMOS
t2.transform(pya.Trans(pya.Point(200, -20)))
finfet.shapes(l1).insert(t2)

t3 = gen.default_generator().text("VIN", 0.07) ## VIN
t3.transform(pya.Trans(pya.Point(125, 110)))
finfet.shapes(l5).insert(t3)

t4 = gen.default_generator().text("VOUT", 0.07) ## VOUT
t4.transform(pya.Trans(pya.Point(120, -15)))
finfet.shapes(l6).insert(t4)

t5 = gen.default_generator().text("GND", 0.07) ## VOUT
t5.transform(pya.Trans(pya.Point(-92, 145)))
finfet.shapes(l8).insert(t5)

t6 = gen.default_generator().text("GND", 0.07) ## VOUT
t6.transform(pya.Trans(pya.Point(342, 145)))
finfet.shapes(l8).insert(t6)


layout.write("finfet_inv.gds")