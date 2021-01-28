import functions as fa

def main2():

    code = str(input("Selecciona una opció: "))

    if code == "a":
        fa.file_name('C:/Users/mario/PycharmProjects/Fitxers/recursivitat/text.txt')
    elif code == "b":
        fa.file_read('C:/Users/mario/PycharmProjects/Fitxers/recursivitat/text.txt')
    elif code == "c":
        fa.file_write2('C:/Users/mario/PycharmProjects/Fitxers/recursivitat/text.txt')
    elif code == "d":
        quit()
    else:
        print("Error")

if __name__ == '__main__':
    main2()