
def find_common(a, b):
    # Removes duplicates and ignores order
    return list(set(a) & set(b))

if __name__=="__main__":
    a=[1,2,3,4,5]
    b=[3,4,5,6,7]
    print(find_common(a,b))


# def find_common(a, b):
#     res = []
#     for i in a:
#         for j in b:
#             if i == j:
#                 res.append(i)
#     return res 

