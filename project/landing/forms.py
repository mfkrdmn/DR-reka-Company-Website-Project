
from django import forms 
from django.forms import ModelForm
from .models import Profile


class profile_edit_tr(ModelForm):
    namesurname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ad Soyad'}),
        label="Ad Soyad")
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '+905050055005'}),
        label="Telefon Numarası")
    mobile_phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '+905050055005'}),
        label="Cep Telefon Numarası")
    web_site = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'rekaglobal.com'}),
        label="Şirket Web Adresi")
    note = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Not ...'}),
        label="Şirket Not Adresi")
    class Meta:
        model = Profile
        fields = [
            'namesurname',
            'phone',
            'mobile_phone',
            'web_site',
            'note','image'
            
        ]

class profile_edit_en(ModelForm):
    namesurname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ad Soyad'}),
        label="Ad Soyad")
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '+905050055005'}),
        label="Telefon Numarası")
    mobile_phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '+905050055005'}),
        label="Cep Telefon Numarası")
    web_site = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'rekaglobal.com'}),
        label="Şirket Web Adresi")
    note = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Not ...'}),
        label="Şirket Not Adresi")
    class Meta:
        model = Profile
        fields = [
            'namesurname',
            'phone',
            'mobile_phone',
            'web_site',
            'note','image'
            
        ]



class profile_edit_de(ModelForm):
    namesurname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ad Soyad'}),
        label="Ad Soyad")
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '+905050055005'}),
        label="Telefon Numarası")
    mobile_phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '+905050055005'}),
        label="Cep Telefon Numarası")
    web_site = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'rekaglobal.com'}),
        label="Şirket Web Adresi")
    note = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Not ...'}),
        label="Şirket Not Adresi")
    class Meta:
        model = Profile
        fields = [
            'namesurname',
            'phone',
            'mobile_phone',
            'web_site',
            'note','image'
            
        ]


class profile_edit_ar(ModelForm):
    namesurname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ad Soyad'}),
        label="Ad Soyad")
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '+905050055005'}),
        label="Telefon Numarası")
    mobile_phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '+905050055005'}),
        label="Cep Telefon Numarası")
    web_site = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'rekaglobal.com'}),
        label="Şirket Web Adresi")
    note = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Not ...'}),
        label="Şirket Not Adresi")
    class Meta:
        model = Profile
        fields = [
            'namesurname',
            'phone',
            'mobile_phone',
            'web_site',
            'note','image'
            
        ]
        