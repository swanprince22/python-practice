# working with integers and floats

a = 50
b = 7

print(a+b)
print(a-b)
print(a*b)
print(a/b)

float_a = 12.0
float_b = 4.9

print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a+float_b)

print(a%b)
print(float_a%float_b)

print(a//b) # takes the floor (rounds the number down to the nearest whole integer. e.g. 13.45 -> 13)
print(float_a//float_b)

print(a**b) # exponentiation

c = 13
print(type(float(c))) 

float_c = 25.13
print(type(int(float_c)))

str_int_d = "45"
str_float_d = "15.67"

print(type(int(str_int_d)))
print(type(float(str_float_d)))

float_e = 4.798
float_f = 4.251

print(round(float_e))
print(round(float_f, 1))

negative_num = -15
print(abs(negative_num))

print(bin(a)) # converts to binary representation
print(oct(a)) # converts to octal representation
print(hex(a)) # converts to hexadecimal representation

result_1 = pow(2,3)
print(result_1)
      
