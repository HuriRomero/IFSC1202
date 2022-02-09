fromvalue = float(input("Enter from Value: "))
fromunit = (input("Enter from unit (in, ft, yd, mi): "))
tounit = input("Enter From Unit (in, ft, yd, mi): ")

if FromUnit == "in" and ToUnit == "ft": multiplier = 0.08333333333333 
if FromUnit == "ft" and ToUnit == "yd": multiplier = 0.3333333333
if FromUnit == "yd" and ToUnit == "mi": multiplier = 0.0005681818181818
if FromUnit == "mi" and ToUnit == "yd": multiplier = 1760
if FromUnit == "yd" and ToUnit == "ft": multiplier = 3 
if FromUnit == "ft" and ToUnit == "in": multiplier = 12

result = multiplier * fromvalue
print(round(fromvalue, "=>", result),7)
