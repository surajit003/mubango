from django.db import models
from business.models import Business
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
    ratings = models.IntegerField(default=1)
    images = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    moderated = models.BooleanField(default=False)

    objects = models.Manager()  # The default manager.
    review_manager = ReviewManager()  # The review manager.

    class Meta:
        verbose_name_plural = "Reviews"
        unique_together = ("business", "user")

    def __str__(self):
        return "{} {} {}".format(self.id, self.user.username, self.business.name)

    def conv_star_to_rating(self, star_rating):
        if star_rating == "*":
            self.ratings = 1
        elif star_rating == "**":
            self.ratings = 2
        elif star_rating == "***":
            self.ratings = 3
        elif star_rating == "****":
            self.ratings = 4
        elif star_rating == "*****":
            self.ratings = 5
        self.save()
