from django.contrib import admin

from .models import District_Mapping

# When django displays a model instance in the admin or in Python shell, by default, it just used the models name along
# with the word object and the id of that object. We can change this by overriding __str__ in the model class.
# Note: This is different from using the list display attribute which overrides attribute in ModelAdmin class.
# We need to register this class with the model that it is associated with. For that we will use a decorator from the
# admin module called register. This will take model class as an argument

@admin.register(District_Mapping)
class mappingAdmin(admin.ModelAdmin):
    list_display = ['state_id', 'district_id', 'district_name', 'state_name']
