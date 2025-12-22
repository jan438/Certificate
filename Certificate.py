from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter  
from reportlab.lib.colors import red, blue, yellow, green
from reportlab.lib.units import mm, cm

c = Canvas("PDF/Certificate.pdf", pagesize=letter)  
 
#c.linearGradient(100, 0, 400, 0, (red, yellow, green), (0, 0.8, 1), extend = False)
 
#c.rect(  
#    x=100, y=600,
#    width=400, height=100,
#    stroke=1
#)
p = c.beginPath()
p.rect(0,0 , 5*cm,5*cm)
c.clipPath(p, stroke=0)
c.linearGradient(0,0 , 5*cm, 5*cm , (red, yellow))

c.save()  

key = input("Wait")



