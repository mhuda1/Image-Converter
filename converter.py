from PIL import Image
import cv2 


# This is a cli based universal converter on python PNG/JPG/JPEG/GIF/BMP/TIFF

def imageConverter(image, format):
    try:
        img = Image.open(image)
        imgName = image.split('.')
        if img.mode != "RGB":
            img = img.convert('RGB')

        if str(format).upper() == "JPG":
            img.save("{}.jpg".format(imgName[0]), 'JPEG')

        elif str(format).upper() == "PNG":
            img.save("{}.png".format(imgName[0]), 'PNG')

        elif str(format).upper() == "GIF":
            img.save("{}.gif".format(imgName[0]), 'GIF')
        
        elif str(format).upper() == "TIFF":
            img.save("{}.tif".format(imgName[0]), 'TIFF')
        
        elif str(format).upper() == "BMP":
            img.save("{}.bmp".format(imgName[0]), 'BMP')

        else:
            print("Unknown Format")

    except ValueError:
        print("Wrong image format.\n please input image in {} format".format((str(format)).upper()))
    

def displayImage(image):
    try:
        img = cv2.imread(image)
        cv2.imshow('image', img)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
    
    except ValueError:
        print("Wrong file format.\n please input image in PNG\JPG\JPEG\TIFF\BMP format")

def main():

    print("This is a python image file converter using the pillow library")

    comIn = input("Input file Path: ")
    comOut = input("Output type(JPG/PNG/GIF/BMP/TIFF): ")

    try:
        imageConverter(str(comIn), str(comOut))
    except:
        print("Wrong image format.\nPlease input image in PNG\JPG\JPEG\TIFF\BMP format.")

if __name__ == "__main__":
    main()