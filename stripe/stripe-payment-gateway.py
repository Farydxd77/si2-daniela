import os
import dotenv
import stripe


#Configuracion del entorno

dotenv.load_dotenv()

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")

stripe.api_key = STRIPE_SECRET_KEY

# Crear metodo de pago

def create_payment_method():

    payment_method = stripe.PaymentMethod.create(
        type="card",
        payment_method="pm_card_visa"
    )

    print(payment_method)
