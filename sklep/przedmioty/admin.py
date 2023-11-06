from django.contrib import admin

from .models import Category, Item

class CategoryAdmin(admin.ModelAdmin):
    def display_subcategories(self, obj):
        subcategories = obj.subcategories.all()
        if subcategories:
            return ", ".join([subcategory.name for subcategory in subcategories])
        return "-"

    display_subcategories.short_description = 'Subcategories'  # Nadanie nazwy dla wyświetlania podkategorii.

    list_display = ('name', 'desciption', 'display_subcategories')  # Wyświetlane kolumny w liście kategorii w panelu admina.
    list_filter = ('parent_category',)  # Filtracja kategorii według rodzica.
    search_fields = ('name', 'desciption')  # Możliwość wyszukiwania kategorii po nazwie lub opisie.

admin.site.register(Category, CategoryAdmin)  # Zarejestrowanie modelu Category z dostosowanym panelem admina.
admin.site.register(Item)  # Zarejestrowanie modelu Item z domyślnym panelem admina.
