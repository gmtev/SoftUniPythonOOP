from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):
    def setUp(self):
        self.trip = Trip(6000, 3, True)

    def test_correct_init(self):
        self.assertEqual(self.trip.budget, 6000)
        self.assertEqual(self.trip.travelers, 3)
        self.assertEqual(self.trip.is_family, True)
        self.assertEqual(self.trip.booked_destinations_paid_amounts, {})

    def test_travelers_setter(self):
        with self.assertRaises(Exception) as ex:
            self.trip.travelers = 0
        self.assertEqual('At least one traveler is required!', str(ex.exception))

    def test_family_setter(self):
        self.trip_2 = Trip(6000, 1, True)
        self.assertFalse(self.trip_2.is_family)

    def test_book_fail(self):
        result = self.trip.book_a_trip("somewhere")
        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

    def test_book_no_money_with_discount(self):
        self.trip_3 = Trip(6000, 2, True)
        result = self.trip_3.book_a_trip('New Zealand')
        self.assertEqual('Your budget is not enough!', result)

    def test_book_no_money(self):
        result = self.trip.book_a_trip('New Zealand')
        self.assertEqual('Your budget is not enough!', result)

    def test_book(self):
        result = self.trip.book_a_trip("Bulgaria")
        self.assertEqual('Successfully booked destination Bulgaria! Your budget left is 4650.00', result)
        self.assertIn("Bulgaria", self.trip.booked_destinations_paid_amounts)
        self.assertEqual(self.trip.budget, 4650)

    def test_booking_status_none(self):
        result = self.trip.booking_status()
        self.assertEqual('No bookings yet. Budget: 6000.00', result)

    def test_booking_status(self):
        self.trip.book_a_trip("Bulgaria")
        result = self.trip.booking_status()
        expected = f"Booked Destination: Bulgaria\nPaid Amount: 1350.00\nNumber of Travelers: 3\nBudget Left: 4650.00"
        self.assertEqual(expected,result)


if __name__ == "__main__":
    main()

