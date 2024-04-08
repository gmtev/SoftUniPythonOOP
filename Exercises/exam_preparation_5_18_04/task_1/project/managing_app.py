from project.user import User
from project.route import Route
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_TYPES = {"CargoVan": CargoVan, "PassengerCar": PassengerCar}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        u = self._find_user_by_license_number(driving_license_number)
        if u is None:
            new_user = User(first_name, last_name, driving_license_number)
            self.users.append(new_user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"
        return f"{driving_license_number} has already been registered to our platform."

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."
        v = self._find_vehicle_by_license_number(license_plate_number)
        if v is None:
            vehicle = self.VALID_TYPES[vehicle_type](brand, model, license_plate_number)
            self.vehicles.append(vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."
        return f"{license_plate_number} belongs to another vehicle."

    def allow_route(self, start_point: str, end_point: str, length: float):
        filtered_route = self._find_route_by_start_point_and_end_point(start_point, end_point)
        if filtered_route is not None:
            if filtered_route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if filtered_route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if filtered_route.length > length:
                filtered_route.is_locked = True
        idx = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, route_id=idx)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = self._find_user_by_license_number(driving_license_number)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        vehicle = self._find_vehicle_by_license_number(license_plate_number)
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        route = self._find_route_by_id(route_id)
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count):
        count_repaired = 0
        broken_vehicles = [v for v in self.vehicles if v.is_damaged]
        sorted_vehicles = sorted(broken_vehicles, key=lambda x: (x.brand, x.model))
        for vehicle in sorted_vehicles:
            if count == 0:
                break
            vehicle.recharge()
            vehicle.change_status()
            count_repaired += 1
        return f"{count_repaired} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda u: -u.rating)
        result = "*** E-Drive-Rent ***\n"
        result += '\n'.join(user.__str__() for user in sorted_users)
        return result

    def _find_user_by_license_number(self, driving_license_number):
        collection = [c for c in self.users if c.driving_license_number == driving_license_number]
        return collection[0] if collection else None

    def _find_vehicle_by_license_number(self, license_plate_number):
        collection = [c for c in self.vehicles if c.license_plate_number == license_plate_number]
        return collection[0] if collection else None

    def _find_route_by_id(self, route_id):
        collection = [r for r in self.routes if r.route_id == route_id]
        return collection[0] if collection else None

    def _find_route_by_start_point_and_end_point(self, start_point: str, end_point: str):
        filtered_routes = [route for route in self.routes if
                           route.start_point == start_point and route.end_point == end_point]
        if filtered_routes:
            return filtered_routes[0]
        return None
