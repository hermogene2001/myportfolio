from django.contrib import admin
from .models import Contact, Project, Skill, Experience, Profile, Education


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'avatar', 'bio')
        }),
        ('Headlines', {
            'fields': ('headline_1', 'headline_2', 'headline_3'),
            'description': 'These will be animated on the hero section'
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Media Links', {
            'fields': ('linkedin_url', 'github_url', 'twitter_url', 'instagram_url', 'facebook_url', 'youtube_url'),
            'description': 'Leave blank if you don\'t have this social media account'
        }),
    )
    readonly_fields = ('updated_at',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'field_of_study', 'school', 'start_date', 'end_date', 'is_current')
    list_filter = ('school', 'is_current', 'start_date')
    search_fields = ('school', 'degree', 'field_of_study')
    fieldsets = (
        ('Education Details', {
            'fields': ('school', 'degree', 'field_of_study', 'grade')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Additional Information', {
            'fields': ('description',)
        }),
    )


admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Experience)
