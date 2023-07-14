import uuid

from yookassa import Configuration, Payment

Configuration.account_id = "229601"
Configuration.secret_key = "live_obQlkUFGrvR3VPJqIbM9iq8EVUa-dHxgxI6u99yoUwo"

def getPaymentConfirmation ():
    Payment.create({
    "amount": {
        "value": "4990.00",
        "currency": "RUB"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": reverse_lazy('succesfully-enroled')
    },
    "capture": True,
    "description": "Оплата курса"
    }, uuid.uuid4())
    
    return Payment

def checkPaymentStatus (payment_id):
    return Payment.find_one(payment_id)

def paymentCapture (payment_id):
    return Payment.capture(payment_id)

