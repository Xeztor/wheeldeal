from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from wheeldeal.core.utils import get_user_profile
from wheeldeal.orders.forms import CreateOrderForm
from wheeldeal.orders.models import Order
from wheeldeal.orders.order_states import ORDER_STATES
from wheeldeal.profiles.models import UserProfile


@login_required
def add_order(request):
    if request.method == "POST":
        form = CreateOrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('orders list')
    else:
        form = CreateOrderForm()

    context = {
        'form': form,
    }

    return render(request, 'orders/add_order.html', context)


@login_required
def orders_history(request):
    profile = get_user_profile(request.user.id)
    if profile.is_deliveryman:
        orders = Order.objects.filter(delivery_guy_id=request.user.id)
    else:
        orders = Order.objects.filter(client_id=request.user.id)

    context = {
        'orders': orders,
    }

    return render(request, 'orders/orders_history.html', context)


@login_required
def orders_available(request):
    orders = Order.objects \
        .filter(state=ORDER_STATES['0'])

    context = {
        'orders': orders,
    }

    return render(request, 'orders/active_orders.html', context)


@login_required
def order_details(request, pk):
    order = Order.objects.get(pk=pk)
    context = {
        'order': order,
    }

    return render(request, 'orders/order_details.html', context)


@login_required
def take_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.state = ORDER_STATES['1']
    profile = UserProfile.objects.get(pk=request.user.id)
    order.delivery_guy = profile
    order.save()
    return redirect('orders history')


@login_required
def complete_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.state = ORDER_STATES['2']
    order.date_delivered = datetime.now()
    order.save()
    return redirect('orders history')
