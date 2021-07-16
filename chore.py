class Chore:
    """
    A chore that someone can do.
    """
    def __init__(self, name: str, frequency: int, description: str):
        """

        :param name: Title of the chore
        :param frequency: Within how many days the chore should be completed
        :param description: Description of the chore such as how to do it
        """
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
        """Returns the title of the chore"""
        return self.name

    def get_frequency(self):
        """Returns the frequency of the chore (in days)"""
        return self.frequency

    def get_description(self):
        """Returns the chore description"""
        return self.description

    def get_weight(self):
        """
        For the chore to be randomly selected, it must be inversely
        weighted against other chores. This method returns the relative
        weight.
        :return: `Float` The weight of the chore
        """
        return 1 / float(self.frequency)
