
def all_variants(string):
    for i in range(1,len(string)+1):
        for j in range(len(string)):
            if j+i<=len(string):
                yield f'i={i}, j={j}, string[{j}:{j+i}] = {string[j:j + i]}'
            else:
                next

a = all_variants("abc")
for i in a:
    print(i)