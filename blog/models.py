from django.db import models

class Query(models.Model):
        class Meta:
            db_table = "query_table"

        link = models.URLField(verbose_name='Ссылка', default='')
        link_date = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.link

        objects = models.Manager()