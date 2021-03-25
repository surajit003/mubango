from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from business.models import Business, Service
from common.models import DateModel
from django.contrib.auth.models import User


class ReviewManager(models.Manager):
    def get_queryset(self):
        return super(ReviewManager, self).get_queryset().filter(moderated=True)

    def get_review_for_a_specific_user(self, username):
        # get review for a specific user
        return self.get_queryset().filter(
            user__username=username,
        )

    def review_for_a_business(self, business):
        # includes review for a business
        return self.get_queryset().filter(
            business__name=business,
        )


class Review(DateModel):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    experience = models.CharField(max_length=200)
    image_1 = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    image_3 = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    moderated = models.BooleanField(default=False)
    objects = models.Manager()  # The default manager.
    review_manager = ReviewManager()  # The review manager.

    class Meta:
        verbose_name_plural = "Reviews"
        unique_together = ("business", "user")

    def __str__(self):
        return "{} {} {}".format(self.id, self.user.username, self.business.name)


class BusinessServiceRating(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{} {} {}".format(self.service.name, self.business.name, self.rating)
