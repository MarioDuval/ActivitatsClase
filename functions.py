def file_write(fname):
    f = open(fname, "a+")
    str = input("Introdueix un text: ")
    f.write(str)
    f.close()

def file_write1(fname):
    f = open(fname, "a+")
    str = input("Introdueix un text: ")
    f.write(str)
    f.close()

def file_name(fname):
    fileName = input("Introdueix el nom de un fitxer: ")
    try:
        with open(fileName) as fname:
            print(fname.readline())
        fname.close()
    except:
        print("Error")

def file_read(fname):
    f = open(fname, "r")
    print(f.read())
    f.close()

def file_write2(fname):
    f = open('C:/Users/mario/PycharmProjects/Fitxers/recursivitat/text.txt', "w")
    for i in range(10):
        f.write("This is line %d\r\n" % (i + 1))
    f.close()
