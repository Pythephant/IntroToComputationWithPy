pi = 3.14159

def circumferenc(radius):
	return 2*pi*radius

def area(radius):
	return pi*radius**2

def sophereSurface(radius):
	return 4*area(radius)

def sophereVolume(radius):
	return (4.0/3.0)*pi*(radius**3)
