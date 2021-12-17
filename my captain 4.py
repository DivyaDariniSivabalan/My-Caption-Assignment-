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
def sort_dict_by_key(di,reverse=False):
    return dict(sorted(di.items(),reverse=reverse))
print("SORTED IN DESCENDING ORDER")
print(sort_dict_by_key(most_frequent(k),True))
