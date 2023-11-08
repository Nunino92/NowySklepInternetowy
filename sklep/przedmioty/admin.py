from django.contrib import admin

from .models import Category, Item

class CategoryAdmin(admin.ModelAdmin):
    def display_subcategories(self, obj): #self instacje admina, obj instacje modeli z admina
        subcategories = obj.subcategories.all() #wszystkie dane subcategorie
        if subcategories:
            return ", ".join([subcategory.name for subcategory in subcategories])
        return "-"

    display_subcategories.short_description = 'Subcategories' #opis-panel

    list_display = ('name', 'desciption', 'display_subcategories') # wyswietlane w admin
    list_filter = ('parent_category',) #filtruje dane na liscie, ktore pasuja do wybranego rekordu
    search_fields = ('name', 'desciption')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item)