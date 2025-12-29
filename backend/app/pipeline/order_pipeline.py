from chain.processors import ValidationProcessor, PaymentProcessor, ShippingProcessor

class OrderPipeline:
    def __init__(self):
        self.validator = ValidationProcessor()
        self.payment = PaymentProcessor()
        self.shipping = ShippingProcessor()
        # link stages
        self.validator.set_next(self.payment).set_next(self.shipping)

    def process(self, order):
        self.validator.process(order)

