num = int(input())
sum =0
i=1
while sum < num:
    sum += i
    i += 1

block = i - 1
step = num - (sum - block)

# 감소하는 경우
if block%2==1:
    a=block
    b=1
    for i in range(step-1):
        a= a-1
        b= b +1

# 증가하는 경우
else:
    a=1
    b=block
    for i in range(step-1):
        a= a+1
        b= b-1

print(str(a)+"/"+str(b))