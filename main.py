import random as rd 
choices = ['rock', 'scissors', 'paper']
movement_choices = ['scissors', 'paper', 'rock']
result_list = []
def wrapper(x):
    print(f"""
    ***********************************************************
                                 {x}
    ***********************************************************
    """)
while True:
    user_answer = input('what is your pick? (r)ock, (p)aper or (s)cissors?').lower()
    wrapper('')
    if user_answer in ['quit','exit','kill','end','teminate','x']:
        for item in result_list:
            wrapper(item)
        break 
    value_map_usr = {'r':'rock', 'p':'paper', 's':'scissors'}
    user_choise = value_map_usr[user_answer]
    robot_choise = rd.choice(choices)
    for i,c in enumerate(choices):
        if user_choise == c:
            if robot_choise == movement_choices[i]:
                print('player won')
                result_list.append('player')
                break
        elif user_choise == robot_choise:
            print('tie')
            result_list.append('tie')
            break
    else:
        print('robot won')
        result_list.append('robot')
        


