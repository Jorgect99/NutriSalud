from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):

    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data = request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name', '')
            subject = request.POST.get('subject', '')
            content = request.POST.get('content', '')
            email = request.POST.get('email', '')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "NutriSalud: Nuevo mensaje de contacto",
                "De {} <{}>\n{}\n\nEscribio:\n\n{}".format(name, email, subject, content),
                "no-contestar@inbox.mailtrap.io",
                ["jorgect99@gmail.com"],
                reply_to=[email],
            )
            try:
                email.send()
                #Todo salio bien
                return redirect(reverse('home')+"?ok")
            except:
                #Algo salio mal
                return redirect(reverse('home')+"?fail")

    return render(request, 'web/index.html', {'contact_form':contact_form})