import math
print(dir(math)) # This will output a list of all the names defined in the math module.

print(math.floor(3.1416))

from math import * # import all functions and variables from a module.

from math import sqrt, pi

print(sqrt(9))

import math as math_builtin_python

result = math_builtin_python.sqrt(9) * math_builtin_python.pi
print(result)