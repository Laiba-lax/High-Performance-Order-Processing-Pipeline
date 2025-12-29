from abc import ABC, abstractmethod

class OrderProcessor(ABC):
    def __init__(self):
        self._next = None

    def set_next(self, processor):
        self._next = processor
        return processor

    @abstractmethod
    def process(self, order):
        if self._next:
            self._next.process(order)


class ValidationProcessor(OrderProcessor):
    def process(self, order):
        print(f"Validating order {order.order_id}")
        if order.amount > 0:
            order.status = "VALIDATED"
            if self._next:
                self._next.process(order)
        else:
            order.status = "INVALID"
            print("Validation failed")


class PaymentProcessor(OrderProcessor):
    def process(self, order):
        print(f"Processing payment for order {order.order_id}")
        order.status = "PAID"
        if self._next:
            self._next.process(order)


class ShippingProcessor(OrderProcessor):
    def process(self, order):
        print(f"Shipping order {order.order_id}")
        order.status = "SHIPPED"
