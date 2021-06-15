from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label = "Nombre", required=True, widget=forms.TextInput(
        attrs={'name':'name' ,'class':'form-control', 'id':'name', 'placeholder':'Tú nombre', 'data-rule':'minlen:4', 'data-msg':'Please enter at least 4 chars'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label = "Email", widget=forms.EmailInput(
        attrs={'class':'form-control', 'name':'email', 'id':'email', 'placeholder':'Tú correo', 'data-rule':'email', 'data-msg':'Please enter a valid email'}
    ), min_length=3, max_length=100)
    subject = forms.CharField(label = "Asunto", required=True, widget=forms.TextInput(
        attrs={'name':'subject' ,'class':'form-control', 'id':'subject', 'placeholder':'Asunto', 'data-rule':'minlen:4', 'data-msg':'Please enter at least 8 chars of subject'}
    ), min_length=3, max_length=100)
    content = forms.CharField(label = "Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'name':'message', 'rows':5, 'data-rule':'required', 'data-msg':'Please write something for us', 'placeholder':'Mensaje'}
    ), min_length=10, max_length=1000)

