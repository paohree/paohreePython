# data crate ok!
# data read ok!
# file read ok!
# data update ok!
# data delete ok!
# data file save
def create(lists):
    item = []
    name = input("이름: ")
    price = input("가격: ")
    size = input("사이즈: ")
    item.append(name)
    item.append(price)
    item.append(size)
    lists.append(item)
    return lists


def read(lists):
    i: int = 0
    j: int = 0
    if len(lists) == 0:
        print("아무것도 없습니다. ")
    while i < len(lists):
        print(i + 1, "번째")
        while j < len(lists[i]):
            if j == 0:
                print("이름: " + lists[i][j] + " ")
            elif j == 1:
                print("가격: " + lists[i][j] + " ")
            else:
                print("사이즈: " + lists[i][j] + " ")
            j = j + 1
        print("")
        i = i + 1
        j = 0
    return


def update(lists):
    want: int = int(input("몇번째 데이터를 수정하시겠습니까?"))
    want = want-1

    name = input("이름: ")
    price = input("가격: ")
    size = input("사이즈: ")
    try:
        lists[want][0] = name
        lists[want][1] = price
        lists[want][2] = size
    except IndexError:
        print("해당 번호의 데이터가 존재하지 않습니다. ")
    return


def delete(lists):
    want: int = int(input("몇번째 데이터를 삭제하시겠습니까? "))
    want = want-1
    try:
        del lists[want]
    except ValueError:
        print("해당 번호의 데이터가 존재하지 않습니다. ")
    return


def save():
    return


def main():
    user: int
    lists = []
    try:
        get = open("data.txt", 'r')
    except FileNotFoundError:
        print("data가 없습니다. ")
    else:
        if get:
            while True:
                item = []
                sentence = get.readline()
                if sentence == "":
                    break
                # print(sentence)
                divided = sentence.split()
                name = divided[0]
                price = divided[1]
                size = divided[2]
                item.append(name)
                item.append(price)
                item.append(size)
                lists.append(item)
            print("data를 읽어왔습니다.")
            get.close()
    while True:
        print("1. Create \n2. Read \n3. Update\n4. Delete\n5. Save\n6. quit")
        user = int(input("무엇을 입력하시겠습니까? : "))
        if user == 1:
            print("Create를 입력하셨습니다. ")
            create(lists)
            print("입력되었습니다. ")
        elif user == 2:
            print("Read를 입력하셨습니다.")
            read(lists)
            print("완료했습니다. ")
        elif user == 3:
            print("Update를 입력하셨습니다.")
            update(lists)
            print("완료했습니다. ")
        elif user == 4:
            print("Delete를 입력하셨습니다. ")
            delete(lists)
            print("완료했습니다. ")
        elif user == 5:
            print("Save를 입력하셨습니다. ")
        elif user == 6:
            print("장비를 정지합니다.")
            break
        else:
            print("\n다시 입력하세요.\n")


if __name__ == "__main__":
    main()
