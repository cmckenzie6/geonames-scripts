import json, urllib2, time

myAPIkey = 'YOUR API USERNAME HERE'
myLocationsJSON = '/path/to/your/file.json'

with open(myLocationsJSON) as data_file:    
    data = json.load(data_file)

timestr = time.strftime("%Y%m%d%H%M%S")

f = open('locations-'+timestr+'.txt', 'w')
	
for location in data:
	url = "http://api.geonames.org/searchJSON?q="+location["City"].replace(" ","+")+"&maxRows=1&username="+myAPIkey
	geonamesResponse = json.load(urllib2.urlopen(url))
	f.write(location["City"]+'\t'+location["Country"]+'\t'+location["Region"]+'\t')
	if geonamesResponse["geonames"]:
		f.write(geonamesResponse["geonames"][0]["lat"]+'\t'+geonamesResponse["geonames"][0]["lng"]+'\n')
	else:
		f.write("NULL"+'\t'+"NULL"+'\n')
		
f.close()