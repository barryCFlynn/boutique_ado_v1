from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51P4gGGP6AxS1ytK4fpGUUOac2OItvM9SSggCfYUa2QAvVwvC4KZkGdMxN4IuMwug5rrt7c0rWvkY6gzp6yhR9heg00flL7t5EC',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)