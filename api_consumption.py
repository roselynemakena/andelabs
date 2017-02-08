import requests
base_url = 'http://api.openweathermap.org/data/2.5/weather'
api_key='008609466db81f5f971a7ff1e0c14774'
def get_weather_by_city(city):
	query = base_url+'?q=%s&units=metric&APPID=%s'%(city,api_key)
	try:
		res = requests.get(query)
		print("*******success*****")
		if(res.status_code !=200):
			return 'City not found'
		else:
			weather_info = res.json()
			return weather_info
	except requests.exceptions.RequestException as error:
    		print(error)
	except:
		print("Some Exception error")
		raise Exception("**********************")
	return
		#errror or data

weathers = get_weather_by_city('London')
print(weathers)
