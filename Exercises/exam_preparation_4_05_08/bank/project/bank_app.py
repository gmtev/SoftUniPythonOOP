from project.clients.student import Student
from project.clients.adult import Adult
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan


class BankApp:
    LOAN_TYPES = {"MortgageLoan": MortgageLoan, "StudentLoan": StudentLoan}
    CLIENT_TYPES = {"Adult": Adult, "Student": Student}
    GRANTED = 0
    TOTAL_GRANTED = 0

    def __init__(self, capacity):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")
        l = self.LOAN_TYPES[loan_type]()
        self.loans.append(l)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise Exception("Invalid client type!")
        if self.capacity <= 0:
            return "Not enough bank capacity."

        self.capacity -= 1
        c = self.CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(c)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        c = self._find_client_by_clientid(client_id)
        if (loan_type == "StudentLoan" and c.TYPE == "Student") or (loan_type == "MortgageLoan" and c.TYPE == "Adult"):
            loan = self._find_loans_by_loan_type(loan_type)
            self.loans.remove(loan)
            c.loans.append(loan)
            self.GRANTED += 1
            self.TOTAL_GRANTED += loan.amount
            return f"Successfully granted {loan_type} to {c.name} with ID {client_id}."
        raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):
        c = self._find_client_by_clientid(client_id)
        if c is None:
            raise Exception("No such client!")
        if len(c.loans) >= 1:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(c)
        self.capacity += 1
        return f"Successfully removed {c.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        filtered_loans = self._find_loans_by_type(loan_type)
        [loan.increase_interest_rate() for loan in filtered_loans]
        return f"Successfully changed {len(filtered_loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        filtered_clients = self._find_clients_by_interest_rate(min_rate)
        [client.increase_clients_interest() for client in filtered_clients]
        return f"Number of clients affected: {len(filtered_clients)}."

    def get_statistics(self):
        if len(self.clients) >= 1:
            interest_total = sum(l.interest for l in self.clients)
            avg_client_interest_rate = interest_total/len(self.clients)
        else:
            avg_client_interest_rate = 0.0
        total_clients_income = sum(c.income for c in self.clients)
        result = f"Active Clients: {len(self.clients)}\nTotal Income: {total_clients_income:.2f}\n"
        result += f"Granted Loans: {self.GRANTED}, Total Sum: {self.TOTAL_GRANTED:.2f}\n"
        result += f"Available Loans: {len(self.loans)}, Total Sum: {sum(l.amount for l in self.loans):.2f}\n"
        result += f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
        return result

    def _find_client_by_clientid(self, client_id):
        collection = [c for c in self.clients if c.client_id == client_id]
        return collection[0] if collection else None

    def _find_loans_by_loan_type(self, loan_type):
        collection = [l for l in self.loans if l.TYPE == loan_type]
        return collection[0] if collection else None

    def _find_loans_by_type(self, loan_type):
        return [loan for loan in self.loans if loan.TYPE == loan_type]

    def _find_clients_by_interest_rate(self, min_rate):
        return [client for client in self.clients if client.interest < min_rate]


