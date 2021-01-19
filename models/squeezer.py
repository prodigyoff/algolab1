class JuiceSqueezer:
    def __init__(self, color, max_amount_of_squeezed_juice_in_litres_per_hour, consumed_power_in_kilowats,
                 producer):
        self.color = color
        self.max_amount_of_squeezed_juice_in_litres_per_hour = int(max_amount_of_squeezed_juice_in_litres_per_hour)
        self.consumed_power_in_kilowats = int(consumed_power_in_kilowats)
        self.producer = producer

    def __repr__(self):
        return f'Color:{self.color}, juice_per_hour:{self.max_amount_of_squeezed_juice_in_litres_per_hour}'\
            f',consumed power:{self.consumed_power_in_kilowats}, producer:{self.producer} \n'
