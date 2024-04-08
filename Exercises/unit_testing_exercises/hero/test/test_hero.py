from unittest import TestCase, main
from hero.project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Test1", 10, 100.0, 20.0)
        self.enemy = Hero("Test2", 10, 100.0, 20.0)

    def test_correct_init(self):
        self.assertEqual("Test1", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(20.0, self.hero.damage)

    def test_battle_against_oneself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_insufficient_health(self):
        self.hero.health = -5
        with self.assertRaises(Exception) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_insufficient_health(self):
        self.enemy.health = -5
        with self.assertRaises(Exception) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Test2. He needs to rest", str(ve.exception))

    def test_battle_draw(self):
        self.assertEqual("Draw", self.hero.battle(self.enemy))

    def test_battle_defeat(self):
        self.enemy.health = 300.0
        self.assertEqual("You lose", self.hero.battle(self.enemy))
        self.assertEqual(11, self.enemy.level)
        self.assertEqual(105, self.enemy.health)
        self.assertEqual(25, self.enemy.damage)

    def test_battle_victory(self):
        self.hero.health = 300.0
        self.assertEqual("You win", self.hero.battle(self.enemy))
        self.assertEqual(11, self.hero.level)
        self.assertEqual(105, self.hero.health)
        self.assertEqual(25, self.hero.damage)

    def test_str_method(self):
        self.assertEqual(f"Hero Test1: 10 lvl\nHealth: 100.0\nDamage: 20.0\n", str(self.hero))


if __name__ == "__main__":
    main()