from django.db import models
from business.models import Business
from common.models import DateModel
from django.contrib.auth.models import User


class Review(DateModel):
    level_of_experience = (
        ("positive", "Positive"),
        ("neutral", "Neutral"),
        ("negative", "Negative"),
    )
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    comment = models.TextField()
    experience = models.CharField(
        max_length=20, choices=level_of_experience, default="neutral"
    )
    rating = models.IntegerField(default=1)
    images = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Reviews"
        unique_together = ("business", "user")

    def __str__(self):
        return "{} {} {}".format(self.id, self.user.username, self.business.name)
