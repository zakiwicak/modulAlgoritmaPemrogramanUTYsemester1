def bubbleShort(vel):
    for i in range(len(vel)-1, 0, -1):
        for j in range(i):
            if vel[j] < vel[j+1]:
                temp = vel[j]
                vel[j] = vel[j+1]
                vel[j+1] = temp
    print(vel)


def selectionSort(vel):
    for i in range(len(vel)-1, 0, -1):
        max = 0
        for j in range(1, i+1):
            if vel[j] < vel[max]:
                max = j
        temp = vel[i]
        vel[i] = vel[max]
        vel[max] = temp
    print(vel)


def insertSort(vel):
    for i in range(len(vel)-1, 0, -1):
        aktif = vel[i]
        j = i-1
        while j >= 0 and vel[j] < aktif:
            vel[j+1] = vel[j]
            j = j-1
            vel[j+1] = aktif
    print(vel)


value = [4, 7, 11, 15, 20, 23, 32, 99]
print("bubbleshort    : ", bubbleShort(value))
print("selectionshort : ", selectionSort(value))
print("insertshort    : ", insertSort(value))
