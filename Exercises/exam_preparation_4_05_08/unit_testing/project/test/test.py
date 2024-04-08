from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("model", "family", 20000, 4000)

    def test_correct_init(self):
        self.assertEqual(self.car.model, "model")
        self.assertEqual(self.car.car_type, "family")
        self.assertEqual(self.car.mileage, 20000)
        self.assertEqual(self.car.price, 4000)
        self.assertEqual(self.car.repairs, [])

    def test_price_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.car.price = 1
        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.car.price = 0.5
        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))

    def test_mileage_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 100
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 10
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ex.exception))

    def test_promotional_price_error(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(4000)
        self.assertEqual('You are supposed to decrease the price!', str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(4500)
        self.assertEqual('You are supposed to decrease the price!', str(ex.exception))

    def test_promotional_price(self):
        result = self.car.set_promotional_price(3500)
        self.assertEqual('The promotional price has been successfully set.', result)
        self.assertEqual(self.car.price, 3500)

    def test_need_repair_error(self):
        result = self.car.need_repair(7000, "won't do")
        self.assertEqual(result, 'Repair is impossible!')
        self.assertEqual(self.car.price, 4000)
        self.assertEqual(self.car.repairs, [])

    def test_need_repairs(self):
        result = self.car.need_repair(1000, "test")
        self.assertEqual(result, 'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, 5000)
        self.assertIn('test', self.car.repairs)

    def test_get_error(self):
        car2 = SecondHandCar("model", "sports", 20000, 4000)
        result = self.car.__gt__(car2)
        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

    def test_get_true(self):
        car2 = SecondHandCar("model", "family", 20000, 3000)
        result = self.car.__gt__(car2)
        self.assertTrue(result)

    def test_get_false(self):
        car2 = SecondHandCar("model", "family", 20000, 5000)
        result = self.car.__gt__(car2)
        self.assertFalse(result)

    def test_str(self):
        expected = f"""Model model | Type family | Milage 20000km
Current price: 4000.00 | Number of Repairs: 0"""
        result = self.car.__str__()
        self.assertEqual(expected, result)

    def test_str_with_repairs(self):
        self.car.need_repair(1000, "test")
        expected = f"""Model model | Type family | Milage 20000km
Current price: 5000.00 | Number of Repairs: 1"""
        result = self.car.__str__()
        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()
