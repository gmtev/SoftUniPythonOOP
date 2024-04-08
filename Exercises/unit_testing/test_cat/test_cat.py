from cat import Cat
from unittest import TestCase, main


class TestCat(TestCase):

    def setUp(self):
        self.cat = Cat("TestCat")

    def test_correct_init(self):
        self.assertEqual("TestCat", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_feeding_cat_when_hungry(self):
        expected_size = self.cat.size + 1
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_feeding_cat_when_not_hungry(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleeping_when_sleepy(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

    def test_sleeping_when_not_sleepy_because_of_hunger(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == "__main__":
    main()