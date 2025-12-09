"""
Unit tests for landing app.
"""
from django.test import TestCase, Client
from django.urls import reverse
from .forms import ContactForm


class LandingPageTests(TestCase):
    """Tests for landing page views."""

    def setUp(self):
        self.client = Client()

    def test_homepage_loads(self):
        """Homepage returns 200 status."""
        response = self.client.get(reverse('landing:index'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_contains_company_name(self):
        """Homepage contains company name."""
        response = self.client.get(reverse('landing:index'))
        self.assertContains(response, 'Trương Gia')

    def test_homepage_contains_phone(self):
        """Homepage contains contact phone."""
        response = self.client.get(reverse('landing:index'))
        self.assertContains(response, '0989 222 800')

    def test_homepage_contains_sections(self):
        """Homepage contains all required sections."""
        response = self.client.get(reverse('landing:index'))
        self.assertContains(response, 'id="solutions"')
        self.assertContains(response, 'id="benefits"')
        self.assertContains(response, 'id="contact"')

    def test_homepage_contains_products(self):
        """Homepage contains all 3 products."""
        response = self.client.get(reverse('landing:index'))
        self.assertContains(response, 'Microsoft 365')
        self.assertContains(response, 'Văn phòng ảo')
        self.assertContains(response, 'Chữ ký số')


class ContactFormTests(TestCase):
    """Tests for contact form validation."""

    def test_valid_form(self):
        """Form with valid data is valid."""
        form_data = {
            'name': 'Nguyễn Văn A',
            'phone': '0989222800',
            'service': 'm365',
            'message': 'Tôi cần tư vấn',
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_requires_name(self):
        """Form requires name field."""
        form_data = {'phone': '0989222800', 'service': 'm365'}
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_form_requires_phone(self):
        """Form requires phone field."""
        form_data = {'name': 'Test', 'service': 'm365'}
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors)

    def test_form_requires_service(self):
        """Form requires service field."""
        form_data = {'name': 'Test', 'phone': '0989222800'}
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('service', form.errors)

    def test_invalid_phone_rejected(self):
        """Form rejects invalid phone numbers."""
        form_data = {
            'name': 'Test',
            'phone': '123',  # Too short
            'service': 'm365',
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors)

    def test_valid_mobile_phone(self):
        """Form accepts valid Vietnamese mobile numbers."""
        valid_phones = ['0989222800', '0351234567', '0771234567']
        for phone in valid_phones:
            form = ContactForm(data={
                'name': 'Test',
                'phone': phone,
                'service': 'm365',
            })
            self.assertTrue(form.is_valid(), f"Phone {phone} should be valid")

    def test_form_submission_redirect(self):
        """Form submission redirects on success."""
        response = self.client.post(reverse('landing:index'), {
            'name': 'Test User',
            'phone': '0989222800',
            'service': 'm365',
        })
        self.assertEqual(response.status_code, 302)  # Redirect


class StaticFilesTests(TestCase):
    """Tests for static file accessibility."""

    def test_css_accessible(self):
        """CSS file is accessible."""
        response = self.client.get('/static/css/style.css')
        self.assertEqual(response.status_code, 200)

    def test_js_accessible(self):
        """JS file is accessible."""
        response = self.client.get('/static/js/main.js')
        self.assertEqual(response.status_code, 200)
