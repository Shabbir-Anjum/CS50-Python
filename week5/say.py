# import sys
# import  cowsay
# if len(sys.argv)==2:
#     cowsay.cow('Hello, '+ sys.argv[1])
import sys
from saying import man2
if len(sys.argv)!=2:
    
    sys.exit('ERROR')
    
man2(sys.argv[1])
