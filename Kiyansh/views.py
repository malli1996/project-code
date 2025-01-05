
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
# hello world
def home(request):
    # home view.
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'phone':phone,
            'message':message,
        }
        print('hello',form_data)
        msg = '''
        From:\n\t\t{}\n
        Email:\n\t\t{}\n
        phone:\n\t\t{}\n
        message:\n\t\t{}\n
        '''.format(form_data['name'], form_data['email'], form_data['phone'],form_data['message'])
        send_mail('You got a mail!', msg, email, ['mallikarjuna762@gmail.com']) # TODO: enter your email address

    return render(request, 'index.html', {})

# def contact(request):
#     return render(request, 'contact.html', {})

# def projects(request):
#     return render(request, 'projects.html', {})


def contact_view(request):
    # CONTACT FORM
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message,
        }
        print('hello',form_data)
        msg = '''
        From:\n\t\t{}\n
        subject:\n\t\t{}\n
        Email:\n\t\t{}\n
        message:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['subject'])
        send_mail('You got a mail!', msg, email, ['mallikarjuna762@gmail.com']) # TODO: enter your email address
         
        
    return render(request, 'contact.html', {})

