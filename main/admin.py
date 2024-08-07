from django.contrib import admin
from .models import Issue, Member, Contribution

class IssueAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Issue model.

    Attributes:
        fieldsets (list): Defines the layout of the admin form for the Issue model.
        list_display (tuple): Specifies the fields to be displayed in the list view of the admin panel.
        list_filter (list): Adds a filter sidebar to filter issues by publication date.
        search_fields (list): Adds a search box to search issues by title.
    """

    fieldsets = [
        (None, {'fields': ['title', 'description']}),  # Basic fields (title and description).
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),  # Collapsible section for the publication date.
    ]
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']

# Register the Issue model with the custom IssueAdmin configuration.
admin.site.register(Issue, IssueAdmin)

# Register the Member model with the default configuration.
admin.site.register(Member)

# Register the Contribution model with the default configuration.
admin.site.register(Contribution)

