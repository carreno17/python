
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

imagen_size = (1920,1080)
background_color = (15,40,90)
Fuente = 'fuente/Roboto-Bold.ttf'


if __name__ == '__main__':
    try:
        """Creando una imagen con en azul"""
        imagen= Image.new(
            'RGB', #Modelo de la imagen
            imagen_size,
            background_color
        ) 
        "Trayendo la imagen a pegar en la imagen azul"
        imagen_python = Image.open('imagenes/python.png')
        "Editando el tamaño"
        cambiar_tamaño = imagen_python.resize((990,950))
        "Pegando la imagen"
        imagen.paste(
            cambiar_tamaño,
            (1200, 250), #Posición (x,y)
            mask=cambiar_tamaño
        )

        """Agrendo el texto a la imagen"""
        draw = ImageDraw.Draw(imagen)
        font = ImageFont.truetype(Fuente, 120) #120 es el tamaño de la fuente
        
        draw.text(
            
            (100,200), #Posición del texto (x,y)
            'Decoradores de \n Python', #El texto
            (255, 255, 255), #color
            font=font#fuente
        )
        """El thumbnail sirve para sacar una miniautra
        de esa imagen"""
        imagen.thumbnail(
            imagen_size
        )
        imagen.save('imagenessave/proyecto_final.jpg')
        imagen.show()

    except FileNotFoundError as Error:
        print('Esa ubicación de la imagen no existe')