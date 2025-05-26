from app.models.customer import Customer

class CustomerService:
    def __init__(self):
        self.customers_db = {}

    def get_all_customers(self):
        return list(self.customers_db.values())

    def get_customer(self, customer_id: int):
        return self.customers_db.get(customer_id)

    def create_customer(self, customer: Customer):
        if customer.id in self.customers_db:
            raise ValueError("Customer already exists")
        self.customers_db[customer.id] = customer
        return customer

    def update_customer(self, customer_id: int, customer_data: Customer):
        if customer_id not in self.customers_db:
            raise ValueError("Customer not found")
        self.customers_db[customer_id] = customer_data
        return customer_data

    def delete_customer(self, customer_id: int):
        if customer_id not in self.customers_db:
            raise ValueError("Customer not found")
        del self.customers_db[customer_id]
        return {"message": "Customer deleted successfully"}