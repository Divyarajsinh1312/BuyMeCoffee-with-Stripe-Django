from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import stripe

# Create your views here.

stripe.api_key = ""

stripe.PaymentIntent.create(
  amount=100,
  currency="inr",
)

def index(request):
	return render(request, 'pay/index.html')


def charge(request):
	amount = 5
	if request.method == 'POST':
		print('Data:', request.POST)

	return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'pay/success.html', {'amount':amount})