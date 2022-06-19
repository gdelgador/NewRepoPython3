import re


# leemos archivo
FILE_NAME = 'tarjetas.txt'
TARJETAS = open(FILE_NAME).readlines()

# REGEX
regex = r"^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}-?$"


def main():
    
    # genero valores 0000, 1111, 2222 .... 
    repeticiones = [ str(i)*4 for i in range(10)]

    for tarjeta in TARJETAS:
        tarjeta = tarjeta.strip()
        
        # validando tarjeta
        if re.search(regex, tarjeta):
            # validando presencia repeticiones '1111'
            new_tarjeta = tarjeta.replace('-','')
            rep = [ True  for repticion in repeticiones if re.search(repticion, new_tarjeta)]
            if not rep:
                print( f'{tarjeta} -> Valid')
                continue
        print( f'{tarjeta} -> Invalid')
    
    pass

if __name__ == '__main__':
    main()