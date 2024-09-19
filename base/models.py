from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=300, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    version = models.PositiveIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['price']),
            models.Index(fields=['created_at']),
        ]