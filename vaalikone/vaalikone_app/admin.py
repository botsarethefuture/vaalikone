from django.contrib import admin

from parler.admin import TranslatableAdmin


from .models import ElectionCandidate, ElectionParty, Question

admin.site.register(ElectionParty, TranslatableAdmin)

admin.site.register(ElectionCandidate, TranslatableAdmin)

admin.site.register(Question, TranslatableAdmin)