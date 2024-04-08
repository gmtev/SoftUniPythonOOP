from unittest import TestCase, main
from vehicle.project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(100.0, 90.0)

    def test_correct_init(self):
        self.assertEqual(self.vehicle.fuel, 100.0)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.horse_power, 90.0)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_without_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(5000)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 87.5)

    def test_refuel_with_more_than_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(5000)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_within_capacity_limit(self):
        self.vehicle.fuel = 50
        self.vehicle.refuel(25)
        self.assertEqual(self.vehicle.fuel, 75)

    def test_str(self):
        self.assertEqual("The vehicle has 90.0 horse power with 100.0 fuel left and 1.25 fuel consumption", str(self.vehicle))


if __name__ == "__main__":
    main()