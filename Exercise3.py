import os
import sys
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, red, blue, yellow, green, white, darkblue, gold,  HexColor
from reportlab.lib.units import mm, cm
    
def drawRect(c, x, y, w, h, d):    
    c.saveState()
    p = c.beginPath()
    p.rect(x, y, w, h)
    c.clipPath(p, stroke = 1)
    if d == "b":
        c.linearGradient(x, y, x, y + h, (col1, col2), (0, 1), extend = False)
    if d == "t":
        c.linearGradient(x, y, x, y + h, (col1, col2), (1, 0), extend = False)
    c.restoreState()

col1 = HexColor("#b8bfbc")
col2 = HexColor("#a4aaa8")

if sys.platform[0] == 'l':
    path = '/home/jan/git/Certificate'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/Certificate"
os.chdir(path)
c = Canvas("PDF/Exercise3.pdf", pagesize=letter)
drawRect(c, 100, 100, 50, 200, "b")
drawRect(c, 150, 100, 50, 200, "t")
drawRect(c, 200, 100, 50, 200, "b")
drawRect(c, 250, 100, 50, 200, "t")
c.save()  

key = input("Wait")
