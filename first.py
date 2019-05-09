# main code reset 12:48

c = [12.3, 14.5, 17.2, 1.3]

def celsius_to_kelvin(celsius = None):
	result = [c+273.15 for c in celsius]
	return result
	
print(celsius_to_kelvin(celsius = c))