# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User,SearchHistoryModel,HandleModel, SaveItemModel, LikeItemModel
from django.forms import MultiWidget, TextInput
from django.forms import CheckboxInput, HiddenInput
import datetime

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email',) # new

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',) # new
#--------------------------------------------
class HomeForm(forms.ModelForm):
    searchtext=forms.CharField(max_length=150,required=True,
    widget=forms.TextInput( attrs={'class':'form-control',
                                   'placeholder':'What are you looking for?'}))

    contributor_author=forms.CharField(max_length=150,required=False,
    widget=forms.TextInput( attrs={'class':'form-control',
                                   'placeholder':'name?'}))

    contributor_department=forms.CharField(max_length=150,required=False,
    widget=forms.TextInput( attrs={'class':'form-control',
                                   'placeholder':'Department name?'}))


    contributor_committeechair=forms.CharField(max_length=150,required=False,
    widget=forms.TextInput( attrs={'class':'form-control',
                                   'placeholder':'Name?'}))

    description_degree=forms.CharField(max_length=150,required=False,
    widget=forms.TextInput( attrs={'class':'form-control',
                                   'placeholder':'PhD,...'}))

    YEARS= [x for x in range(1940,2021)]
    date1= forms.DateField(label='', widget=forms.SelectDateWidget(years=YEARS))
    date2= forms.DateField(label='', widget=forms.SelectDateWidget(years=YEARS),initial=datetime.date.today)

    class Meta:
        model=SearchHistoryModel
        fields=('searchtext','contributor_author','contributor_department',
        'contributor_committeechair','description_degree',)

#-------------------------For uploading files-------------------------------------------------
class UploadForm(forms.ModelForm):

    title=forms.CharField(max_length=500,required=True,
    widget=forms.TextInput( attrs={'class':'form-control',
                                   'placeholder':'Enter your title'})
    )

    contributor_author=forms.CharField(max_length=500,required=True,
    widget=forms.TextInput( attrs={'class':'form-control',
                                   'placeholder':'Name'})
    )

    description_abstract=forms.CharField(max_length=5000,required=True,
    widget=forms.TextInput( attrs={'class':'form-control',
                                   'placeholder':'Abstract'})
    )

    contributor_committeechair=forms.CharField(max_length=500,required=True,
    widget=forms.TextInput( attrs={'class':'form-control',
                                   'placeholder':'Names'})
    )

    contributor_committeemember=forms.CharField(max_length=500,required=True,
    widget=forms.TextInput( attrs={'class':'form-control',
                                   'placeholder':'Enter namesin quotes (Eg:" Jian Wu" "Ravi Mukkamala" "Michele C. Weigle")'})
    )

    contributor_department=forms.CharField(max_length=500,required=True,
    widget=forms.TextInput( attrs={'class':'form-control',
                                   'placeholder':'Department'})
    )

    YEARS= [x for x in range(1940,2021)]
    date_issued=forms.DateField(label='', widget=forms.SelectDateWidget(years=YEARS),initial=datetime.date.today)

    subject=forms.CharField(max_length=500,required=True,
    widget=forms.TextInput( attrs={'class':'form-control',
                                   'placeholder':'Enter keywords in quotes (Eg: "VSC","SMES","Multi-Level",)'}))

    identifier_sourceurl=forms.CharField(max_length=500,required=True,
    widget=forms.TextInput( attrs={'class':'form-control',
                                   'placeholder':'url'})
    )

    file=forms.FileField(required=True)

    handle=forms.CharField(max_length=500,required=False,widget=forms.HiddenInput())
    class Meta:
        model=HandleModel
        fields=('handle',)

#-----------------------------------------------------------------------
class SaveItemForm(forms.ModelForm):
    class Meta:
        model=SaveItemModel
        fields=('handle',)
#------------------------------------------------------------------------
class LikeItemForm(forms.ModelForm):
    class Meta:
        model=LikeItemModel
        fields=('handle',)