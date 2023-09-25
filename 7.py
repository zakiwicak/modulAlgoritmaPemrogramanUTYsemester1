def fibo(n):
    angkapertama = 1
    angkakedua = 1

    print(angkapertama, angkakedua, end=" ")
    n -= 2
    while n > 0:
        print(angkapertama + angkakedua, end=" ")
        temp = angkakedua
        angkakedua = angkapertama + angkakedua
        angkapertama = temp
        n -= 1


# sesuai soal, cukup 7 saja
if __name__ == "__main__":
    print("Deret fibonacci : ")
    fibo(7)
    pass
