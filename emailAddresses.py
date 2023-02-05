# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils
numOfEmail = input()
valid = []
addresses = []

for i in range(int(numOfEmail)):
    addresses.append(input())

for x in range(len(addresses)):
    name, email = addresses[x].split()
    if bool(re.match('<[a-zA-Z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>', email)):
        valid.append(addresses[x])
out = "\n".join(valid)
print(out)

#vineet <vineet@gmail.com>
#vineet <vin-nii@gmail.com>
#vineet <v__i_n-n_ii@gmail.com>
