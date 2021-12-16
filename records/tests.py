from django.test import TestCase
from records.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/register/')

    def test_get(self):
        """Get /register/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use records/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'records/subscription_form.html')
    
    def test_html(self):
        """Html must contain input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 2)
        self.assertContains(self.response, 'type="url"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form must have 4 fields."""
        form = self.response.context['form']
        self.assertSequenceEqual(['title', 'url_video', 'texto'], list(form.fields))


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(title='Homem-Aranha - Sem Volta Para Casa | Trailer 2', url_video='https://www.youtube.com/watch?v=ae6w0-kZ3-M', 
                    texto='Somos o melhor destino para quem busca trailers assim que eles são lançados.' )
        self.response =  self.client.post('/register/', data)

    def test_post(self):
        """Valid POST should redirect to /register/"""
        self.assertEqual(302, self.response.status_code)


class SubscribeSucessMessage(TestCase):
    def test_message(self):
        data = dict(title='Homem-Aranha - Sem Volta Para Casa | Trailer 2', url_video='https://www.youtube.com/watch?v=ae6w0-kZ3-M', 
                    texto='Somos o melhor destino para quem busca trailers assim que eles são lançados.' )

        response = self.client.post('/register/', data, follow=True)
        self.assertContains(response, 'Novo vídeo cadastrado com sucesso!')  