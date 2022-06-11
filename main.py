from random import randrange

Success = 0
Fall = 0
Try = 100
Change = False

def Pick(rooms, Choice):
    while True:
        BotChoice = randrange(3)
        if BotChoice != Choice and rooms[BotChoice] == 0:
            break
    return BotChoice

for i in range(Try):
    # 염소 세팅 코드
    rooms = [0, 0, 0]
    rooms[randrange(3)] = 1
    Choice = randrange(3) # 몇번을 선택할지
    
    if Change: # 선택을 만약 바꾸면
        BotChoice = Pick(rooms, Choice)
        if rooms[BotChoice] == 0 and rooms[Choice] ==0:
            Success += 1
        else:
            Fall +=1

    else: # 선택을 바꾸지 않는다면
        if rooms[Choice] == 1:
            Success += 1
        else:
            Fall +=1

print(Success, Fall)

