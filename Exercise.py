'''import platform
import datetime
x = platform.system()
print(x)
x = datetime.datetime.now()
print(x.strftime("%x"))

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)

print(x)


# use four indents to make it easier to read the result:
print(json.dumps(x, indent=2, separators=(",","+")))
'''
'''
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("h...o", txt)

print(x)

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())



import numpy as np
from numpy import random

arr = np.array([1, 2, 3, 5])
print(arr)
x = random.randint(10)
print(x)

from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()
'''

from numpy import random

x = random.normal(size = (6, 3))

print(x)