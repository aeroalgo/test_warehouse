from django.forms import ModelForm

from app.accounting.models import Storage


class StorageForm(ModelForm):
    class Meta:
        model = Storage
        fields = ['count', 'sku']
