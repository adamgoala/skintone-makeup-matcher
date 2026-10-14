from PIL import Image #imports the image using scanner

image = Image.open("LEBRON_FACE.PNG") #opens the image
image = image.convert("RGB")

print("Image size: ", image.size) #Gets the dimensions of the image

pixel = image.getpixel((320,350)) #Gets RGB from specific pixel
pixel2 = image.getpixel((530, 350))
'''
print("Left Cheek: ",pixel)
print("Right Cheek: ", pixel2)
'''

'''
rAvg = (pixel[0] + pixel2[0]) / 2 #Gets average RGB from 2 pixels (base)
gAvg = (pixel[1] + pixel2[1]) / 2
bAvg = (pixel[2] + pixel2[2]) / 2
average_color = (rAvg, gAvg, bAvg) 
print("Average color palate: ", average_color )
'''

#-------------------------------------------
'''
n = 0
red = 0
green = 0
blue  = 0
start_x = 320
start_y = 350
size = 50
for i in range(start_x,start_x + size):
    for k in range(start_y, start_y + size):
        pixel = image.getpixel((i, k))
        red += pixel[0]
        green += pixel[1]
        blue += pixel[2]

        n+=1

average_color_2 = (red / n, green/n, blue / n)    

print("Average_color_2: ", average_color_2)
'''
#--------------------------------------------


def average_skin_color(image, start_x, start_y, size) -> tuple[float, float, float]:
    n = 0
    red = 0
    green = 0
    blue  = 0
    #start_x = 320
    #start_y = 350
    #size = 50
    for i in range(start_x,start_x + size):
        for k in range(start_y, start_y + size):
            pixel = image.getpixel((i, k))
            red += pixel[0]
            green += pixel[1]
            blue += pixel[2]

            n+=1

    average_color_2 = (red / n, green/n, blue / n)    
    print("runs")
    return average_color_2


left = average_skin_color(image, 320, 350, 50)
print("Left cheek: ", left)

right = average_skin_color(image ,530,350, 50)
print("Right cheek: ", right)