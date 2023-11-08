class Bill:
    """
    A Class of Bill.
    """

    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmate:

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, co_flatmate):
        weight = self.days_in_house / (co_flatmate.days_in_house + self.days_in_house)
        return round(bill.amount * weight, 2)
