from django.db import models

from parler.models import TranslatableModel, TranslatedFields


class ElectionParty(TranslatableModel):
    translations = TranslatedFields(
        Name=models.CharField(max_length=90),
        Description=models.CharField(max_length=250),
    )

    def __str__(self):
        return self.Name


class ElectionCandidate(TranslatableModel):
    translations = TranslatedFields(
        FirstName=models.CharField(max_length=30),
        LastName=models.CharField(max_length=30),
        CandidateNumber=models.IntegerField(max_length=50),
        Party=models.ForeignKey("ElectionParty", on_delete=models.CASCADE),
    )
