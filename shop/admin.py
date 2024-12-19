from django.contrib import admin
from shop.models import Category, Item, Tag

class ItemInline(admin.StackedInline):
    model = Item
    extra = 1
    fields = ['name','price','description']

class TagInline(admin.StackedInline):
    model = Item.tags.through
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','get_five_items']
    search_fields = ['name','id','items__name']
    ordering = ['id']
    list_per_page = 100
    inlines = [ItemInline]

    def get_five_items(self, category):
        return [item.name for item in category.items.all()[:5]]
    
    def get_queryset(self, request):
        existing_queryset = super().get_queryset(request)
        return existing_queryset.prefetch_related('items')



admin.site.register(Category, CategoryAdmin)

class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['price']
    list_display = ['id','name','price']
    fields = ['name','description','price','category']
    autocomplete_fields = ['category']
    inlines = [TagInline]
    list_filter = ['price']

admin.site.register(Item, ItemAdmin)

class TagItemInline(admin.TabularInline):
    model = Tag.items.through
    extra = 1

class TagAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name']
    inlines = [TagItemInline] 

admin.site.register(Tag, TagAdmin)