import os
import sys
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, red, blue, yellow, green, white, darkblue, gold,  HexColor
from reportlab.lib.units import mm, cm
    
def drawRect(c, x, y, w, h):    
    c.saveState()
    p = c.beginPath()
    p.rect(x, y, w, h)
    c.clipPath(p, stroke = 1)
    c.linearGradient(x, y, x, h, (darkblue, gold), (0, 1))
    c.restoreState()

if sys.platform[0] == 'l':
    path = '/home/jan/git/Certificate'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/Certificate"
os.chdir(path)
c = Canvas("PDF/Exercise3.pdf", pagesize=letter)
drawRect(c, 100, 100, 50, 200)
drawRect(c, 150, 100, 50, 200)
drawRect(c, 200, 100, 50, 200)
c.save()  

key = input("Wait")
