from PIL import Image

im = Image.open("parrot.jpg")

pix = im.load()
width, height = im.size

#print("Width: "+str(width))
#print("Height: "+str(height))

for i in range(0,width):
    for j in range(0,height):
        red, green, blue = pix[i,j]
        if red > 100:
            pix[i,j] = (255, 255, 230)
        elif green > 100:
            pix[i,j] = (255,230,255)
        elif blue > 100:
            pix[i,j] = (230,255,255)
        else:
            pix[i,j] = (77, 77, 77)




#print(pix[1,1]) #Get the RGBA Value of the a pixel of an image
#pix[2,2] = (3,4,5) # Set the RGBA Value of the image (tuple)


im.save("parrot_filtered.jpg") # Save the modified pixels as png
