from django.contrib import admin
from .models import Category, Attribute, Product, ProductAttributeValue

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "price")
    list_filter = ("category",)
    search_fields = ("title",)


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "attribute", "value")
    list_filter = ("attribute", "product__category")
    search_fields = ("product__name", "attribute__name", "value")