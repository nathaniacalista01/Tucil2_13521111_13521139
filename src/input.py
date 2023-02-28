def welcomeMsg():
    print("=====================================================")
    print("================ NEAREST POINT ======================")
    print("=====================================================")

def inputUser():
    while(True):
        titik = int(input("Please input the number of points: "))
        if(titik > 1):
            break
        else :
            print("Input not valid, a minimum number of 2 points is needed, please reenter your input!")

    while(True):
        dimensi = int(input("Please input the dimension: "))
        if(dimensi > 0):
            break
        else :
            print("Input not valid, a minimum of 1 dimension is needed, please reenter your input!")
    return titik,dimensi
