import pya

layout = pya.Layout()
cmos = layout.create_cell("CMOS")

# P-Well Layer
l1 = layout.layer(1,0)
cmos.shapes(l1).insert(pya.Box(800, 6750, 4800, 8330))

# N-Well Layer
l2 = layout.layer(2,0)
cmos.shapes(l2).insert(pya.Box(800, 4770, 4800, 6350))

# N-Active Layer
l3 = layout.layer(3,0)
cmos.shapes(l3).insert(pya.Box(1500, 6850, 4000, 8230))

# P-Active Layer
l4 = layout.layer(4,0)
cmos.shapes(l4).insert(pya.Box(1500, 4870, 4000, 6250))

# Gate Layer
l5 = layout.layer(5,0)
cmos.shapes(l5).insert(pya.Box(1500, 7450, 4000, 7630)) ## NMOS Gate
cmos.shapes(l5).insert(pya.Box(1500, 5470, 4000, 5650)) ## PMOS Gate

# Contact Layer
l6 = layout.layer(6,0)
cmos.shapes(l6).insert(pya.Box(2000, 7780, 2300, 8080)) ## NMOS Drain Contact
cmos.shapes(l6).insert(pya.Box(2600, 7780, 2900, 8080))
cmos.shapes(l6).insert(pya.Box(3200, 7780, 3500, 8080))

cmos.shapes(l6).insert(pya.Box(2000, 7000, 2300, 7300)) ## NMOS Source Contact
cmos.shapes(l6).insert(pya.Box(2600, 7000, 2900, 7300))
cmos.shapes(l6).insert(pya.Box(3200, 7000, 3500, 7300))

cmos.shapes(l6).insert(pya.Box(2000, 5000, 2300, 5300)) ## PMOS Drain Contact
cmos.shapes(l6).insert(pya.Box(2600, 5000, 2900, 5300))
cmos.shapes(l6).insert(pya.Box(3200, 5000, 3500, 5380))

cmos.shapes(l6).insert(pya.Box(2000, 5830, 2300, 6130)) ## PMOS Source Contact
cmos.shapes(l6).insert(pya.Box(2600, 5830, 2900, 6130))
cmos.shapes(l6).insert(pya.Box(3200, 5830, 3500, 6130))

# Gate Interconnection Layer
l7 = layout.layer(7,0)
cmos.shapes(l7).insert(pya.Box(800, 7450, 4200, 7630)) ## NMOS
cmos.shapes(l7).insert(pya.Box(800, 5470, 4200, 5650)) ## PMOS

cmos.shapes(l7).insert(pya.Box(800, 4695, 1200, 8410))
cmos.shapes(l7).insert(pya.Box(100, 6395, 800, 6705))

# Vin Interconnection Layer
l8 = layout.layer(8,0)
cmos.shapes(l8).insert(pya.Box(100, 6395, 500, 6705))

# Drain Interconnection Layer
l9 = layout.layer(9,0)
cmos.shapes(l9).insert(pya.Box(2035, 7825, 4405, 8040)) ## NMOS
cmos.shapes(l9).insert(pya.Box(2035, 5045, 4405, 5260)) ## PMOS

cmos.shapes(l9).insert(pya.Box(4405, 4695, 4800, 8400)) 
cmos.shapes(l9).insert(pya.Box(4800, 6400, 5400, 6700)) 

# Vout Interconnection Layer
l10 = layout.layer(10,0)
cmos.shapes(l10).insert(pya.Box(5100, 6400, 5400, 6700))

# Insert Text
gen = pya.TextGenerator

t1 = gen.default_generator().text("NMOS", 0.003) ## NMOS
t1.transform(pya.Trans(pya.Point(1500, 8400)))
cmos.shapes(l1).insert(t1)

t2 = gen.default_generator().text("PMOS", 0.003) ## PMOS
t2.transform(pya.Trans(pya.Point(1500, 4500)))
cmos.shapes(l2).insert(t2)

t3 = gen.default_generator().text("VIN", 0.004) ## Vin
t3.transform(pya.Trans(pya.Point(100, 6800)))
cmos.shapes(l8).insert(t3)

t4 = gen.default_generator().text("VOUT", 0.004) ## Vout
t4.transform(pya.Trans(pya.Point(5100, 6790)))
cmos.shapes(l10).insert(t4)

layout.write("CMOSinv.gds")
