from django.db import models
from django.utils.translation import gettext_lazy as _

class word_tr(models.Model):
    word_pr = models.CharField(_("متن در غالب الفبا"), max_length=50)
    word_lt = models.CharField(_("متن در نوشتار لاتین"), max_length=50)
    meaning = models.CharField(_("معنی در یک کلمه به پارسی"), max_length=50)
    info = models.TextField(_("توضیحات به پارسی"), max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.word_pr} ({self.word_lt}) - {self.meaning}:\n [{self.info}]"


