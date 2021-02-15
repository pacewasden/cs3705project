import pandas as pd

addresses = {
    "mac": ['82:13:0b:06:45:41 ','82:13:0b:06:45:44 '],
    "ip": ['192.0.0.1', '192.0.0.2' ]
}

#edit to make sure that this works.

myvar= pd.DataFrame(addresses, index=['row1','row2'])
print(myvar['row2'])
