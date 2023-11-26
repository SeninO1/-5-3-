x = int(input())
a = int(input())
b = int(input())
if x <= a and x <= b:
    print('2')
elif x <= a:
    print('Mike')
elif x <= b:
    print('Ivan')
elif x <= (a + b):
    print('1')
elif x > (a + b):
    print(0)