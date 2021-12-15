from django import forms


class SubscriptionForm(forms.Form):
    title = forms.CharField(label='Título')
    url_video = forms.URLField(label='Url do Vídeo')
    texto = forms.CharField(label='Descrição do Vídeo')