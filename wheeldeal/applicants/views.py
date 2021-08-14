from django.shortcuts import render, redirect

from wheeldeal.applicants.forms import ApplyForm


def apply(request):
    if request.method == "POST":
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.user = request.user
            applicant.save()
            return redirect('index')
    else:
        form = ApplyForm()

    context = {
        'form': form,
    }

    return render(request, 'applicants/apply.html', context)
