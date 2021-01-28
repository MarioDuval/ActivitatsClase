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
    fd = open(fileName, "w")
    fd.write(fileName)

def file_read(fname):
    fa = open(fname, "r")
    print(fa.read())
    fa.close()

def file_write2(fname):
    fileName = input("Introdueix el nom del fitxer: ")
    fa = open(fileName, "w")
    for i in range(5):
        fa.write("This is line %d\r\n" % (i + 1))
    fa.close()
