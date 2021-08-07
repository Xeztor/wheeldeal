from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from wheeldeal.profiles.forms import DeliveryManProfileForm, ClientProfileForm
from wheeldeal.profiles.models import UserProfile


@login_required
def profile_details(request):
    profile = UserProfile.objects.get(pk=request.user.id)
    if not profile.is_complete:
        return redirect('profile edit')
    context = {
        'profile': profile,
    }

    return render(request, 'profiles/details.html', context)


@login_required
def profile_edit(request):
    profile = UserProfile.objects.get(pk=request.user.id)
    form_type = ClientProfileForm
    if profile.is_deliveryman:
        form_type = DeliveryManProfileForm

    if request.method == "POST":
        form = form_type(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = form_type(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/edit.html', context)
