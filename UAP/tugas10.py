from functools import reduce

def count(start=1, stop=5):
    for i in range(start,stop+1):
        yield i

my_gen = count(1,50)

div_by_3 = filter(lambda my_gen: my_gen % 3 == 0, my_gen)
print(tuple(div_by_3), "kelipatan 3")

sum = reduce(lambda x, y : x + y,  tuple(div_by_3))
print(f"jumlah semuanya = {sum} ")