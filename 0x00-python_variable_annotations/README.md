# 0x00. Python variable annotations

## Tasks
0. Basic annotations - add

Write a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float.

```py
>>> print(add.__annotations__)
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```

File: [0-add.py](./0-add.py)
   
1. Basic annotations - concat

Write a type-annotated function `concat` that takes a string `str1` and a string `str2` as arguments and returns a concatenated string

```py
>>> print(concat.__annotations__)
{'str1': <class 'str'>, 'str2': <class 'str'>, 'return': <class 'str'>}
```

File: [1-concat.py](./1-concat.py)

2. Basic annotations - floor

Write a type-annotated function `floor` which takes a float `n` as argument and returns the floor of the float.

```py
>>> print(floor.__annotations__)
{'n': <class 'float'>, 'return': <class 'int'>}

>>> print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
floor(3.14) returns 3, which is a <class 'int'>
```

File: [2-floor.py](./2-floor.py)
   
3. Basic annotations - to string

Write a type-annotated function `to_str` that takes a float `n` as argument and returns the string representation of the float.

```py
>>> print(to_str.__annotations__)
{'n': <class 'float'>, 'return': <class 'str'>}

>>> print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
to_str(3.14) returns 3.14, which is a <class 'str'>
```

File: [3-to_str.py](./3-to_str.py)
   
4. Define variables

Define and annotate the following variables with the specified values:

`a`, an integer with a value of 1

`pi`, a float with a value of 3.14

`i_understand_annotations`, a boolean with a value of True

`school`, a string with a value of “Holberton”

```py
>>> print("a is a {} with a value of {}".format(type(a), a))
a is a <class 'int'> with a value of 1

>>> print("pi is a {} with a value of {}".format(type(pi), pi))
pi is a <class 'float'> with a value of 3.14

>>> print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
i_understand_annotations is a <class 'bool'> with a value of True

>>> print("school is a {} with a value of {}".format(type(school), school))
school is a <class 'str'> with a value of Holberton
```

File: [4-define_variables.py](./4-define_variables.py)

5. Complex types - list of floats

Write a type-annotated function `sum_list` which takes a list `input_list` of floats as argument and returns their sum as a float.

```py
>>> print(sum_list.__annotations__)
{'input_list': typing.List[float], 'return': <class 'float'>}
```
File: [5-sum_list.py](./5-sum_list.py)
   
6. Complex types - mixed list

Write a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float.

```py
>>> print(sum_mixed_list.__annotations__)
{'mxd_lst': typing.List[typing.Union[int, float]], 'return': <class 'float'>}
```
File: [6-sum_mixed_list.py](./6-sum_mixed_list.py)
   
7. Complex types - string and int/float to tuple

Write a type-annotated function `to_kv` that takes a string `k` and an int OR float `v` as arguments and returns a tuple. The first element of the tuple is the string `k`. The second element is the square of the int/float `v` and should be annotated as a float.

```py
print(to_kv.__annotations__)
{'k': <class 'str'>, 'v': typing.Union[int, float], 'return': typing.Tuple[str, float]}
```
File: [7-to_kv.py](./7-to_kv.py)

8. Complex types - functions

Write a type-annotated function `make_multiplier` that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.

```py
>>> print(make_multiplier.__annotations__)
{'multiplier': <class 'float'>, 'return': typing.Callable[[float], float]}

>>> fun = make_multiplier(2.22)
>>> print("{}".format(fun(2.22)))
4.928400000000001
```
File: [8-make_multiplier.py](./8-make_multiplier.py)

9. Let's duck type an iterable object

Annotate the below function’s parameters and return values with the appropriate types

```py
def element_length(lst):
    return [(i, len(i)) for i in lst]
```
```py
>>> print(element_length.__annotations__)
{'lst': typing.Iterable[typing.Sequence], 'return': typing.List[typing.Tuple[typing.Sequence, int]]}
```
File: [9-element_length.py](./9-element_length.py)
   
10. Duck typing - first element of a sequence

Augment the following code with the correct duck-typed annotations:

**The types of the elements of the input are not know**
```py
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
```
```py
>>> print(safe_first_element.__annotations__)
{'lst': typing.Sequence[typing.Any], 'return': typing.Union[typing.Any, NoneType]}
```
File: [100-safe_first_element.py](./100-safe_first_element.py)
   
11. More involved type annotations

Given the parameters and the return values, add type annotations to the function

**Hint: look into `TypeVar`**

```py
def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
```
```py
>>> annotations = safely_get_value.__annotations__
>>> for k, v in annotations.items():
...    print( ("{}: {}".format(k, v)))
dct: typing.Mapping
key: typing.Any
default: typing.Union[~T, NoneType]
return: typing.Union[typing.Any, ~T]
```
File: [101-safely_get_value.py](./101-safely_get_value.py)
   
12. Type Checking

Use mypy to validate the following piece of code and apply any necessary changes.

```py
>>> def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
...     zoomed_in: Tuple = [
...         item for item in lst
...         for i in range(factor)
...     ]
...     return zoomed_in
>>> array = [12, 72, 91]
>>> zoom_2x = zoom_array(array)
>>> zoom_3x = zoom_array(array, 3.0)
>>> print(zoom_array.__annotations__)
{'lst': typing.Tuple, 'factor': <class 'int'>, 'return': typing.List}
```
File: [102-type_checking.py](./102-type_checking.py)
