import os
import sys
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER, A4, landscape, portrait
from reportlab.lib.colors import Color, red, blue, yellow, green, white, HexColor
from reportlab.lib.units import mm, cm
from reportlab.lib import colors
from reportlab.graphics.shapes import *

if sys.platform[0] == 'l':
    path = '/home/jan/git/Certificate'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/Certificate"
os.chdir(path)
c = Canvas("PDF/Exercise2.pdf", pagesize=LETTER)
c.rect(300,75,100,100, fill=True, stroke=False)
d = Drawing(A4[1], A4[0])
c.save()  

key = input("Wait")
