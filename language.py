my_list=[]
for name in list_countries:
    for i in name["languages"]:
        my_list.append(i)
print(my_list)
unique = set(my_list)
language_total = {} # empty dict

for n in unique:
    language_total[n] = my_list.count(n)
my_dict1={}
# Find the key with the largest value
counter=0
while language_total:
    max_value = max(language_total.values())
    max_key = max(language_total,key=language_total.get)
    my_dict1[max_key]=max_value
# Remove the key-value pair
    del language_total[max_key]
    counter+=1
    if counter==10:
        break
print(my_dict1)
