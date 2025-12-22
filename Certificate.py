import os
import sys
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter  
from reportlab.lib.colors import red, blue, yellow, green
from reportlab.lib.units import mm, cm

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
c.save()  

key = input("Wait")
