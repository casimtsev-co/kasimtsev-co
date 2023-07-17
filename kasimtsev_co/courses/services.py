import uuid
from django.urls import reverse

from yookassa import Configuration, Payment

Configuration.account_id = "231010"
Configuration.secret_key = "test_6g72Fr7NBy2dOpRoAzF7pklsI7PxjmWl8r5SJx0rxSk"

def getPaymentConfirmation ():
    payment = Payment.create({
    "amount": {
        "value": "4990.00",
        "currency": "RUB"
    },
    "confirmation": {
        "type": "embedded"
    },
    "capture": True,
    "description": "Оплата курса"
    }, uuid.uuid4())
    
    return payment

def checkPaymentStatus (payment_id):
    return Payment.find_one(payment_id).status

def paymentCapture (payment_id):
    return Payment.capture(payment_id)

def enroleUser (user):
    with open ("allowed-users.json") as file:
        students = file.read().strip().split('\n')
        if str(user.id) in students: return
    with open ("allowed-users.json", "a") as file:
        file.write (f"{user.id}\n")
 

