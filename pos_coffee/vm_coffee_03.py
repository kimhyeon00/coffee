from coffee import show_menu, coffee_process, input_coin
import coffee

menu = '0'

while menu != '5':

    show_menu()
    menu= input('메뉴선택:')
    coffee_process(menu)
    print('잔액:',coffee.user_coin)