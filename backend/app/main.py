from model.order import Order
from chain.processors import ValidationProcessor, PaymentProcessor, ShippingProcessor
from pipeline.order_pipeline import OrderPipeline


if __name__ == "__main__":
    pipeline = OrderPipeline()

    orders = [
        Order(1, 100),
        Order(2, 0),    # invalid
        Order(3, 250)
    ]

    for order in orders:
        pipeline.process(order)
        print(order)
        print("-" * 30)
