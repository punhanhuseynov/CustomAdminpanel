from django import forms
from django.core.validators import RegexValidator
from .models import Users
import random
class Userform(forms.ModelForm):
    class Meta:
        model=Users
        fields="__all__"
       
        
        widgets={
            "username":forms.TextInput(attrs={'class':'form-control'}),
            "name":forms.TextInput(attrs={'class':'form-control'}),
            "surname":forms.TextInput(attrs={'class':'form-control'}),
            "password":forms.PasswordInput(attrs={'class':'form-control'}),
            "number":forms.TextInput(attrs={'class':'form-control','placeholder':'+944'}),
            'img':forms.FileInput(attrs={'class':'form-control'}),
            "email":forms.EmailInput(attrs={'class':'form-control'}),
            "is_active":forms.CheckboxInput(attrs={'class':'form-control'})
        }

    def clean(self):
        cleaned_data=super().clean()
        image=cleaned_data.get('img')
        if image:
            filename=image.name.split('.')[1]
            image.name=self.cleaned_data.get('number')+str(random.randint(10,100))+'.'+filename
        print('working')
        return cleaned_data    
        
                
            
      
        
        
        
        
        