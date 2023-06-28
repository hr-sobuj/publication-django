from django.contrib import admin
from App_Home.models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['book_title', 'writer', 'publisher','price']

admin.site.register(Book,BookAdmin)