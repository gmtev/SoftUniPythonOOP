from unittest import TestCase, main
from project.robot import Robot


class TestRobot(TestCase):
    def setUp(self):
        self.robot = Robot("someid", 'Military', 100, 1000)

    def test_correct_init(self):
        self.assertEqual(self.robot.robot_id, "someid")
        self.assertEqual(self.robot.category, 'Military')
        self.assertEqual(self.robot.price, 1000)
        self.assertEqual(self.robot.available_capacity, 100)
        self.assertEqual(self.robot.ALLOWED_CATEGORIES, ['Military', 'Education', 'Entertainment', 'Humanoids'])
        self.assertEqual(self.robot.PRICE_INCREMENT, 1.5)
        self.assertEqual(self.robot.software_updates, [])
        self.assertEqual(self.robot.hardware_upgrades, [])

    def test_category_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.category = "test"
        self.assertEqual(f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'", str(ex.exception))

    def test_price_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.price = - 1
        self.assertEqual("Price cannot be negative!", str(ex.exception))

    def test_upgrade_fail(self):
        self.robot.hardware_upgrades.append("test")
        result = self.robot.upgrade("test", 20)
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not upgraded.")
        self.assertEqual(self.robot.hardware_upgrades, ["test"])
        self.assertEqual(self.robot.price, 1000)

    def test_upgrade(self):
        result = self.robot.upgrade("test", 20)
        self.assertEqual(result, f'Robot {self.robot.robot_id} was upgraded with test.')
        self.assertEqual(self.robot.hardware_upgrades, ["test"])
        self.assertEqual(self.robot.price, 1030)

    def test_update_fail_1(self):
        self.robot.update(10.0, 90)
        result = self.robot.update(8.0, 30)
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not updated.")
        self.assertEqual(self.robot.software_updates, [10.0])
        self.assertEqual(self.robot.available_capacity, 10)

    def test_update_fail_1_5(self):
        self.robot.update(10.0, 90)
        result = self.robot.update(10.0, 30)
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not updated.")
        self.assertEqual(self.robot.software_updates, [10.0])
        self.assertEqual(self.robot.available_capacity, 10)

    def test_update_fail_2(self):
        result = self.robot.update(8.0, 130)
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not updated.")
        self.assertEqual(self.robot.software_updates, [])
        self.assertEqual(self.robot.available_capacity, 100)

    def test_update_fail_3(self):
        self.robot.update(10.0, 10)
        result = self.robot.update(11.0, 100)
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not updated.")
        self.assertEqual(self.robot.software_updates, [10.0])
        self.assertEqual(self.robot.available_capacity, 90)

    def test_update(self):
        result = self.robot.update(8.0, 30)
        self.assertEqual(result, f'Robot {self.robot.robot_id} was updated to version {8.0}.')
        self.assertEqual(self.robot.software_updates, [8.0])
        self.assertEqual(self.robot.available_capacity, 70)

    def test_update_2(self):
        self.robot.update(10.0, 10)
        result = self.robot.update(11.0, 30)
        self.assertEqual(result, f'Robot {self.robot.robot_id} was updated to version {11.0}.')
        self.assertEqual(self.robot.software_updates, [10.0, 11.0])
        self.assertEqual(self.robot.available_capacity, 60)

    def test_gt_one(self):
        self.other = Robot("someid", 'Military', 100, 2000)
        result = self.robot.__gt__(self.other)
        self.assertEqual(result,
                         f'Robot with ID {self.robot.robot_id} is cheaper than Robot with ID {self.other.robot_id}.')

    def test_gt_two(self):
        self.other = Robot("someid", 'Military', 100, 100)
        result = self.robot.__gt__(self.other)
        self.assertEqual(result,
                         f'Robot with ID {self.robot.robot_id} is more expensive than Robot with ID {self.other.robot_id}.')

    def test_gt_three(self):
        self.other = Robot("someid", 'Military', 100, 1000)
        result = self.robot.__gt__(self.other)
        self.assertEqual(result, f'Robot with ID {self.robot.robot_id} costs equal to Robot with ID {self.other.robot_id}.')


if __name__ == "__main__":
    main()
