class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount
        self.status = "NEW"

    def __str__(self):
        return f"Order(id={self.order_id}, amount={self.amount}, status={self.status})"
