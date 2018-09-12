from PIL import Image
import subprocess
def cleanFile(filePath,newFilePath):
    image = Image.open(filePath)
    # For image filtering(过滤)
    image = image.point(lambda x:0 if x <143 else 255)
    image.save(newFilePath)

    subprocess.call(["tesseract",newFilePath,"output"])

    outputFile = open("output.txt",'r')
    print(outputFile.read())
    outputFile.close()

cleanFile("text_2.jpg","text_2_clean.png")
