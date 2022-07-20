"""Para trabajar con filtros en las imagenes se debe importar el modulo
Imagefilter"""
from PIL import Image
from PIL import ImageFilter
if __name__ == '__main__':
    try:
        imagen = Image.open('imagenes/tercera.jpg')
        #Creando el un filtro, este filtro será para que la imagen se vea
        #borrosa
        #El radius nos sirve para poner la imagen más opaca con un valor alto
        #o menos opaca con un valor minimo
        filtro = ImageFilter.GaussianBlur(radius= 20)
        #Metodo filter es para aplicar el filtro a la imagen
        nueva_imagen = imagen.filter(filtro)
        nueva_imagen.show()
    except FileNotFoundError as Error:
        print('Esa ubicación de la imagen no existe')