import material as m

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
        case 'b'|'B'|'ㅠ':
            show_metarials()
            
        case '_':
            print('잘못입력')    

def check_material(material):
    match material:
        case '밀크':
            if m.coffee_material['coffee'] >= 10 and \
                m.coffee_material['cream'] >= 20 and \
                m.coffee_material['suger'] >= 10:
                return True
        case '설탕':
            if m.coffee_material['coffee'] >= 10 and \
                m.coffee_material['suger'] >= 10:
                return True
        case '블랙':
            if m.coffee_material['coffee'] >= 10:
                return True
    return False

def made_coffee(coffee):
    global coffee_price, user_coin, vm_coin
    check_material(coffee)
    price = coffee_price[coffee]

    if user_coin >= price:

        # 커피 제조과정
        if coffee == "밀크":
            if check_material(coffee):
                m.coffee_material['coffee'] -= 10
                m.coffee_material['cream'] -= 20
                m.coffee_material['suger'] -= 10
                print(coffee,'커피 나왔습니다.')
            else:
                print('재료가 부족합니다.')
        elif coffee == '설탕':
            if check_material(coffee):
                m.coffee_material['coffee'] -= 10
                m.coffee_material['suger'] -= 10
                print(coffee,'커피 나왔습니다.')
            else:
                print('재료가 부족합니다.')
        elif coffee == '블랙':
            if check_material(coffee):
                m.coffee_material['coffee'] -= 10
                print(coffee,'커피 나왔습니다.')
            else:
                print('재료가 부족합니다.')

        if user_coin >= price:
            user_coin-=price
            vm_coin+=price
            print('잔액: ',user_coin)
            print('매출: ',vm_coin)

def admin_total_sales():
    print('총 판매금액:')

def show_metarials():
    print('------------커피 제고-------------')
    print('커피: ',m.coffee_material['coffee'])
    print('크림: ',m.coffee_material['cream'])
    print('설탕: ',m.coffee_material['suger'])
    print('---------------------------------')


def input_coin():
    global user_coin
    in_coin=-1

    print('동전입력')

    while True:
        try:
            in_coin=int(input('메뉴에 알맞는 동전 입력'))
        except:
            print('동전은 숫자로 입력해주세요.')
    
        if in_coin > 0:
            user_coin +=in_coin
            print('user_coin',user_coin)
            break
    

def admin_total_sales():
    print('총 판매금액:',vm_coin)

def show_menu():

    coffee_menu = """
            1. 밀크커피(300원)

            2. 설탕커피(300원)

            3. 블랙커피(200원)

            4. 동전입력

            a. 관리자 기능(판매금액)

            b. 관리자 기능(재고)

            5. 종료
    """
    print(coffee_menu)

user_coin=0     #사용자가 입력한 동전

vm_coin=0   # 자판기 매출

coffee_price= {"밀크":300,'설탕':300,'블랙':200} #커피 가격 # 열쇠와 가격을 ':'로 묶어서 저장

# input_coin()

made_coffee('밀크')

show_metarials()


            