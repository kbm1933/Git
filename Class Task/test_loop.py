'''
사용자의 입력을 받아 반복하는 프로그램
1.정수를 입력 받으면 입력값의 2배 수를 출력
2.문자를 입력 받으면 f-string으로 '입력한 문자는 {} 입니다' 출력
3.사용자가 exit를 입력 하거나 숫자를 5번 입력 받으면 프로그램 종료
'''
cnt = 0
while cnt <= 5:
    num = input()
    try:
        num_ = int(num)
        print(num_ * 2)
        cnt+=1
        pass
    except:
        print(f'입력한 문자는 {num}입니다.')
        break

    if num == 'exit' or cnt >= 5:
        break
