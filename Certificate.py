import os
import sys
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import red, blue, yellow, green, white, HexColor
from reportlab.lib.units import mm, cm

def drawRect(c, x, y, w, h, a, color):    
    c.setFillColor(HexColor(color))
    p = c.beginPath()
    p.moveTo(x, y + 0.5 * a)
    p.arcTo(x, y, x + a, y + a, startAng = 180, extent = 90)                # arc left below
    p.lineTo(x + w, y)                                                      # horizontal line
    p.arcTo(x + w, y, x + w + a, y + a, startAng = 270, extent = 90)        # arc right below
    p.lineTo(x + w + a, y + h)                                              # vertcal line
    p.arcTo(x + w, y + h, x + w + a, y + h + a, startAng = 0, extent = 90)  # arc right above
    p.lineTo(x + 0.5 * a, y + h + a)                                        # horizontal line
    p.arcTo(x, y + h, x + a, y + h + a, startAng = 90, extent = 90)         # arc left above
    p.lineTo(x, y + 0.5 * a)                                                # vertcal line
    c.drawPath(p, stroke = 0, fill = 1)
    c.clipPath(p, stroke=0)
    c.linearGradient(10*cm, 10*cm, 20*cm, 20*cm , (red, white, yellow), (0, 0.3, 1))
    
if sys.platform[0] == 'l':
    path = '/home/jan/git/Certificate'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/Certificate"
os.chdir(path)
c = Canvas("PDF/Certificate.pdf", pagesize=letter)
c.saveState()
p = c.beginPath()
p.rect(0, 0, 5*cm, 5*cm)
c.clipPath(p, stroke=0)
c.linearGradient(0, 0, 5*cm, 5*cm , (red, green, yellow), (0, 0.3, 1))
c.restoreState()
p = c.beginPath()
p.rect(10*cm, 10*cm, 10*cm, 10*cm)
c.clipPath(p, stroke=0)
c.linearGradient(10*cm, 10*cm, 20*cm, 20*cm , (red, green, yellow), (0, 0.3, 1))
drawRect(c, 11*cm,  12*cm, 50, 50, 20, "#da23ff")
c.save()  

key = input("Wait")
