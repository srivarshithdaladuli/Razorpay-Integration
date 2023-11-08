from django.shortcuts import render
import razorpay
from decouple import config

def home(request):
    return render(request, 'home.html')

def create_order(request):
    razorpay_api_key = config('RAZORPAY_API_KEY')
    razorpay_secret_key = config('RAZORPAY_SECRET_KEY')

    client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    # Create an order
    response = client.order.create({
        'amount': 50000,  # Amount in paise (change as per your requirement)
        'currency': 'INR',
        'payment_capture': 1  # Auto capture payment
    })

    order_id = response['id']
    context = {
        'order_id': order_id,
        'razorpay_api_key': razorpay_api_key  # Use this key in the frontend to create the payment form
    }

    return render(request, 'payment/payment.html', context)
