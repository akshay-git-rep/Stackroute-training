import mymath2 as mm2

from mymath import add as add1
from mymath import sub as sub1
from mymath2 import mul as mul1
from mymath2 import divi as divi1


result_add = mm2.mm1.add(10, 20)
result_sub = mm2.mm1.sub(100, 20)
result_mul = mm2.mul(10, 15)
result_div = mm2.divi(1000, 200)

print(result_add)
print(result_sub)
print(result_mul)
print(result_div)

print("variable defined in calling program")

print(add1(400, 100))
print(sub1(400, 50))
print(mul1(num1 = 50, num2 = 50))
print(divi1(500, 10))
