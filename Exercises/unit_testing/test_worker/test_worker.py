from unittest import TestCase, main
from worker import Worker


class TestWorker(TestCase):

    def setUp(self):
        self.worker = Worker('TestGuy', 25000, 100)

    def test_correct_init(self):
        self.assertEqual("TestGuy", self.worker.name)
        self.assertEqual(25000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_with_energy_increasing_money_and_reducing_energy(self):
        expected_money = self.worker.salary * 2
        expected_energy = self.worker.energy - 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_work_without_energy_raising_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_rest_increasing_eneergy(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_returning_correct_string(self):
        expected_string = f'TestGuy has saved 0 money.'
        self.assertEqual(expected_string, self.worker.get_info())


if __name__ == "__main__":
    main()
