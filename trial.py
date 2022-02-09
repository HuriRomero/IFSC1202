from math import pi
one = "one"
two = "two"
three = "three"

print("{}{}{}".format("one", "two", "three"))
print("one = {:s}, two = {:s}, three = {:s}".format(one, two, three))
print("one = {:8s}, two = {:8s}, three = {:8s}".format(one, two, three))
print("one = {:.2s}, two = {:.2s}, three = {:.2s}".format(one, two, three))
print("x{:4.1f}x".format(pi))
print('{:,.2f}'.format(123456789.017))