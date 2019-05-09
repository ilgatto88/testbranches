# developer code reset 12:49

c = [12.3, 14.5, 17.2, 1.3]
k = [290, 310, 273.15, 280]

def celsius_to_kelvin(celsius = None):
	result = [c+273.15 for c in celsius]
	return result
	
def kelvin_to_celsius(kelvin = None):
	result = [k-273.15 for k in kelvin]
	return result
	
print(celsius_to_kelvin(celsius = c))
print(kelvin_to_celsius(kelvin = k))