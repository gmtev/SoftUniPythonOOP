from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.station = RailwayStation("Gara")

    def test_correct_init(self):
        self.assertEqual(self.station.name, "Gara")
        self.assertEqual(self.station.arrival_trains, deque([]))
        self.assertEqual(self.station.departure_trains, deque([]))

    def test_name_setter(self):
        with self.assertRaises(Exception) as ex:
            self.station.name = "A"
        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))
        with self.assertRaises(Exception) as ex:
            self.station.name = "ABC"
        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board("train_info")
        self.assertIn("train_info", self.station.arrival_trains)

    def test_train_has_arrived_fail(self):
        self.station.new_arrival_on_board("train_info")
        result = self.station.train_has_arrived("other_train_info")
        self.assertEqual(result, "There are other trains to arrive before other_train_info.")

    def test_train_has_arrived_fail_second(self):
        self.station.new_arrival_on_board("other_train_info")
        self.station.new_arrival_on_board("train_info")
        result = self.station.train_has_arrived("train_info")
        self.assertEqual(result, "There are other trains to arrive before train_info.")

    def test_train_has_arrived(self):
        self.station.new_arrival_on_board("train_info")
        result = self.station.train_has_arrived("train_info")
        self.assertEqual(result, "train_info is on the platform and will leave in 5 minutes.")
        self.assertNotIn("train_info", self.station.arrival_trains)
        self.assertIn("train_info", self.station.departure_trains)

    def test_train_has_arrived_second(self):
        self.station.new_arrival_on_board("train_info")
        self.station.new_arrival_on_board("other_train_info")
        result = self.station.train_has_arrived("train_info")
        self.assertEqual(result, "train_info is on the platform and will leave in 5 minutes.")
        self.assertNotIn("train_info", self.station.arrival_trains)
        self.assertIn("train_info", self.station.departure_trains)

    def test_train_has_left_true(self):
        self.station.departure_trains.append("train_info")
        result = self.station.train_has_left("train_info")
        self.assertEqual(result, True)
        self.assertNotIn("train_info", self.station.departure_trains)

    def test_train_has_left_false(self):
        result = self.station.train_has_left("train_info")
        self.assertEqual(result, False)

    def test_train_has_left_false_second(self):
        self.station.departure_trains.append("other_train_info")
        result = self.station.train_has_left("train_info")
        self.assertEqual(result, False)


if __name__ == "__main__":
    main()