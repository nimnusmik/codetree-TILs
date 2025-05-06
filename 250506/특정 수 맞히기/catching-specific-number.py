while True:
    user_input = int(input())
    if user_input == 25: 
        print('Good')
        break
    else:
        if user_input < 25: print('Higher')
        if user_input > 25: print('Lower')