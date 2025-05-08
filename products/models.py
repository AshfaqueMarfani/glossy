from django.db import models
import os

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name or self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    ingredients = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    has_variants = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
        
    def get_image_url(self):
        """Return image URL or appropriate placeholder based on category"""
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
            
        # Use category-specific placeholder if available
        if self.category:
            category_name = self.category.name.lower()
            placeholder_path = f'media/product_images/{category_name}_placeholder.jpg'
            if os.path.exists(placeholder_path):
                return f'/media/product_images/{category_name}_placeholder.jpg'
                
        # Fallback to a generic placeholder
        return '/media/product_images/default_placeholder.jpg'


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # e.g., "Shade 01 - Light", "Size 30ml"
    sku_suffix = models.CharField(max_length=10, null=True, blank=True)  # To be appended to the base SKU
    price_adjustment = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    stock_qty = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.product.name} - {self.name}"
    
    @property
    def full_sku(self):
        if self.product.sku and self.sku_suffix:
            return f"{self.product.sku}-{self.sku_suffix}"
        return None
    
    @property
    def final_price(self):
        return self.product.price + self.price_adjustment
        
    def get_image_url(self):
        """Return variant image or parent product image"""
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return self.product.get_image_url()
