## if your script calling addressvalidation is not in "googlemaps" folder
## adjust sys path to the "googlemaps" folder  
# import sys
# sys.path.insert(0, './googlemaps')
import googlemaps

# Development Test key [INTERNAL]
gmaps = googlemaps.Client(key='AIzaSy')

# Address Validate an address
addressvalidation_result = gmaps.addressvalidation('1600 Amphitheatre Pk', regionCode='US', locality='Mountain View')
print(addressvalidation_result)