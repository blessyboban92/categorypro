
from django.urls import path
from . import views
app_name='finalapp'
urlpatterns = [
       path('AddCategory/',views.addcategory,name='addcategory'),
        path('add_category',views.add_category,name='add_category'),
       path('delete_category/<int:categoryid>/',views.delete_category,name='delete_category'),
       path('edit_category/<int:categoryid>/',views.edit_category,name='edit_category'),

]
