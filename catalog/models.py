from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    TYPE_CHOICES = [
        ("string", "String"),
        ("number", "Number"),
        ("boolean", "Boolean"),
        ("date", "Date"),
        ("enum", "Enum"),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="attributes")
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    required = models.BooleanField(default=False)
    allowed_values = models.TextField(blank=True, null=True) # only for enums

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    sku = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="attribute_values")
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.TextField()

    class Meta:
        unique_together = ("product", "attribute")

    def __str__(self):
        return f"{self.product.title} - {self.attribute.name}: {self.value}"



        