from django.forms import ModelForm
from .models import addasset,ProjectDetail,AddProjectDocument
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class addassetForm(ModelForm):
    class Meta:
        model = addasset
        fields = ['Assettype','Assetsequence','Assetname','Assetnumber','DateofPurchase','AssestWarrentyUpto']

class addProjectDetailform(ModelForm):
    class Meta:
        model = ProjectDetail
        fields = ['ProjectNumber','ProjectName','ProjectContact','ProjectAddress']

class AddProjectDocumentForm(ModelForm):
    class Meta:
        model = AddProjectDocument
        fields = ['DocumentType','DocumentSequence','DocumentNumber','DocumentName','Attachment']


