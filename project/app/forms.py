from django import forms

#create forms
class students(forms.Form):
    #name = forms.CharField(max_length=50)
    name = forms.CharField(
                            max_length=50, 
                            #initial='sonam',
                            label='Your Name',
                            label_suffix=' ',                                                           #Fields Arguments
                            required=False,
                            #disabled=True,
                            help_text='limit 70 char',
                            #widget=forms.PasswordInput(),
                            )
    email = forms.EmailField(
                            #widget=forms.PasswordInput(),
                            #widget=forms.HiddenInput(),
                            #widget=forms.Textarea(),                                                   #Fields Widgets
                            #widget=forms.CheckboxInput(),
                            #widget=forms.FileInput(),
                            #widget=forms.TextInput(attrs={'class':'css1', 'id':'unique_id'}),
                        )