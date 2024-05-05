import math

class MField():
    # numOfRings = N, eFlow = I, radius = R, length = l, magneticFieldIntensity = B, electricCharge = q, speed = v
    def __init__(self, numOfRings = 1 , eFlow = 1, radius = 1, length = 1):
        self.numOfRings = numOfRings
        self.eFlow = eFlow
        self.radius = radius
        self.length = length

    def ringed_mField_intensity(self, numOfRings, eFlow, radius):
        mu_0 = 4 * math.pi * 10**-7
        return (mu_0 * numOfRings * eFlow) / (2 * radius)
    
    def solenoid_mField_intensity(self, numOfRings, eFlow, length):
        mu_0 = 4 * math.pi * 10**-7
        return (mu_0 * numOfRings * eFlow) / (length)