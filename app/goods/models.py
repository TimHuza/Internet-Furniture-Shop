from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="goods_images", blank=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("id",)

    def __str__(self):
        return self.name

    # Category -> id prefix mapping used to build the human-readable product id
    CATEGORY_ID_PREFIXES = {
        "bedroom": "10",
        "kitchen": "20",
        "living-room": "30",
        "office": "40",
        "furniture": "50",
        "decoration": "60",
    }

    def display_id(self):
        prefix = self.CATEGORY_ID_PREFIXES.get(self.category.slug, "00")
        return f"{prefix}{self.id:03}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2) 
        return self.price