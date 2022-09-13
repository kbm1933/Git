'''
1. 사용자의 입력을 받아 n개의 중복되지 않는 랜덤한 숫자를 생성한다.
2. 프로그램이 시작 된 시간을 기록한다.
3. 사용자의 입력을 받고, 입력을 받을 때마다 try count를 1씩 더해준다.
4. 사용자 입력x와 랜덤하게 생성 된 y 두 숫자를 비교한다.
    4-a. x의 첫 번째 숫자가 y에 포함되어 있는지 확인한다.
        * 포함되어 있지 않다면 out count + 1
    4-b. x의 첫 번째 숫자가 y에 포함되어 있다면 x의 첫 번째 숫자와 y의 첫 번쨰 숫자가 일치하는지 확인한다.
        * 일치하는 경우 strike count + 1
        * 일치하지 않는 경우 ball count + 1
    4-c. 4-a ~ 4-b를 x의 모든 자릿수를 돌 때까지 반복한다.
5. 사용자가 exit을 입력하거나 정답을 맞출 때까지 3~4의 동작을 무한하게 반복한다.
6. 사용자의 입력이 1번에서 생성한 숫자와 일치 할 경우 필요한 정보를 출력하고 프로그램을 종료한다.
    6-a. try count를 출력한다.
    6-b. 프로그램이 종료 된 시간과 프로그램이 시작 된 시간의 차를 계산해 프로그램의 실행 시간을 출력한다.
    6-c. 게임이 종료 된 시점의 날짜와 시각을 출력한다.
--------------------
문제점
시간 측정이 안돼는 이유
exit입력을 좀더 자유롭게 받을 수 없는지?
-숫자를 입력받고 exit입력을 받을지 안받을지 대기 하기때문에 코드 진행이 매끄럽지 못함
guess는 일반 input인데 왜 int형 오류가 발생하는 것인가
리스트를 전부 str로 변경하여 구분 해야 하는건지?
'''
import random
import time
from datetime import datetime

start_time = time.time()
end_time = time.time()
num_list = []
t_count = 0
time.sleep(1)

print('게임에 이용할 숫자 갯수를 입력하세요(1~10)')
set_game_ball = input()
count_number = set_game_ball

while len(num_list) < int(count_number):
    random_num = random.randint(0,9)
    if random_num not in num_list:
        num_list.append(random_num)
    
print(f'게임 숫자 {count_number}만큼 랜덤 생성 되었습니다.')
print(num_list)

while True:
    s_count = 0
    b_count = 0
    t_count +=1
    
    guess_list = []
    guess = input(f'숫자{count_number}자리수 입력:(게임종료exit)')
    
    if guess == 'exit':
        break
    else:
        pass

    for i in range(0,int(count_number)):
        guess_list.append(int(guess[i:i + 1]))
    print(guess_list)

    for i in range(0,int(count_number)):
        if guess_list[i] == num_list[i]:
            s_count +=1
        elif guess_list[i] in num_list:
            b_count += 1

    
    print('%d Strike' % s_count)
    print('%d Ball' % b_count)
    if(num_list == guess_list):
        print('%d번 만에 정답' % t_count)        
        print(datetime.now())
        break
print(f'걸린시간 : {end_time - start_time: .5f}')