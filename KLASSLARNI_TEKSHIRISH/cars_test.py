import unittest
from cars import Car

class CarTest(unittest.TestCase):
    '''Car class ni metodlarini  tekshirish uchun class'''
    def setUp(self):
        self.make = "BMW"
        self.model = 'BMW x7'
        self.year = 2009
        self.price = 10000
        self.km = 100
        self.car1 = Car(self.make, self.model, self.year)
        self.car2 = Car(self.make, self.model, self.year, self.km)
        self.car3 = Car(self.make, self.model, self.year, self.km, self.price)


    def test_car(self):
        '''Car class ni metodlarini tekshiruvchi metod'''
        self.assertEqual(self.car1.get_km(), 0)
        self.assertEqual(self.car2.get_km(), self.km)
        self.assertEqual(self.car2.get_km(), self.km)
        
        self.car1.set_price(100)
        self.assertEqual(self.car1.price, 100)

        self.car2.set_price(200)
        self.assertEqual(self.car2.price, 200)

        self.car3.set_price(300)
        self.assertEqual(self.car3.price, 300)

        self.car1.add_km(100)
        self.assertEqual(self.car1.get_km(), 100)
        
        try :
            self.car1.add_km(-100)
        
        except ValueError as error :
            self.assertEqual(type(error), ValueError)
        
        try :
            self.car2.add_km(-100)
        
        except ValueError as error :
            self.assertEqual(type(error), ValueError)
        
        try :
            self.car3.add_km(-100)
        
        except ValueError as error :
            self.assertEqual(type(error), ValueError)


        

unittest.main()
