from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter  
from reportlab.lib.colors import red, blue, yellow, green
from reportlab.lib.units import mm, cm

c = Canvas("PDF/Certificate.pdf", pagesize=letter)  
p = c.beginPath()
p.rect(0, 0, 5*cm, 5*cm)
c.clipPath(p, stroke=0)
c.linearGradient(0, 0, 5*cm, 5*cm , (red, green, yellow), (0, 0.3, 1))
c.save()  

key = input("Wait")
