from project.clients.base_client import BaseClient


class Adult(BaseClient):
    INITIAL_INTEREST = 4.0
    TYPE = "Adult"

    def __init__(self, name, client_id, income):
        super().__init__(name, client_id, income, interest=self.INITIAL_INTEREST)

    def increase_clients_interest(self):
        self.interest += 2.0