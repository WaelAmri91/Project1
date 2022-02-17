from dataclasses import fields
import email
from inspect import Parameter
from operator import truediv
from queue import Empty
from turtle import title
from django.contrib import admin,messages
from .models import *

# Register your models here.
class ProjectInline(admin.TabularInline):
    model=Projet
class StudentAdmin(admin.ModelAdmin):
    list_display=(
        'last_name',
        'first_name'
    )
    fields=(
        ('last_name','first_name'),
        'email' 
    )
    search_fields=['last_name','first_name']
    inlines=[ProjectInline]
class CoachAdmin(admin.ModelAdmin):
    list_display=(
        'last_name',
        'first_name'
    )
    fields=(
        ('last_name','first_name'),
        'email' 
    )
    search_fields=['last_name','first_name']

class ProjectDurationFilter(admin.SimpleListFilter):
    parameter_name ="dure"
    title ="durée"
    def lookups (self, request, model_admin):
            return(
                ('1 Month','less than 1 month'),
                ('3 Months','less than 3 months'),
                ('4 Months','greater than 4 months')
            )

    def queryset(self, request, queryset):
            if self.value()=="1 Month":
                return queryset.filter(dure__lte=30)
            if self.value()=="3 Months":
                return queryset.filter(dure__gt=30, dure__lte=90) 
            if self.value()=="4 Months":
                return queryset.filter(dure__gt=90)   
def set_Valid(modeladmin, request, queryset):
        rows = queryset.update(isValid=True)
        if rows ==1:
            msg ="1 project was"
        else:
            msg =f"{rows} projects were"
        messages.success(request,message=f"{msg}successfully marked as valid")  
set_Valid.short_description ="validate"      
                        
@admin.register(Projet)
class ProjectAdmin(admin.ModelAdmin):
        def set_invalid(modeladmin, request, queryset):
            number = queryset.filter(isValid=False)
            if(number.count()>0):
                 messages.error(request,"Projects already set to not valid")
            else :
                rows=queryset.update(isValid=False)
                if rows ==1:
                    msg ="1 project was"
                else:
                    msg =f"{rows} projects were"
                messages.success(request,message=f"{msg}successfully marked as not valid")  
        set_invalid.short_description ="invalidate" 

        actions = [set_Valid , 'set_invalid']
        actions_on_bottom =True
        actions_on_top =True 

        list_filter =(
            'creator',
            'isValid',
            ProjectDurationFilter
        )
        list_display=(
        'project_name',
        'dure',
        'supervisor',
        'creator',
        'isValid'
        )
        fieldsets=[
            (
                None,
                {
                    'fields':('isValid',)
                }
            ),
            (
                'About',
                {
                    'fields':(
                    'project_name',
                    ('creator','supervisor'),
                    'besoin',
                    'description'
                    )
                }
            ),
            (
                'dure',
                {
                    'classes':('collapse',),
                    'fields':(
                        'dure',
                        'temp_allocated'
                    )
                }
            )
            ] 
       # radio_fields = {'supervisor':admin.VERTICAL}
        autocomplete_fields=['supervisor']
        Empty_value_display='-empty-'
      
    
     
admin.site.register(MemberShip)
admin.site.register(Student,StudentAdmin)
admin.site.register(Coach,CoachAdmin)

