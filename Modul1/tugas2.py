random_list = [105, 3.1, "Hello" , 737, "python " , 2.7, "world" , 412, 5.5, "AI"]

int_dict = {"satuan": [], "puluhan": [], "ratusan": []}
float_tuple = ()
string_list = []

for item in random_list:
    if isinstance(item, int):
        if item < 10:
            int_dict["satuan"].append(item)
        elif item < 100:
            int_dict["puluhan"].append(item)
        else:
            int_dict["ratusan"].append(item)
    elif isinstance(item, float):
        float_tuple += (item,)
    elif isinstance(item, str):
        string_list.append(item)

# Menampilkan hasil
print("Integers (Dalam Dictionary):")
print(int_dict)
print("Floats (Dalam Tuple):")
print(float_tuple)
print("Strings (Dalam List):")
print(string_list)