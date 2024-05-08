from collections import defaultdict
while True:
    try:
        x=int(input('Value: '))
    except ValueError:
        # print('error')
        pass
    else:
        break
print(x)
# Initializing an ordinary dictionary
# res = {}
# res=defaultdict(list)
# # Adding elements to the dictionary
# try:
#     res[1] = ['apple']
#     res[2] = ['banana']
#     res[2]=['almond'] #overriding
#     res[1].append('apricot')
#     res[3].append('orange')
#     raise KeyError
# except(KeyError):
#     print('error')

# print(res)
