class Battery:
    def __init__(self, battery, power) -> None:
         self.percent = battery.percent
         self.status = battery.power_plugged
         self.power = power
    
    def __repr__(self) -> str:
        return f"""Battery: {self.percent} Scheduled shutdown with: {self.power}%"""