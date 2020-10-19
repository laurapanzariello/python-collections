print("breakpoint: calls pdb by default, debbuger")
# breakpoint()

print("abs: absolute value of a number")
pi = -3
complex_number = 3+4j
print(pi, complex_number)
print(abs(pi), abs(complex_number))

print("all: return true if all elem of iterable are true")
a = ["a", "b", 12]
b = ["c", "", 10]
c = ["d", -9, (12, 1)]
d = []
print(all(a), " - ", a)
print(all(b), " - ", b)
print(all(c), " - ", c)
print(all(d), " - ", d)

print("any: return true if any elem of iterable is true")
print(any(a), " - ", a)
print(any(b), " - ", b)
print(any(c), " - ", c)
print(any(d), " - ", d)

print("return a complex number")
print(complex(3, 4))

"""
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
"""



