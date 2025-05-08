from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    """ A view to return the homepage """
    return render(request, 'pages/home.html')

def about(request):
    """ A view to return the about page """
    return render(request, 'pages/about.html')

def privacy_policy(request):
    """ A view to return the privacy policy page """
    return render(request, 'pages/privacy_policy.html')

def terms(request):
    """ A view to return the terms and conditions page """
    return render(request, 'pages/terms.html')

def shipping_returns(request):
    """ A view to return the shipping & returns page """
    return render(request, 'pages/shipping_returns.html')

def contact(request):
    """ A view to return the contact page """
    return render(request, 'pages/contact.html')

def contact_submit(request):
    """ Handle the contact form submission """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Here you would typically save this to a database or send an email
        # For now, we'll just return a success message
        
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
        return redirect('pages:contact')
    
    # If not a POST request, redirect back to contact form
    return redirect('pages:contact')

def coming_soon(request, feature=None):
    """ A view to return the coming soon page with context about the feature """
    context = {
        'feature': feature or 'This feature'
    }
    return render(request, 'pages/coming_soon.html', context)
