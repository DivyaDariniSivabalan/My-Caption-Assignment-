k=input("STRING:")
def most_frequent(a):
    d=dict()
    for b in a:
        if b not in d:
            d[b]=1
        else:
            d[b]+=1
    return d
print(most_frequent(k))
a1_sorted_keys = sorted(most_frequent(k), key=most_frequent(k).get, reverse=True)
for r in a1_sorted_keys:
    print(r, most_frequent(k)[r])
