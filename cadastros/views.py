from django.shortcuts import render
from .forms import ClienteForm

def cliente(request):
    sucesso = False
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            sucesso = True
            form = ClienteForm()
    else:
        form = ClienteForm()
    return render(request, 'cliente.html',{
        'form': form,
        'sucesso': sucesso
    })
