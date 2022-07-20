from PIL import Image
from PIL import ImageOps
if __name__ == '__main__':
    try:
        imagen = Image.open('imagenes/tercera.jpg')
        imagen = ImageOps.expand(
            imagen, #La imagen
            border = (60,40,60,40),#Top, right, buttom, left #Borde
            fill = (202,300,264) #Color del borde
        )       
        imagen.show()



    except FileNotFoundError as Error:
        print('Esa ubicación de la imagen no existe')