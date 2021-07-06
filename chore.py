class Chore:
    def __init__(self, name: str, frequency: int, description: str):
        self.name = name
        self.frequency = frequency
        self.description = description

    def __format__(self, format_spec):
        if format_spec[-1] != 's':
            raise ValueError(
                '{} format specifier not understood for this object',
                format_spec[:-1])

        raw = "{} ({})".format(self.name, self.frequency)
        return "{r:{f}}".format(r=raw, f=format_spec)

    def get_name(self):
        return self.name

    def get_frequency(self):
        return self.frequency

    def get_description(self):
        return self.description

    def get_weight(self):
        return 1 / float(self.frequency)
