def exercise3():
    checker:float
    checker=1
    sums:float
    sums:0
    point=1
    try:
        get = open("input.txt", 'r')
    except FileNotFoundError:
        print("input.txt가 없습니다. ")
    else:
        if get:
            while True:
                sums=0
                sentence = get.readline()
                if sentence.find(".")==False:
                    point=100
                if sentence == "":
                    break
                divided = sentence.split(" ")
                for i in divided :
                    sums=sums+float(i)
                if checker==1 :
                    out=open("output.txt",'w')
                    checker=checker+1
                else :
                    out=open("output.txt",'a')
                if point==100:
                    round(sums)
                    out.write(str(sums))
                    out.write("\n");
                else :
                    out.write("%g" %sums)
                    out.write("\n");
                out.close()
                point=0
            get.close()
        final=open("output.txt","r")
        sentence = final.readline()
        print(sentence,end="")
        while sentence:
            sentence = final.readline()
            print(sentence,end="")
        final.close()


def exercise2():
    start = int(input('Enter the start day (0~6)>> '))
    date = int(input('Enter the number of days (1~31) >> '))
    check : int
    check=7-start
    number : int
    number=1
    print("Sun Mon Tue Wed Thu Fri Sat")
    for x in range(start):
        print("    ", end="")
    for x in range(check):
        print(" "+str(number), end="  ")
        number=number+1
    print("\n", end="")
    while True:
        for x in range(7) :
            if number < 10:
                print(" " + str(number), end="  ")
            else :
                print(" "+str(number), end=" ")
            number=number+1
            if number == date+1:
                break
        print("\n", end="")
        if number==date+1:
            break
def main():
    userInput: int
    star: int
    space: int
    userInput = int(input('enter number '))
    star=userInput
    space=0
    for x in range(userInput):
        for y in range(space):
            print(" ", end=" ")
        for y in range(star):
            print("*", end=" ")
        print("\n",end="")
        star=star-1
        space=space+1

if __name__ == "__main__":
    main()
    exercise2()
    exercise3()