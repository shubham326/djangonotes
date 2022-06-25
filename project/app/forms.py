from django import forms

#create forms
class student(forms.Form):
    #name = forms.CharField(max_length=50)
    name = forms.CharField(
                            max_length=50, 
                            initial='sonam',
                            label='Your Name',
                            label_suffix=' ',
                            required=False,
                            disabled=True,
                            help_text='limit 70 char',
                            )
    email = forms.EmailField()