import getpass
import hashlib
from os import truncate

money = 0
inventory = {"시발점":0, "뉴런":0, "수분감":0, "드릴":0, "킬캠":0}


def menu() : 

    i = int(input(f"실행할 항목을 선택하세요. 현재 당신의 잔액은 {money}원 입니다. 1.구매 2.판매 3.재고확인 4.끝내기 : "))

    if i == 1 : 
        buy()

    elif i == 2 : 
        sell()

    elif i == 3 : 
        inven()

    elif i == 4 : 
        print("프로그램을 종료합니다.")         

    else : 
        print("잘못된 입력입니다.")
        menu()

def quit() :
    f = open('save.txt','w')
    f.writelines('id:{}\n'.format(saveid))
    
    

def buy() :
    global money
    i = int(input(f"구입할 항목의 번호를 입력하세요. 현재 당신의 잔액은 {money}원 입니다. 1.시발점(1000) 2.뉴런(3000) 3.수분감(5000) 4.드릴(7000) 5.킬캠(9000) : "))
    if i == 1 :
        if money >= 1000 :
            print("시발점을 구매합니다.")
            inventory["시발점"] += 1
            money -= 1000

        else :
            print("잔액이 부족합니다.")

    elif i == 2 :
        
        if money >= 3000 :
            print("뉴런을 구매합니다.")
            inventory["뉴런"] += 1
            money -= 3000

        else :
            print("잔액이 부족합니다.")

    elif i == 3 :
        if money >= 5000 :
            print("수분감을 구매합니다.")
            inventory["수분감"] += 1
            money -= 5000

        else :
            print("잔액이 부족합니다.")

    elif i == 4 :
        if money >= 7000 :
            print("드릴을 구매합니다.")
            inventory["드릴"] += 1
            money -= 7000

        else :
            print("잔액이 부족합니다.")

    elif i == 5 :
        if money >= 9000 :
            print("킬캠을 구매합니다.")
            inventory["킬캠"] += 1
            money -= 9000

        else :
            print("잔액이 부족합니다.")

    else : 
        print("잘못된 입력입니다.")
        buy()

    menu()

def sell() :
    global money
    i = int(input(f"판매할 항목의 번호를 입력하세요. 현재 당신의 잔액은 {money}원 입니다. 1.시발점(1000) 2.뉴런(3000) 3.수분감(5000) 4.드릴(7000) 5.킬캠(9000) : "))
    if i == 1 :
        if inventory.get("시발점") != 0 :
            print("시발점을 판매합니다.")
            inventory["시발점"] -= 1
            money += 1000

        else :
            print("재고가 부족합니다.")

    elif i == 2 :
        if inventory.get("뉴런") != 0 :
            print("뉴런을 판매합니다.")
            inventory["뉴런"] -= 1
            money += 3000

        else :
            print("재고가 부족합니다.")

    elif i == 3 :
        if inventory.get("수분감") != 0 :
            print("수분감을 판매합니다.")
            inventory["수분감"] -= 1
            money += 5000

        else :
            print("재고가 부족합니다.")

    elif i == 4 :
        if inventory.get("드릴") != 0 :
            print("드릴을 판매합니다.")
            inventory["드릴"] -= 1
            money += 7000

        else :
            print("재고가 부족합니다.")

    elif i == 5 :
        if inventory.get("킬캠") != 0 :
            print("킬캠을 판매합니다.")
            inventory["킬캠"] -= 1
            money += 9000

        else :
            print("재고가 부족합니다.")

    else : 
        print("잘못된 입력입니다.")
        sell()

    menu()

def inven() :
    print(f"현재 당신의 재고 : {inventory.items()}입니다.")
    menu()
    
def login() :
    global saveid,savepw,money, inventory
    f = open("save.txt","r")
    saveid = f.readline().split("=")[1].strip()   
    savepw = f.readline().split("=")[1].strip()
    money = int(f.readlines().split("=")[1].strip())
    inventory['시발점'] = f.readline().split("=")[1].strip()
    inventory['시발점'] = f.readline().split("=")[1].strip()
    inventory['시발점'] = f.readline().split("=")[1].strip()
    inventory['시발점'] = f.readline().split("=")[1].strip()
    inventory['시발점'] = f.readline().split("=")[1].strip()
        
    while True :
        inputid = input("아이디를 입력하세요 : ")
        if inputid == saveid :            

            while True :
                inputpw = hashlib.sha256(getpass.getpass('패스워드를 입력하세요 : ').encode()).hexdigest()
                if inputpw == savepw :
                    print("환영합니다, {}님!".format(saveid))
                    break

                else :
                    print("잘못된 패스워드입니다.")
                continue
            break

        else :
            print("잘못된 아이디입니다.")
            continue
    f.close()

        
if __name__ == '__main__':
    login()
    menu()
