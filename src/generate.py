#!/usr/bin/python3
import numpy as np
import sys
import shutil
import os


def main():
    n = 8
    z = 8
    b = 8
    n_detect = False
    z_detect = False
    b_detect = False

    for i in sys.argv:
        if i == "--help":
            print("test.py -n -z -b")
            print("     -n, where n is the # of files we want to generate")
            print("     -z, where z is the matrix size of z x z")
            print("     -b, where b is the maximum bit of each matrix element")
            exit(-1)
        elif n_detect:
            n = int(i)
            n_detect = False
        elif z_detect:
            z = int(i)
            z_detect = False
        elif b_detect:
            b = int(i)
            b_detect = False
        else:
            if n_detect == False and i == "-n":
                n_detect = True
            elif z_detect == False and i == "-z":
                z_detect = True
            elif b_detect == False and i == '-b':
                b_detect = True



    try:
        os.mkdir("../matrix")
    except:
        try:
            os.rmdir("../matrix")
        except:
            decision = input("The matrix file is not empty, wish to delete all files inside? (Y/n):")
            if decision == '':
                shutil.rmtree("../matrix")
                os.mkdir("../matrix")
            else:
                print("please sort through your matrix before generating a new set")
                exit(-1)

    os.chdir("../matrix")

    file_name = "Matrix"

    for i in range(n):
        temp = np.random.randint(2 ** b, size=(z * z))
        name = file_name + str(i + 1) + ".txt"
        argument = "{0:0" + str(b) + "b}"
        fd = open(name, 'w')

        for k in range(z * z):
            if k == z * z - 1:
                fd.write("%s" % argument.format(temp[k]))
            else:
                fd.write("%s\n" % argument.format(temp[k]))

        fd.close()

        print("finished creating %d matrix file" % (i + 1))

    print("SUCCESS: Finished creating all files ....")
    os.chdir("../")


if __name__ == "__main__":
    main()
