def get_grade(score):
    if score >= 91 and score <= 100:
        print('A')
    elif score >= 81 and score <= 90:
        print('B')
    elif score >= 71 and score <= 80:
        print('C')
    else:
        print('F')

score = int(input())
grade = get_grade(score)
print(grade)