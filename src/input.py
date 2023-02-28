def welcomeMsg():
    print("=====================================================")
    print("================ NEAREST POINT ======================")
    print("=====================================================")

def inputUser():
    while(True):
        titik = int(input("Masukkan jumlah titik yang diinginkan : "))
        if(titik > 0):
            break
        else :
            print("Masukkan anda tidak valid, silakan coba lagi!")

    while(True):
        dimensi = int(input("Masukkan banyaknya dimensi titik yang anda inginkan : "))
        if(dimensi > 0):
            break
        else :
            print("Masukkan anda tidak valid")
    return titik,dimensi
