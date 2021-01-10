import requests

print("Welcome to Weather Check!")

def Get_zip():
  get_zip = input("Please enter zip code: ")
  url = "https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=00eaa7a3ee94361186ed72f0745a902f".format(get_zip)
  request = requests.get(url) #request data
  weather_details = request.json() #get data in json format
  
  try:
    print_info(weather_details)
    
  except: #invalid input
    print("Please enter valid city name. \n ")
    Get_zip() #restart program
  
def Restart_program():
  add_location = input("Would you like to check forecast for another location? \n ")
  if add_location == "yes":
    Get_zip()
  elif add_location == "no":
    print("Thank you for using Weather Check. Goodbye!")
    return
  
  else: #invalid input
    print("Input is invalid. Please enter 'yes' or 'no'. ")
    Restart_program()

def print_info(weather_details):
    
    temp = weather_details["main"]["temp"]
    highTemp = weather_details["main"]["temp_max"]
    lowTemp = weather_details["main"]["temp_min"]
    wind_speed = weather_details["wind"]["speed"]
    pressure = weather_details["main"]["pressure"]
    latitude = weather_details["coord"]["lat"]
    longitude = weather_details["coord"]["lon"]
    humid = weather_details["main"]["humidity"]
    weather_description = weather_details["weather"][0]["description"]
    

    print("Current temperature: {} Degree(s) Fahrenheit".format(temp))
    print("Highest temperature: {} Degree(s) Fahrenheit".format(highTemp))
    print("Lowest temperature: {} Degree(s) Fahrenheit".format(lowTemp))
    print("Wind speed: {} Meters A Second".format(wind_speed))
    print("Pressure: {} hecto Pascals".format(pressure))
    print("Latitude: {}".format(latitude))
    print("Longitude: {}".format(longitude))
    print("Humidity: {} Percent".format(humid))
    print("Weather description: {}".format(weather_description))

    Restart_program()
    
#run full program
Get_zip
  