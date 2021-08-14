from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from wheeldeal.core.decorators import only_delivery_guy_allowed
from wheeldeal.core.utils import get_user_profile
from wheeldeal.orders.forms import CreateOrderForm, EditOrderForm
from wheeldeal.orders.models import Order
from wheeldeal.orders.order_states import ORDER_STATES


@login_required
def add_order(request):
    if request.method == "POST":
        form = CreateOrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            profile = get_user_profile(request.user.id)
            order.client = profile
            order.save()
            return redirect('orders history')
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


@only_delivery_guy_allowed
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


@only_delivery_guy_allowed
@login_required
def take_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.state = ORDER_STATES['1']
    profile = get_user_profile(request.user.id)
    order.delivery_guy = profile
    order.save()
    return redirect('orders history')


@only_delivery_guy_allowed
@login_required
def complete_order(request, pk):
    order = Order.objects.get(pk=pk)
    user_profile = get_user_profile(request.user.id)
    if not user_profile == order.delivery_guy:
        return render(request, 'error_codes/401.html')

    order.state = ORDER_STATES['2']
    order.date_delivered = datetime.now()
    order.save()
    return redirect('orders history')


@login_required
def order_edit(request, pk):
    order = Order.objects.get(pk=pk)
    request_user_profile = get_user_profile(request.user.id)
    if not order.client == request_user_profile:
        return render(request, 'error_codes/401.html')

    if request.method == "POST":
        form = EditOrderForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders history')
    else:
        form = EditOrderForm(instance=order)

    context = {
        'form': form,
        'order': order,
    }

    return render(request, 'orders/edit_order.html', context)


@login_required
def order_delete(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return redirect('orders history')
