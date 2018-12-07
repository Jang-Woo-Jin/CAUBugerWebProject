from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .forms import ContactForm
from .models import Contact, MyContact

# Create your views here.
def contact_list(request):
    contacts = Contact.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'mycontact/contact_list.html', {'contacts':contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'mycontact/contact_detail.html', {'contact': contact})

def contact_new(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = request.user
            contact.published_date = timezone.now()
            contact.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm()
    return render(request, 'mycontact/contact_edit.html', {'form': form})    

def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = request.user
            contact.published_date = timezone.now()
            contact.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'mycontact/contact_edit.html', {'form': form})