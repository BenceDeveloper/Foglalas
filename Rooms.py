from abc import ABC, abstractmethod
class Szoba(ABC):
    def __init__(self,Price,Number):
        self._Price = Price
        self._Number = Number
    @property
    def Number(self):
        return self._Number
    @property
    def Price(self):
        return self._Price
class EgyAgyasSzoba(Szoba):
    def __init__(self,Number):
        super().__init__(Price=1000,Number=Number)
class KetAgyasSzoba(Szoba):
    def __init__(self,Number):
        super().__init__(Price=2000,Number=Number)