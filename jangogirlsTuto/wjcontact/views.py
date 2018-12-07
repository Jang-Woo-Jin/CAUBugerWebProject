from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .forms import ContactForm
from .models import WJContact

# Create your views here.
def contact_list(request):
    contacts = WJContact.objects.filter(created_date__lte=timezone.now()).order_by('name')
        
    search = request.GET.get('search','')
    if search:
        contacts =contacts.filter(name__icontains=search).order_by('name')
        return render(request, 'wjcontact/contact_list.html', {'contacts':contacts})
    else:
        return render(request, 'wjcontact/contact_list.html', {'contacts':contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(WJContact, pk=pk)
    return render(request, 'wjcontact/contact_detail.html', {'contact': contact})

def contact_new(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = request.user
            contact.created_date = timezone.now()
            contact.save()
            return redirect('wjcontact_detail', pk=contact.pk)
    else:
        form = ContactForm()
    return render(request, 'wjcontact/contact_edit.html', {'form': form})    

def contact_edit(request, pk):
    contact = get_object_or_404(WJContact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = request.user
            contact.created_date = timezone.now()
            contact.save()
            return redirect('wjcontact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'wjcontact/contact_edit.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(WJContact, pk=pk)
    contact.delete()
    return redirect('wjcontact_list')
 