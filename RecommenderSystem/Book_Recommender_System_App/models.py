from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone


class UserInfo(models.Model):
    """
    User for recommender book history
    """
    user = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    registration_date: models.DateField(null=True)

    class Meta:
        managed = True
        db_table = "UserInfo"


class UserRecommendation:
    """
    Model to save prediction to each user
    """
    recommendation = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    recommendation_date = models.DateField(null=True)

    class Meta:
        managed = True
        db_table = "UserRecommendations"









