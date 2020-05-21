from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
	path('',views.main,name='home'),
	path('product_view',views.productview,name="product_view"),
	# path('<int:i_id>',views.productdetail,name="product_detail"),
	path('<int:i_id>',views.get_value,name='product_detail'),
	path('create',views.create,name='create')
	
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)