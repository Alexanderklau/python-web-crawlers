from PIL import Image
import subprocess

def cleanFIle(filePath,newFilePath):
    image = Image.open(filePath)
    image = image.point(lambda x:0 if x < 143 else 255)
    image.save(newFilePath)

    subprocess.call(['tesseract',newFilePath,"output"])

    outputFile = open("output.txt",'r')
    print(outputFile.read())
    outputFile.close()
cleanFIle("text_2_.png","text_2_clean.png")
