temprature = int(input("Please enter Celsius Tempreture: "))
###int(input("Please enter Celsius Tempreture: "))
def calc_far(t):
    if t < -273.15:
        return "Temp doesnt make sens"
    else:
        c = t * 9/5 +32
        return temprature,'C Temriture is equial', c," F"
#for i in temprature:
print(calc_far(temprature))
