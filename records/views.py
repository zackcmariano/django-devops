from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from records.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':

        messages.success(request, 'Novo vídeo cadastrado com sucesso!')
        return HttpResponseRedirect('/register/')

    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'records/subscription_form.html', context)