import sub

while True:
    print('연산기호를 입력 후 계산할 숫자를 입력하세요')
    print('ex)\t* \n \tn1 n2 \n e.종료')
    operator = input()
    if operator == 'e':
        break
    else:
        n1,n2 = map(int,input().split())
        print(sub.cal(operator,n1,n2))

