# pip install pyfiglet 
from pyfiglet import Figlet
import sys
import random


is_random_font=True
figlet = Figlet()
fonts = figlet.getFonts()

def get_random_fond(fonts:list)->str:
    """Return a random font"""
    return random.choice(fonts)

def main():
    
    s = input('Introduzca un texto: ')
    fuente = input('Introduzca la fuente a utilizar: ').strip()
    
    # fuente aleatoria
    if fuente not in fonts:
        fuente = get_random_fond(fonts)
    print(f'Se usara la fuente {fuente}')
    
    
    figlet.setFont(font=fuente)
    print(figlet.renderText(s))
    pass

if __name__ == '__main__':
    main()