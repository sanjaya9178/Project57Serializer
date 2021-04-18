from rest_framework import serializers
from django import forms
class studentserializer(serializers.Serializer):
    name = serializers.CharField(max_length=70)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=20)

class studentform(forms.Form):
    name = forms.CharField(max_length=70)
    roll = forms.IntegerField()
    city = forms.CharField(max_length=20)
