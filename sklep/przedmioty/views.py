from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Category, Item





def items(request):
    # Pobieranie parametrów zapytania GET, tj. 'query' i 'category'.
    query = request.GET.get('query', '') # Wyszukiwanie wg nazwy lub opisu przedmiotu.
    category_id = request.GET.get('category', 0) # Filtruj przedmioty według kategorii.

    # Pobieranie tylko unikalnych kategorii, które nie mają podkategorii.
    categories = Category.objects.filter(subcategories__isnull=True).distinct()

    # Pobieranie nie sprzedanych przedmiotów.
    items = Item.objects.filter(is_sold=False)

    if category_id:
        # Jeśli określono kategorię, filtrowanie przedmiotów według kategorii.
        items = items.filter(category_id=category_id)

    if query:
        # Jeśli jest podany parametr 'query', filtrowanie przedmiotów według nazwy lub opisu.
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    # Renderowanie szablonu z kontekstem zawierającym przefiltrowane przedmioty i inne dane.
    return render(request, 'item/items.html', {
        'items': items, # Przefiltrowane przedmioty.
        'query': query, # Wartość parametru 'query' dla wyświetlenia w formularzu.
        'categories': categories, # Unikalne kategorie.
        'category_id': int(category_id) # Wybrana kategoria (jeśli jest określona).
    })
@login_required()
def detail(request, pk):
    # Pobierz szczegóły przedmiotu o określonym identyfikatorze (pk).
    item = get_object_or_404(Item, pk=pk)

    # Pobierz powiązane przedmioty w tej samej kategorii (nie sprzedane) i wyklucz bieżący przedmiot.
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    # Renderuj szablon 'detail.html' z danymi przedmiotu i powiązanych przedmiotów.
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            # Jeśli formularz jest poprawny, tworzy nowy przedmiot i przypisuje go do zalogowanego użytkownika.
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    # Renderowanie formularza tworzenia nowego przedmiotu.
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })


@login_required
def edit(request, pk):
    # Pobieranie przedmiotu do edycji, pod warunkiem, że użytkownik jest jego właścicielem.
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            # Jeśli formularz jest poprawny, zapisuje zmiany.
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    # Renderowanie formularza edycji przedmiotu.
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })
@login_required
def delete(request, pk):
    # Pobieranie przedmiotu do usunięcia, pod warunkiem, że użytkownik jest jego właścicielem.
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    # Usuwanie przedmiotu i przekierowanie użytkownika na inną stronę (panel:index).
    item.delete()
    return redirect('panel:index')

@login_required()
def buy(request, pk):
    # Pobieranie szczegółów przedmiotu do zakupu.
    item = get_object_or_404(Item, pk=pk)

    context = {
        'item': item,
    }

    # Renderowanie strony 'buy.html' z kontekstem zawierającym szczegóły przedmiotu.
    return render(request, 'item/buy.html', context)