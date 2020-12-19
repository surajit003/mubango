from django.db import models
from business.models import Business

# Create your models here.


class Offer(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)
    code = models.CharField(max_length=120, blank=True, null=True)
    limit = models.IntegerField(default=0)

    def __str__(self):
        return "{} {}".format(self.title, self.business.name)

    class Meta:
        unique_together = ("business", "title")
        verbose_name_plural = "Offers"
