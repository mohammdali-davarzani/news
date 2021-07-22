from django import  forms
from .models import NewsSources, NewsContents, AuthUser
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from tinymce.widgets import TinyMCE




class AddSource_Form(forms.ModelForm):

    class Meta:

        model = NewsSources
        fields = ("source_name", "source_url", "is_active")


        widgets = {
			'source_name': forms.TextInput(attrs={'class': 'form-control'}),
			'source_url': forms.URLInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class':'form-check-input'})

		}


class UpdateSource_Form(forms.ModelForm):

    class Meta:

        model = NewsSources
        fields = ("source_name", "source_url", "is_active")


        widgets = {
			'source_name': forms.TextInput(attrs={'class': 'form-control'}),
			'source_url': forms.URLInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class':'form-check-input'})

		}


class AddNews_Form(forms.ModelForm):

    class Meta:

        model = NewsContents
        fields = ("news_source", "news_url", "news_date_time", "news_title",
                    "news_lead", "news_image", "news_content", "is_duplicate", "is_disable")


        widgets = {
			'news_source':forms.TextInput(attrs={'class':'form-control'}),
			'news_url': forms.URLInput(attrs={'class': 'form-control'}),
            'news_title':forms.TextInput(attrs={'class':'form-control'}),
            'news_image': forms.URLInput(attrs={'class': 'form-control'}),
            'news_lead':forms.TextInput(attrs={'class':'form-control'}),
            'news_content': TinyMCE(mce_attrs={'class': 'form-control'}),
            'is_duplicate': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_disable': forms.CheckboxInput(attrs={'class':'form-check-input'})
		}


    def __init__(self, *args, **kwargs):
        super(AddNews_Form, self).__init__(*args, **kwargs)
        self.fields['news_date_time'] = SplitJalaliDateTimeField(label=('news date time'), # date format is  "yyyy-mm-dd"
            widget=AdminSplitJalaliDateTime# optional, to use default datepicker
        )



class UpdateNews_Form(forms.ModelForm):

    class Meta:

        model = NewsContents
        fields = ("news_source", "news_url", "news_date_time", "news_title",
                    "news_lead", "news_image", "news_content", "is_duplicate", "is_disable")


        widgets = {
			'news_source':forms.TextInput(attrs={'class':'form-control'}),
			'news_url': forms.URLInput(attrs={'class': 'form-control'}),
            'news_title':forms.TextInput(attrs={'class':'form-control'}),
            'news_image': forms.URLInput(attrs={'class': 'form-control'}),
            'news_lead':forms.TextInput(attrs={'class':'form-control'}),
            'news_content': TinyMCE(mce_attrs={'class': 'form-control'}),
            'is_duplicate': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_disable': forms.CheckboxInput(attrs={'class':'form-check-input'})
		}



class AddUser_form(forms.ModelForm):

    class Meta:

        model = AuthUser
        fields = ("username", "password", "first_name", "last_name",
                    "email", "is_active", "is_staff", "is_superuser")


        widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control'}),
			'password': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
		}





class UpdateUser_form(forms.ModelForm):

    class Meta:

        model = AuthUser
        fields = ("username", "password", "first_name", "last_name",
                    "email", "is_active", "is_staff", "is_superuser")


        widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control'}),
			'password': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
		}
