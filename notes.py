# single line comment by # and multi line comment by "" '''
# print("heelooo") ye string hai, print(hello) ye function hai
# indentation is used to know the scope, or to definwe the code blocks, jo space ati hai code likne ke bd ex if codition ko define krne ke bd
#ismein brackets use nhi hote yaha pr space ka use nhi hota, space ka use sirf indentation ke liye hota hai
age = 20
if (age>18):
    print("you are eligible to vote")
# line continuation : to continue the satetment written on next line we use \ at the end of the line
total = 10 + 20 + 30 + \
        40 + 50
print(total)   # 150
#literals are the data which is assigned to a variable, like 10, 3.14, "hello", True, 10+3j
# integer, float, string, boolean, complex
a = 10
print(type(a))
b = "hello"
print(type(b))
c = 3.14
print(type(c))
d = True
print(type(d))
e = 10+3j
print(type(e))
# none is a data type which is used to represent the absence of a value or a null value
f = None
print(type(f))
#collection data types: list, tuple, set, dictionary
g = [1, 2, 3]
print(type(g))
h = (1, 2, 3)
print(type(h))
i = {1, 2, 3}
print(type(i))
j = {"name": "Alice", "age": 20}
print(type(j))
# disadvantage of python slow language
#list and tupple diff ?? list is mutable and tupple is immutable, list can be changed but tupple cannot be changed,
#  list is not secure while tupple is secure, list is slower than tupple, list takes more memory than tupple
# set contains hetrogeneous data types, set is unordered, set is mutable, set does not allow duplicate values, set is faster than list and tupple
# dono main indexing aram se kr sakte ho for transversing,pr set main koi definite pos nhi hai
# set is not indexable as they are unordered, set is not subscriptable, set is not sliceable, set is not iterable, set is not hashable, set is not comparable, set is not sortable
#dic is pair of key and value, dic is mutable, dic is unordered, dic is not indexable, dic is not sliceable, dic is not iterable, dic is not hashable, dic is not comparable, dic is not sortable
# dic is accesed due to key
# variables
# we use python 3 
# before python 2 was used, python 2 is not supported now, python 3 is the latest version of python