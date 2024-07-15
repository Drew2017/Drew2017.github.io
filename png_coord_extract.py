from PIL import Image
import math
imgLink=input('Give image relative path')

#extract image pixel values to a list, and then convert them into coordinate values
rawImg=Image.open(imgLink,'r')
width=rawImg.size[0]
rawPixels=list(rawImg.getdata())
pixelCoords=[]
for index in range(len(rawPixels)):
    row_number=math.floor(index/width)
    row_index=index-(width*row_number)
    pixelCoords.append([row_number,row_index,rawPixels[index]])
    index += 1

#remove white pixels
nonWhiteCoords=[]
def findNonWhite(coords):
    if coords[2]!=255:
        nonWhiteCoords.append(coords)
for i in range(len(pixelCoords)):
    findNonWhite(pixelCoords[i])
    i += 1

#save as text file ending in _coords.txt
nonWhiteCoords=str(nonWhiteCoords)
coordFileName=imgLink+'_coords.txt'
with open (coordFileName,'w') as file:
    file.write(nonWhiteCoords)