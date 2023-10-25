from django.contrib import admin

from .models import Category, Item

class CategoryAdmin(admin.ModelAdmin):
    def display_subcategories(self, obj):
        subcategories = obj.subcategories.all()
        if subcategories:
            return ", ".join([subcategory.name for subcategory in subcategories])
        return "-"

    display_subcategories.short_description = 'Subcategories'

    list_display = ('name', 'desciption', 'display_subcategories')
    list_filter = ('parent_category',)
    search_fields = ('name', 'desciption')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item)