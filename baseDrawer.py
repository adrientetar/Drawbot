#Input Values
xHeight = 500
ascender = 750
descender = 250
capHeight = None
baselineOverShoot = 12
xHeightOverShoot = 12
monospaceWidth = None


#Calcs    
baseline = 220
equis = (xHeight/10)*2.8346
ascendente = (ascender/10)*2.8346
descendente = (descender/10)*2.8346
if capHeight is not None: mayusculas = (capHeight/10)*2.8346
baseOvershoot = (baselineOverShoot/10)*2.8346
xOvershoot = (xHeightOverShoot/10)*2.8346
if monospaceWidth is not None: monoWidth = (monospaceWidth/10)*2.8346

#Texts
newPage('A4Landscape')
font("Menlo")
fontSize(8)

text("base.(0)", (30, baseline-2))
text("x–h(" +  str(xHeight) + ")", (30, (baseline+equis)-2))
text("asc.(" +  str(ascender) + ")", (30, (baseline+ascendente)-2))
if capHeight is not None: text("cap.(" +  str(capHeight) + ")", (30, (baseline+mayusculas)-2))
text("desc.(" +  str(descender) + ")", (30, (baseline-descendente)-2))
text("1cm ≈ 100 upm", (30, 30))
if monospaceWidth is not None: text("monospace: " + str(monospaceWidth) + " units", (30, 30))

font("Menlo-Bold")
text("Project Name:", (30, 540))
text("Style:", (30, 525))
text("Weight:", (30, 510))
text("Date:", (30, 495))


#Drawings
#Baseline
rect(85, baseline, 730, 0.5)

#AlturaX
rect(85, baseline+equis, 730, 0.3)

#ascender
rect(85, baseline+ascendente, 730, 0.3)

#descender
rect(85, baseline-descendente, 730, 0.3)

#cap height
if capHeight is not None: rect(85, baseline+mayusculas, 730, 0.3)

#monospace guidelines
if monospaceWidth is not None:
  padding = (730-85) % monoWidth * 2
  for i in range((730-85) // monoWidth + 1):
    rect(85+padding+i*monoWidth, descendente-30, 0.2, 30+descendente+ascendente+30)

#BaselineOvershoot
fill(1, 0, 0, .1)
rect(85, baseline, 730, -xOvershoot)

#xHeightOverShoot
fill(1, 0, 0, .1)
rect(85, baseline+equis, 730, xOvershoot)

#set a stroke color
fill(0, 0, 0, 1)


saveImage("~/Desktop/base.pdf")
