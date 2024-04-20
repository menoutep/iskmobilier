from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Fieldset, ButtonHolder, Submit
from .models import RentalProperty,SaleProperty
from datetime import datetime
from django.core.validators import validate_email,validate_image_file_extension, RegexValidator
from django import forms
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',  # Modifiez cette regex en fonction de vos besoins
    message="Le numéro de téléphone doit être au format: '+999999999'. Il peut contenir jusqu'à 15 chiffres."
)
username_validator = UnicodeUsernameValidator()



class SalePropertyCreationForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        label="Nom du bien",
        help_text="ex: appartement hausmanien",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le prix du bien'})
        )
    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Entrez une description du bien'}),
        help_text="ex: Bel appartemenet Hausmanien",
        )
    sale_price = forms.CharField(
        max_length=255,
        label="Prix de vente",
        help_text="ex: 300.000.000f",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le prix du bien'})
        )
    area = forms.IntegerField(
        label="Superficie", 
        help_text="ex: 200",   
        widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'taille du bien en m2'})
        )
    number_of_rooms = forms.IntegerField(
        label="Nombre de pièces",    
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'entrez le nombre de pièce dans le bien'})
        )
    

    negotiable = forms.BooleanField(
        label = "Negociable",
        widget=forms.CheckboxInput(),
        required=False
        
    )
    location = forms.CharField(
        max_length=255,
        label="Localisation",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Localisation', 'cols':'60'})
        )
    latitude = forms.FloatField(   
        widget=forms.HiddenInput(),
        required=False,      
    )
    longitude = forms.FloatField(
        widget=forms.HiddenInput(),
        required=False,   
    )
     
    img1 = forms.ImageField(
        label="photo1",
        
        required=False,
        help_text="une photo du bien",
        widget=forms.FileInput(attrs={'class':'form-control','type':'file', 'id':'formFile','placeholder':'Ajoutez une photo du bien'}),
        validators=[validate_image_file_extension]    
    )
    img2 = forms.ImageField(
        label="photo2",
        help_text="une photo du bien",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez une photo du bien'}),
        validators=[validate_image_file_extension]
        )
    img3 = forms.ImageField(
        label="photo3",
        required=False,
        help_text="photo3",
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez une photo du bien'}),
        validators=[validate_image_file_extension]
    )
    img4 = forms.ImageField(
        label="photo4",
        required=False,
        help_text="photo4",
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez une photo du bien'}),
        validators=[validate_image_file_extension]
        )
    img5 = forms.ImageField(
        label="photo5",
        required=False,
        help_text="une photo du bien",
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez Ajoutez une photo du bien'}),
        validators=[validate_image_file_extension]
        )
    img6 = forms.ImageField(
        label="photo6",
        required=False,
        help_text="une photo du bien",
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez Ajoutez une photo du bien'}),
        
    )
    def __init__(self, *args, **kwargs):
        super(SalePropertyCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-3 col-form-label'
        self.helper.field_class = 'col-sm-8'
        self.helper.layout = Layout(
            Fieldset('Informations sur le bien',
                Div(
                    Div('title', css_class='col-md-6'),
                    Div('description', css_class='col-md-6'),
                    css_class='row'
                ),
        
                Div(
                    Div('area', css_class='col-md-6'),
                    Div('number_of_rooms', css_class='col-md-6'),
                    css_class='row'
                ),
                Div(
                    Div('sale_price', css_class='col-md-6'),
                    Div('negotiable', css_class='col-md-6'),
                    css_class='row'
                ),
            Div(
                Div('location', css_class='col-md-6'),
                Div('latitude', css_class='col-md-6', style="display: none;"),
                Div('longitude', css_class='col-md-6', style="display: none;"),
                css_class='row'
            ),         
          
            ),
            Fieldset('Images du bien',
                Div(
                    Div('img1', css_class='col-md-6'),
                    Div('img2', css_class='col-md-6'),
                    css_class='row'
                ),
                Div(
                    Div('img3', css_class='col-md-6'),
                    Div('img4', css_class='col-md-6'),
                    css_class='row'
                ),
                Div(
                    Div('img5', css_class='col-md-6'),
                    Div('img6', css_class='col-md-6'),
                    css_class='row'
                ),
            ),
            ButtonHolder(
                Submit('submit', 'Enregistrer', css_class='btn btn-primary')
            )
        )

    
class RentalPropertyCreationForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        label="Nom du bien",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du bien'})
        )
    description = forms.CharField(
        label="description",
        widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Entrez la description du bien'})
        )
    rental_price = forms.IntegerField(
        label="Loyer",    
        widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Entrez le prix du bien'})
        )
    rental_period = forms.CharField(
        max_length=255,
        label="Période",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Periode de location'})
        )
    
    security_deposit = forms.IntegerField(
        label="caution",    
        widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'caution'})
        )
    area = forms.IntegerField(
        label="aire",    
        widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'taille du bien en m2'})
        )
    number_of_rooms = forms.IntegerField(
        label="Nombre de pièces",    
        widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'entrez le nombre de pièce dans le bien'})
        )
    negotiable = forms.BooleanField(
        label = "Negociable",
        widget=forms.CheckboxInput(),
        required=False 
    )
    location = forms.CharField(
        max_length=255,
        label="Localisation",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Localisation', 'cols':'60'})
        )
    latitude = forms.FloatField(   
        widget=forms.HiddenInput(),
        required=False,      
    )
    longitude = forms.FloatField(
        widget=forms.HiddenInput(),
        required=False,   
    )
   
    img1 = forms.ImageField(
        label="photo1",
        
        required=False,
        help_text="une photo du bien",
        widget=forms.FileInput(attrs={'class':'form-control','type':'file', 'id':'formFile','placeholder':'Ajoutez une photo du bien'}),
        validators=[validate_image_file_extension]    
    )
    img2 = forms.ImageField(
        label="photo2",
        help_text="une photo du bien",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez une photo du bien'}),
        validators=[validate_image_file_extension]
        )
    img3 = forms.ImageField(
        label="photo3",
        required=False,
        help_text="photo3",
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez une photo du bien'}),
        validators=[validate_image_file_extension]
    )
    img4 = forms.ImageField(
        label="photo4",
        required=False,
        help_text="photo4",
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez une photo du bien'}),
        validators=[validate_image_file_extension]
        )
    img5 = forms.ImageField(
        label="photo5",
        required=False,
        help_text="une photo du bien",
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez Ajoutez une photo du bien'}),
        validators=[validate_image_file_extension]
        )
    img6 = forms.ImageField(
        label="photo6",
        required=False,
        help_text="une photo du bien",
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez Ajoutez une photo du bien'}),
        validators=[validate_image_file_extension] 
    )
    def __init__(self, *args, **kwargs):
        super(RentalPropertyCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
            Fieldset('Informations sur le bien',
                Div(
                    Div('title', css_class='col-md-6'),
                    Div('location', css_class='col-md-6'),
                    css_class='row'
                ),
        
                Div(
                    Div('area', css_class='col-md-6'),
                    Div('number_of_rooms', css_class='col-md-6'),
                    css_class='row'
                ),
                Div(
                    Div('rental_price', css_class='col-md-6'),
                    Div('rental_period', css_class='col-md-6'),
                    css_class='row'
                ),
        
                Div(
                    Div('security_deposit', css_class='col-md-6'),
                    Div('negotiable', css_class='col-md-6'),
                    css_class='row'
                ),
                Div(
                    
                    Div('description', css_class='col-md-12 '),
                    
                    css_class='row'
                ),
            ),
            Div(
                
                Div('latitude', css_class='col-md-6', style="display: none;"),
                Div('longitude', css_class='col-md-6', style="display: none;"),
                css_class='row'
            ),
            Fieldset('Images du bien',
                Div(
                    Div('img1', css_class='col-md-6'),
                    Div('img2', css_class='col-md-6'),
                    css_class='row'
                ),
                Div(
                    Div('img3', css_class='col-md-6'),
                    Div('img4', css_class='col-md-6'),
                    css_class='row'
                ),
                Div(
                    Div('img5', css_class='col-md-6'),
                    Div('img6', css_class='col-md-6'),
                    css_class='row'
                ),
            ),
            ButtonHolder(
                Submit('submit', 'Enregistrer', css_class='btn btn-primary')
            )
        )

    