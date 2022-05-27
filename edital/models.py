from django.db import models
from django_extensions.db.models import TimeStampedModel

class EditalModel(TimeStampedModel):

    edital = models.CharField(
         db_column="EDITAL",
          max_length=50,
    )

    texto = models.TextField(
         db_column="TEXTO",
         max_length=100,
    )


    class Meta:
            db_table = "EDITAL"
            verbose_name = "edital"
            verbose_name_plural = "editais"
    
    def __str__(self) -> str:
        return self.edital
