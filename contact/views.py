from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_view(request):
    print('testttttttttttttttttttttttttttttttt')
    if request.method == 'POST':
        print('here')
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
        else:
            print(form.errors)
    else:
        print('GET request received')
        form = ContactForm()
    return render(request, 'index.html', {'form': form})
