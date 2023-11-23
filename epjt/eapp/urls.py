from django.urls import path
from.import views
app_name='eapp'
urlpatterns = [
    path('', views.allpdtcart, name='allpdtcart'),
    path('<slug:c_slug>/', views.allpdtcart, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetls, name='procatdet'),

]
