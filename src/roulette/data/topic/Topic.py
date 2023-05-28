
class Topic:
    """Topic class"""
    def __init__(self, name, percentage, min_time):
        self.__name = name
        self.__percentage = percentage
        self.__min_time = min_time

    @property
    def name(self):
        return self.__name

    @property
    def percentage(self):
        return self.__percentage

    @property
    def min_time(self):
        return self.__min_time
