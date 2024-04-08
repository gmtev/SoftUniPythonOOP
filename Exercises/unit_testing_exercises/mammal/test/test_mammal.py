from unittest import TestCase, main
from mammal.project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.m = Mammal("Name", "Type", "some_sound")

    def test_correct_init(self):
        self.assertEqual("Name", self.m.name)
        self.assertEqual("Type", self.m.type)
        self.assertEqual("some_sound", self.m.sound)
        self.assertEqual("animals", self.m.get_kingdom())  # also tests get_kingdom

    def test_make_sound(self):
        self.assertEqual("Name makes some_sound", self.m.make_sound())

    def test_get_info(self):
        self.assertEqual("Name is of type Type", self.m.info())


if __name__ == "__main__":
    main()