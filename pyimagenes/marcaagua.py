from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
"""Para poder agregarle texto a una imagen hay que importar los modulos
ImageDraw y ImageFont"""

Fuente = 'fuente/Roboto-Bold.ttf'

if __name__ == '__main__':

    try:
        imagen = Image.open('imagenes/tercera.jpg')
        imagen = imagen.convert('RGBA') #Debemos pasarlo a este formanto

        new_imagen = Image.new('RGBA', imagen.size, (255,255,255,0))

        font = ImageFont.truetype(Fuente, 120) #120 es el tamaño de la fuente
        
        draw = ImageDraw.Draw(new_imagen)
        
        text_size = draw.textsize('Hola mundo', font)

        """
        #Esto es si queremos mostrar multiples marcas de agua
        
        for pas_x in range(0, imagen.size[0], text_size[0]+50 ):
             for pas_y in range(0, imagen.size[0], text_size[0]+50):
                draw.text(
    
                    (pas_x, pas_y), #Posición del texto (x,y)
                    'Hola mundo', #El texto
                    (255, 255, 255, 50), #color
                    font=font#fuente
                )
        """
        draw.text(
                
                (100,100), #Posición del texto (x,y)
                'Hola mundo', #El texto
                (255, 255, 255, 50), #color
                font=font#fuente
            )

        imagen = Image.alpha_composite(imagen, new_imagen)
        imagen.show()
    
    except FileNotFoundError as Error:
        print('Esa ubicación de la imagen no existe')