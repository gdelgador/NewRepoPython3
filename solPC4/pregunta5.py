import sys


def main():
    
    file_name = input('Ingrese el nombre del archivo: ').strip()
    if not file_name.endswith('.py'):
        print('Not a Python file')
        sys.exit(1)

    try:
        lines= open(file_name).readlines()
    except FileNotFoundError:
        print('File does not exist')
        sys.exit(1)

    count = 0
    for line in lines:
        if line.strip().startswith('#') or line.strip()=='':
            continue
        count +=1

    print(count)
    pass

if __name__ == '__main__':
    main()