import pandas as pd
import geolocation

addresses = {
    "mac": ['82:13:0b:06:45:41 ','82:13:0b:06:45:44 '],
    "ip": ['192.0.0.1', '192.0.0.2' ]
}

#edit to make sure that this works.
# testdata=pd.read_csv('testdata.csv')
# print(testdata[453].to_string())

print(geolocation.location('161.170.236.29'))
