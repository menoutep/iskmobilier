


from django.shortcuts import render, redirect
from .forms import RentalPropertyCreationForm,SalePropertyCreationForm
from .models import RentalProperty, Image,SaleProperty
from base.models import CustomUser
def index(request):
    # Traitement de la logique métier ici
    # ...
    
    # Définition du contexte à passer au template
    context = {
        'titre': "Page d'accueil",
        'message': 'Bienvenue sur mon site !',
    }

    # Rendu du template 'index.html' avec le contexte défini
    return render(request, 'index.html', context)


def profile(request):
    # Traitement de la logique métier ici
    # ...
    user = CustomUser.objects.get(id=request.user.id)
    # Définition du contexte à passer au template
    context = {
        'titre': "Page d'accueil",
        'message': 'Bienvenue sur mon site !',
    }

    # Rendu du template 'index.html' avec le contexte défini
    return render(request, 'index.html', context)



def create_rental_property(request):
    if request.method == 'POST':
        form = RentalPropertyCreationForm(request.POST, request.FILES)
        print(request.user.username)
        user = CustomUser.objects.get(username=request.user.username)
        print(form.data)
        print(form.errors)
        print(f" my custom user : {user}")
        print(form.is_valid())
        print(request.user.username)
        if form.is_valid():
            img = Image.objects.create(

                imgP=form.cleaned_data['img1'],
                imgS=form.cleaned_data['img2'],
                imgT=form.cleaned_data['img3'],
                imgQ=form.cleaned_data['img4'],
                imgC=form.cleaned_data['img5'],
                imgSi=form.cleaned_data['img6']
                
            )
            print(user)
            rental_property = RentalProperty.objects.create(
                title=form.cleaned_data['title'],
                images = img,
                description=form.cleaned_data['description'],
                rental_price=form.cleaned_data['rental_price'],
                rental_period=form.cleaned_data['rental_period'],
                security_deposit=form.cleaned_data['security_deposit'],
                area=form.cleaned_data['area'],
                number_of_rooms=form.cleaned_data['number_of_rooms'],
                negotiable=form.cleaned_data['negotiable'],
                location = form.cleaned_data['location'],
                latitude = form.cleaned_data['latitude'],
                longitude = form.cleaned_data['longitude'],
                vendor = user)
            print(f"bien : {rental_property}")

            return redirect('base:index')
    else:
        form = RentalPropertyCreationForm()
    return render(request, 'base/rental_add_form.html', {'form': form})

def create_sale_property(request):
    if request.method == 'POST':
        form = SalePropertyCreationForm(request.POST, request.FILES)
        print(request.user.username)
        user = CustomUser.objects.get(username=request.user.username)
        print(form.data)
        print(form.errors)
        print(f" my custom user : {user}")
        print(form.is_valid())
        print(request.user.username)
        if form.is_valid():
            img = Image.objects.create(

                imgP=form.cleaned_data['img1'],
                imgS=form.cleaned_data['img2'],
                imgT=form.cleaned_data['img3'],
                imgQ=form.cleaned_data['img4'],
                imgC=form.cleaned_data['img5'],
                imgSi=form.cleaned_data['img6']
                
            )
            print(user)
            sale_property = SaleProperty.objects.create(
                title=form.cleaned_data['title'],
                images = img,
                description=form.cleaned_data['description'],
                sale_price=form.cleaned_data['sale_price'],
                area=form.cleaned_data['area'],
                number_of_rooms=form.cleaned_data['number_of_rooms'],
                negotiable=form.cleaned_data['negotiable'],
                location = form.cleaned_data['location'],
                latitude = form.cleaned_data['latitude'],
                longitude = form.cleaned_data['longitude'],
                vendor = user)
            print(f"bien : {sale_property}")

            return redirect('base:index')
    else:
        form = SalePropertyCreationForm()
    return render(request, 'base/sale_add_form.html', {'form': form})
