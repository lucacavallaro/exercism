class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def compute_age_factor(self, earth_years):
        return round(self.seconds / (31557600 * earth_years), 2)

    def on_earth(self):
        return self.compute_age_factor(1)

    def on_mercury(self):
        return self.compute_age_factor(0.2408467)

    def on_venus(self):
        return self.compute_age_factor(0.61519726)

    def on_mars(self):
        return self.compute_age_factor(1.8808158)

    def on_jupiter(self):
        return self.compute_age_factor(11.862615)

    def on_saturn(self):
        return self.compute_age_factor(29.447498)

    def on_uranus(self):
        return self.compute_age_factor(84.016846)

    def on_neptune(self):
        return self.compute_age_factor(164.79132)


