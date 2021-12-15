from django.shortcuts import render
from records.forms import SubscriptionForm


def subscribe(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'records/subscription_form.html', context)