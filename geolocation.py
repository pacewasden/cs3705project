from ip2geotools.databases.noncommercial import DbIpCity
def location(ipaddress):
    response = DbIpCity.get(ipaddress, api_key='free')
    return(response.city)

#print(location('147.229.2.90'))