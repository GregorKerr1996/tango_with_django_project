from django.contrib import admin
from rango.models import Category, Page, PageAdmin

# Register your models here.
#admin.site.register(Category)

class CategoryAdmin(admin.ModelAdmin):
     prepopulated_fields = { 'slug' : ('name',)}

     
class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url')

admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)




