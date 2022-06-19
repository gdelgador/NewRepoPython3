import random


def get_int(msg:str)->int:
    try:
        x = int(input(msg))
        
        assert x>=1 # genera error en caso contrario
        return x
    except:
        return get_int(msg)

def guess(x, msg):

    while True:
        v = get_int(msg)

        if v<x:
            print('¡Demasiado pequeño!')
        elif v>x:
            print('¡Te pasaste!')
        else:
            print('¡Adivinaste!')
            break

def main():

    n = get_int('Level: ')
    x = random.randint(1, n)

    guess(x, 'Guess: ')
    pass

if __name__ == '__main__':
    main()