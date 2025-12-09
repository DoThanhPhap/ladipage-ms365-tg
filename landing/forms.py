"""
Contact form for landing page.
"""
import re
from django import forms


class ContactForm(forms.Form):
    """Contact form with Vietnamese phone validation."""

    SERVICE_CHOICES = [
        ('', 'Chọn dịch vụ quan tâm *'),
        ('m365', 'Microsoft 365'),
        ('office', 'Văn phòng ảo'),
        ('digital', 'Chữ ký số & Hoá đơn'),
        ('all', 'Tất cả dịch vụ'),
    ]

    name = forms.CharField(
        max_length=100,
        required=True,
        error_messages={'required': 'Vui lòng nhập họ tên'},
    )
    phone = forms.CharField(
        max_length=15,
        required=True,
        error_messages={'required': 'Vui lòng nhập số điện thoại'},
    )
    service = forms.ChoiceField(
        choices=SERVICE_CHOICES,
        required=True,
        error_messages={'required': 'Vui lòng chọn dịch vụ'},
    )
    message = forms.CharField(
        required=False,
        widget=forms.Textarea(),
    )

    def clean_phone(self):
        """Validate Vietnamese phone number format."""
        phone = self.cleaned_data.get('phone', '')
        # Remove spaces and dashes
        cleaned = re.sub(r'[\s\-]', '', phone)

        # Vietnamese mobile: 03x, 05x, 07x, 08x, 09x (10 digits)
        # Vietnamese landline: 02x (11 digits)
        mobile_pattern = r'^(0[35789][0-9]{8})$|^(\+84[35789][0-9]{8})$'
        landline_pattern = r'^(02[0-9]{9})$|^(\+842[0-9]{9})$'

        if not (re.match(mobile_pattern, cleaned) or re.match(landline_pattern, cleaned)):
            raise forms.ValidationError('Số điện thoại không hợp lệ')

        return cleaned

    def clean_service(self):
        """Ensure a service is selected."""
        service = self.cleaned_data.get('service', '')
        if not service:
            raise forms.ValidationError('Vui lòng chọn dịch vụ')
        return service
