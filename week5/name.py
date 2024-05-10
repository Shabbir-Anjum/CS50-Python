import sys
# try: 
#     print('hello are you', sys.argv[1],sys.argv[2])
# except:
#     print('error')
if len(sys.argv)<2:
    sys.exit('error')
    # print('lower')
elif len(sys.argv)>2:
       sys.exit('error')
# else:

print('are you ', sys.argv[1])