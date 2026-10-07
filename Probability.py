import random

def ball(): 
    balls = ['Orange', 'Red', 'Blue']
    result = random.choice(balls)

    pro = balls.count('Red')/len(balls)
    print('Probability of picking red ball is: ', pro)

    if result == 'Red': 
        return 'Red ball was picked'
    else: 
        return 'better luck next time'

res = ball()
print(res)