from unittest import TestCase, main
from car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Brand", "Model", 5, 100)

    def test_correct_init(self):
        self.assertEqual("Brand", self.car.make)
        self.assertEqual("Model", self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_consumption_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_capacity_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_negative_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_more_than_capacity(self):  # also tests refuel itself
        self.car.refuel(1000)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_with_insufficient_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_sufficient_fuel(self):
        self.car.fuel_amount = 50
        self.car.drive(100)
        self.assertEqual(45, self.car.fuel_amount)


if __name__ == "__main__":
    main()