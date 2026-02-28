import sys

form = sys.stdin.readline()

if "-" not in form:
    numbers = list(map(int, form.split("+")))
    print(sum(numbers))
else:
    sub_forms = list(form.split("-"))
    
    for i in range(len(sub_forms)):
        sum_num = 0

        if "+" in sub_forms[i]:
            sub_nums = list(map(int, sub_forms[i].split("+")))
            sum_num = sum(sub_nums)
            
            sub_forms[i] = sum_num

    answer = int(sub_forms[0])
    for i in range(1, len(sub_forms)):
        answer -= int(sub_forms[i])    
    print(answer)

            
        