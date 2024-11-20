def coffee_process(menu):
    global user_coin

    match menu:
        case '1':
            made_coffee('밀크')
        case '2':
            made_coffee('설탕')
        case '3':
            made_coffee('블랙')
        case '4':
            input_coin()
        case 'a'|'A':
            admin_total_sales()
            
        case '_':
            print('잘못입력')    


def made_coffee(coffee):
        global coffee_price, user_coin, vm_coin

        price = coffee_price[coffee]


        if user_coin >= price:
            print(coffee,'커피 나왔습니다.')
            user_coin-=price
            vm_coin+=price
            print('잔액: ',user_coin)
            print('매출: ',vm_coin)

def input_coin():
    global user_coin

    print('insert coin')
    in_coin=int(input('메뉴에 알맞는 동전 입력: '))
    user_coin+=in_coin
    print('user_coin',user_coin)

def admin_total_sales():
    print('총 판매금액:',vm_coin)

def show_menu():

    coffee_menu = """
            1. 밀크커피(300원)

            2. 설탕커피(300원)

            3. 블랙커피(200원)

            4. 동전입력

            a. 관리자 기능(판매금액)

            5. 종료
    """
    print(coffee_menu)

user_coin=0     #사용자가 입력한 동전

vm_coin=0   # 자판기 매출

coffee_price= {"밀크":300,'설탕':300,'블랙':200} #커피 가격 # 열쇠와 가격을 ':'로 묶어서 저장

while True:

    show_menu()
    
    menu= input("메뉴선택: ")

    coffee_process(menu)
    
     # 'def 함수'를 불러옴 # 이 함수 내에서 사용되는 변수는 지역변수로,
    #그 값이 일반적으로는 함수 밖으로 나올 수 없음 때문에 global 을 사용하여 전역변수로 선언해 줘야 함.
    
    if menu =="5":
        break

    
print('-----------program end--------------')