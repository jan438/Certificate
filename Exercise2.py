import os
import sys
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, red, blue, yellow, green, white, HexColor
from reportlab.lib.units import mm, cm

if sys.platform[0] == 'l':
    path = '/home/jan/git/Certificate'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/Certificate"
os.chdir(path)
c = Canvas("PDF/Exercise2.pdf", pagesize=letter)
c.rect(300,75,100,100, fill=True, stroke=False)
c.save()  

key = input("Wait")
