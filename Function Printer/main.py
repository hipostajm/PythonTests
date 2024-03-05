import cmath
import matplotlib.pyplot as plt

# xList = []
# yList = []

# powers = int(input('Etner power of equation: '))
# num = list(input('Enter a,b,c,d... : ').split())

# for x in range(-3,3):
#     tempList = []
#     for power in range(1,powers+1):

#         x = x**power * float(num[-1*power])
#         tempList.append(x)

#         print(float(num[-1*power]))

#     y = sum(list(filter(lambda x: (x),tempList))) + float(num[-1])

#     yList.append(y)
#     xList.append(x)


a = float(input('Enter a of x^2: '))
b = float(input('Enter b of x: '))
c = float(input('Enter c: '))

delt = (b**2)-(4*a*c)

x0 = ((-1*b) - (cmath.sqrt(delt)))/2*a
x1 = ((-1*b) + (cmath.sqrt(delt)))/2*a

print(f"x = 0 at {x0} and {x1}")

xList = []
yList = []

for x in range(-100,100):
    y = (x**2)*a + x*b + c
    xList.append(x)
    yList.append(y)

plt.grid(visible=True, which='major', axis='both')
plt.plot(xList,yList)
plt.show()