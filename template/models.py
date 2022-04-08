from django.db import models

class Template(TimeStampedModel):

    edital = models.CharField(
         db_column="EDITAL",
    )

    texto = models.TextField(
         db_column="TEXTO",
    )

    # projeto = models.ManyToOneRel

    class Meta:
            db_table = "TEMPLATE"
            verbose_name = "template"
            verbose_name_plural = "templates"
    
    def __str__(self) -> str:
        return self.edital
