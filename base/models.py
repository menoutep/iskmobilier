from django.db import models

from accounts.models import CustomUser
class Tags(models.Model):
    name=models.CharField(max_length=100)
    # Standar
    statut = models.BooleanField(default=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering=['-updated', '-created']
     


class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_rooms = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def nearby_properties(self):
        nearby_properties = Property.objects.exclude(pk=self.pk).filter(
            latitude__range=(self.latitude - 0.15, self.latitude + 0.15),
            longitude__range=(self.longitude - 0.15, self.longitude + 0.15)
        )
        return nearby_properties


class Image(models.Model):
    
    imgP=models.FileField(upload_to="image_articles/%y")
    imgS=models.FileField(upload_to="image_articles/%y",null=True, blank=True)
    imgT=models.FileField(upload_to="image_articles/%y",null=True, blank=True)
    imgQ=models.FileField(upload_to="image_articles/%y",null=True, blank=True)
    imgC=models.FileField(upload_to="image_articles/%y",null=True, blank=True)
    imgSi=models.FileField(upload_to="image_articles/%y",null=True, blank=True)
    imgSe=models.FileField(upload_to="image_articles/%y",null=True, blank=True)

  

class RentalProperty(Property):
    vendor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rentals_properties')
    images = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='rentals_properties')
    rental_price = models.DecimalField(max_digits=30, decimal_places=2)
    rental_period = models.CharField(max_length=50)
    security_deposit = models.DecimalField(max_digits=30, decimal_places=2)
    negotiable = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.title} - {self.rental_price}"

class SaleProperty(Property):
    vendor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sales_properties')
    images = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='sales_properties')
    sale_price = models.DecimalField(max_digits=30, decimal_places=2)
    negotiable = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.sale_price}"

