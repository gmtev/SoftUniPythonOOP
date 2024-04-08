from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    def setUp(self):
        self.robot = ClimbingRobot('Mountain', 'Type1', 100, 1000)

    def test_correct_init(self):
        self.assertEqual('Mountain', self.robot.category)
        self.assertEqual('Type1', self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(1000, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)
        self.assertEqual(['Mountain', 'Alpine', 'Indoor', 'Bouldering'], self.robot.ALLOWED_CATEGORIES)

    def test_category_setter_fail(self):
        with self.assertRaises(Exception) as ex:
            self.robot.category = 'Invalid_Category'
        self.assertEqual(f"Category should be one of {self.robot.ALLOWED_CATEGORIES}", str(ex.exception))

    def test_get_used_capacity(self):
        result = self.robot.get_used_capacity()
        self.assertEqual(0, result)
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        self.robot.install_software(software)
        result = self.robot.get_used_capacity()
        self.assertEqual(30, result)

    def test_get_available_capacity(self):
        result = self.robot.get_available_capacity()
        self.assertEqual(100, result)
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        self.robot.install_software(software)
        result = self.robot.get_available_capacity()
        self.assertEqual(70, result)

    def test_get_available_memory(self):
        result = self.robot.get_available_memory()
        self.assertEqual(1000, result)
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        self.robot.install_software(software)
        result = self.robot.get_available_memory()
        self.assertEqual(950, result)

    def test_get_used_memory(self):
        result = self.robot.get_used_memory()
        self.assertEqual(0, result)
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        self.robot.install_software(software)
        result = self.robot.get_used_memory()
        self.assertEqual(50, result)

    def test_install_software_successful(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        result = self.robot.install_software(software)
        expected = f"Software '{'Software1'}' successfully installed on {self.robot.category} part."
        self.assertEqual(expected, result)
        self.assertEqual(self.robot.installed_software, [software])

    def test_install_software_successful_equal(self):
        software = {'name': 'Software1', 'capacity_consumption': 100, 'memory_consumption': 1000}
        result = self.robot.install_software(software)
        expected = f"Software '{'Software1'}' successfully installed on {self.robot.category} part."
        self.assertEqual(expected, result)
        self.assertEqual(self.robot.installed_software, [software])

    def test_install_software_unsuccessful_both(self):
        result = self.robot.install_software({'name': 'Software1', 'capacity_consumption': 300, 'memory_consumption': 5000})
        expected = f"Software '{'Software1'}' cannot be installed on {self.robot.category} part."
        self.assertEqual(expected, result)
        self.assertEqual(self.robot.installed_software, [])

    def test_install_software_unsuccessful_cap(self):
        result = self.robot.install_software({'name': 'Software1', 'capacity_consumption': 300, 'memory_consumption': 50})
        expected = f"Software '{'Software1'}' cannot be installed on {self.robot.category} part."
        self.assertEqual(expected, result)
        self.assertEqual(self.robot.installed_software, [])

    def test_install_software_unsuccessful_mem(self):
        result = self.robot.install_software({'name': 'Software1', 'capacity_consumption': 10, 'memory_consumption': 5000})
        expected = f"Software '{'Software1'}' cannot be installed on {self.robot.category} part."
        self.assertEqual(expected, result)
        self.assertEqual(self.robot.installed_software, [])


if __name__ == '__main__':
    main()