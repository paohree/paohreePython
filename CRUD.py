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


def update():
    return


def delete():
    return


def save():
    return


def main():
    user: int
    lists = []
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
        elif user == 4:
            print("Delete를 입력하셨습니다. ")
        elif user == 5:
            print("Save를 입력하셨습니다. ")
        elif user == 6:
            print("장비를 정지합니다.")
            break
        else:
            print("\n다시 입력하세요.\n")


if __name__ == "__main__":
    main()
