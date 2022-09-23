"""
1.1부터 10000까지의 숫자를 numbers변수에 할당해 주세요
2. 1부터 10000까지 숫자 중, 짝수에 해당하는 숫자만 `even_numbers` 변수에 할당해주세요
3. 1부터 10000까지의 숫자 중, 3의 배수이며 15의 배수가 아닌 숫자에 10을 곱하여 `some_numbers` 에 할당해주세요
"""   
def get_even_numbers(numbers):
    result = list(filter(lambda x: x%2 == 0,numbers))
    # result = [x for x in numbers if x%2==0]
    
    return result

def get_some_numbers(numbers):
    result = [x*10 for x in numbers if x%3==0 and x%15 != 0]
    # some code
    return result

def main():
    numbers = [] # 1 ~ 10000
    for i in range(1,10001):
        numbers.append(int(i))
    #numbers = list(range(1,10001)) case_2
    #numbers = [x for x in range(1,10001)] case_3
    even_numbers = get_even_numbers(numbers)
    some_numbers = get_some_numbers(numbers)
    print(even_numbers) # [2, 4, 6, ...]
    print(some_numbers) # [30, 60, 90, 120, 180, ...]
    
main() 
