import os
import sys
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, red, blue, yellow, green, white, gold, darkblue, HexColor
from reportlab.lib.units import mm, cm

def drawBGRect(c):    
    c.saveState()
    p = c.beginPath()
    p.rect(0, 0, width, height)
    c.clipPath(p, stroke = 0)
    c.linearGradient(0, 0, width, height, (Color(0.9, 0.95, 1), Color(0.7, 0.85, 1)), (0, 1))
    c.restoreState()
    
def drawTitleRect(c):    
    c.saveState()
    p = c.beginPath()
    p.rect(100, height - 200, 400, 80)
    c.clipPath(p, stroke = 1)
    c.linearGradient(0, 0, 400, 0, (darkblue, gold), (0, 1))
    c.restoreState()
    
def drawSealEllipse(c):    
    c.saveState()
    p = c.beginPath()
    p.ellipse(width - 200, 200, 100, 100)
    c.clipPath(p, stroke = 1)
    c.radialGradient(width - 175, 225, 50, (gold, darkblue), (0, 1))
    c.restoreState()

if sys.platform[0] == 'l':
    path = '/home/jan/git/Certificate'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/Certificate"
os.chdir(path)
c = Canvas("PDF/Certificate.pdf", pagesize=letter)
width, height = letter
drawBGRect(c)
drawTitleRect(c)
c.setFont("Helvetica-Bold", 36)  
c.setFillColor(white)  
c.drawCentredString(width/2, height - 160, "CERTIFICATE OF ACHIEVEMENT")
drawSealEllipse(c)
c.save()  

key = input("Wait")
