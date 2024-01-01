def count(start=1, stop=5):
    for i in range(start,stop+1):
        yield i

my_gen = count(1,50)
print('Hasilnya', end=" ")
for n in my_gen:
    print(n, end=" ")