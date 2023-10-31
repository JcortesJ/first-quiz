################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / / 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/   
#                                                                        
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.

def get_city_temperature(city):
   #In this case we strip and lower the strings to avoid misspelling in the names of the cities
   #we also add the newyork case
   city = city.replace(" ","").lower()
   if city == "quito":
      return 22
   if city == "saopaulo":
      return 17
   if city == "sanfrancisco":
      return 16
   if city =="newyork":
      return 14

def get_city_weather(city):
# we add the remaining cases to avoid errors in testing
  sky_condition = None
  city = city.replace(" ","").lower()
  if city == "saopaulo":
     sky_condition = "cloudy"
  if city == "newyork":
     sky_condition = "rainy"
  if city == "quito":
     sky_condition = "sunny"
  if city == "sanfrancisco":
     sky_condition = "partly sunny"
     
  temperature = get_city_temperature(city)
  if sky_condition:
      return str(temperature) + " degrees and " + sky_condition
  else:
     #we add an extra case if sky_condition is None
      return str(temperature) + " degrees, with no info about sky condition"