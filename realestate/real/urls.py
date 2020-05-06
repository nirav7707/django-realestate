from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
	path('',views.main,name='home'),
	path('<int:i_id>',views.get_value,name='show'),
	path('create',views.create,name='create')
	
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)