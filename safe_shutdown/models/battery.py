class Battery:
    def __init__(self, percent: 10, power_off: int, status: bool) -> None:
         self.percent = percent
         self.status = status
         self.power_off = power_off
    
    def __repr__(self) -> str:
        return f"""Battery(percent={self.percent}, power_off={self.power_off}, status={self.status})"""