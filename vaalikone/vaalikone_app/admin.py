from django.contrib import admin

from parler.admin import TranslatableAdmin


from .models import ElectionCandidate, ElectionParty

admin.site.register(ElectionParty, TranslatableAdmin)

admin.site.register(ElectionCandidate, TranslatableAdmin)
