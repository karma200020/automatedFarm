import os
import img2pdf

#Method 1
with open("Output.pdf", "wb") as file:
    file.write(img2pdf.convert([i for i in os.listdir('Path of image_Directory') if i.endswith(".jpg")]))
#Method 2
# from fpdf import FPDF
# Pdf = FPDF()
# list_of_images = ["1.jpg", "2.jpg"]
# for i in list_of_images: # list of images with filename
#     Pdf.add_page()
#     Pdf.image(i,x,y,w,h)
# Pdf.output("yourfile.pdf", "F")