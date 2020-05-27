number = [1, 5, 6, 8, 11, 12, 15, 18, 22, 24]
j = 0
for i in range(1, 25) :
    if( i != number[j]) :
        print(i)
    elif(i == number[j] and j < 8) :
        j = j + 1

