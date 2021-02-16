import pandas as pd

addresses = {
    "mac": ['82:13:0b:06:45:41 ','82:13:0b:06:45:44 '],
    "ip": ['192.0.0.1', '192.0.0.2' ]
}

#edit to make sure that this works.
testdata=pd.read_csv('testdata.csv')
print(testdata.to_string())
