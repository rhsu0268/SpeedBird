import requests
import json

resp = requests.get('http://terminal2.expedia.com/x/mflights/search?departureAirport=CLT&arrivalAirport=JFK&departureDate=2016-04-22&numberOfAdultTravelers=1&apikey=MxAMm4mA6fjaGZ8jN3oDK7BJa3FTOvWG')

# url = 'http://terminal2.expedia.com:80/x/flights/overview/get'

# params = dict(
# 	airOverviewSearchRequest={"MessageHeader": { "ClientInfo": { "DirectClientName": "Hackathon"}, "TransactionGUID": ""},
# 	"tpid": 1, "eapid": 0, "PointOfSaleKey": { "JurisdictionCountryCode": "USA", "CompanyCode": "10111", "ManagementUnitCode": "1010" },

# 	"OriginAirportCodeList": {
# 	"AirportCode": ["JFK"]
# 	},
# 	"DestinationAirportCodeList": {
# 	"AirportCode": ["SFO", "OAK"]
# 	},

# 	"FlightListings": { },
# 	"apikey": "MxAMm4mA6fjaGZ8jN3oDK7BJa3FTOvWG"
# 	}
# )

# resp = requests.get(url=url, params=params)
if resp.status_code != 200:
	raise ApiError('GET /places/ {}'.format(resp.status_code))
else:

	data_file = open('iad_jfk.txt', 'w+')

	# write the json to the file
	data = resp.json()

	legs = resp.json()

	legs = legs['legs']

	paths = []
	path = []


	for leg in legs:
		#print(leg)
		leg_string = str(leg)
		#print(item_string)
		#data_file.write(leg_string + '\n')

		segments = leg['segments']
		counter = 0
		#print(segments)
		for segment in segments:
			
			counter = counter + 1
			#print(counter)
			#print(segment['arrivalAirportCode'])
			departureAirportCode = segment['departureAirportCode']
			distance = segment['distance']
			arrivalAirportCode = segment['arrivalAirportCode']
			path.append(departureAirportCode)
			path.append(distance)
			path.append(arrivalAirportCode)
			paths.append(path)
		print (path)
		# write the path to the file
		data_file.write("%s\n" % path)
		# reset path list
		path = []
	#print(paths)

	# close the file
	data_file.close()

	
