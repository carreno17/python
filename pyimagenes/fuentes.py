
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
"""Para poder agregarle texto a una imagen hay que importar los modulos
ImageDraw y ImageFont"""
Fuente = 'fuente/Roboto-Bold.ttf'
if __name__ == '__main__':

    try:
        imagen = Image.open('imagenes/tercera.jpg')
        
        draw = ImageDraw.Draw(imagen)
        font = ImageFont.truetype(Fuente, 120) #120 es el tamaño de la fuente
        
        draw.text(
            
            (100,200), #Posición del texto (x,y)
            'Hola mundo', #El texto
            (255, 255, 255), #color
            font=font#fuente
        )

        imagen.show()
    except FileNotFoundError as Error:
        print('Esa ubicación de la imagen no existe')