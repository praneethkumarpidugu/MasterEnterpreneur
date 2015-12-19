from django.contrib import admin

# Register your models here.
from .models import Video, Category

class VideoAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", 'slug']
    fields = ['title', 'share_message','embed_code',
                 'active', 'featured',
                 'free_preview', 'category']

    #prepopulated_fields = {'slug': ['title'],}

    class Meta:
        model = Video


admin.site.register(Category)
admin.site.register(Video, VideoAdmin)


