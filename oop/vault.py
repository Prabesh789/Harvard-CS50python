"""operator overloading: giving extended meaning beyond their predefined operational meaning."""


class Vault:

    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        _galleons = self.galleons + other.galleons
        _sickles = self.sickles + other.sickles
        _knuts = self.knuts + other.knuts
        return Vault(_galleons, _sickles, _knuts)


potter = Vault(100, 50, 25)
print(potter)
waesley = Vault(25, 50, 100)
print(waesley)
"""
The goal here is to add potter vault and waesley vault. In python while overloading when it python sees + operator, it 
automaticly calls __add__ method and passes the argument
"""
total = potter + waesley
print(total)
