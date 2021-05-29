from django.urls import path
from .views import ClientListView, DepartmentListView, DiscountCardListView, ClientDetailView, \
    clients_delete, clients_create, index, clients_update, DepartmentDetailView, department_delete, department_create, \
    department_update, DiscountCardDetailView, discount_card_create, discount_card_update, discount_card_delete, \
    PositionListView, position_delete, PositionDetailView, position_update, ProductListView, product_create, \
    product_delete, ProductDetailView, product_update, ProviderListView, provider_create, provider_delete, \
    ProviderDetailView, provider_update

urlpatterns = [
    path('', index, name='index'),

    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/<slug:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/<slug:pk>/delete/', clients_delete, name='client_detail_delete'),
    path('clients/create', clients_create, name='client_create'),
    path('clients/<slug:pk>/update/', clients_update, name='client_update'),

    path('departments/', DepartmentListView.as_view(), name='department_list'),
    path('departments/<slug:pk>/', DepartmentDetailView.as_view(), name='department_detail'),
    path('departments/<slug:pk>/delete/', department_delete, name='department_delete'),
    path('departments/create', department_create, name='department_create'),
    path('departments/<slug:pk>/update/', department_update, name='department_update'),

    path('discount_cards/', DiscountCardListView.as_view(), name='discount_card_list'),
    path('discount_cards/<slug:pk>/', DiscountCardDetailView.as_view(), name='discount_card_detail'),
    path('discount_cards/create', discount_card_create, name='discount_card_create'),
    path('discount_cards/<slug:pk>/update/', discount_card_update, name='discount_card_update'),
    path('discount_cards/<slug:pk>/delete/', discount_card_delete, name='discount_card_delete'),

    path('positions/', PositionListView.as_view(), name='position_list'),
    path('positions/create', discount_card_create, name='position_create'),
    path('positions/<slug:pk>/delete/', position_delete, name='position_delete'),
    path('positions/<slug:pk>/', PositionDetailView.as_view(), name='position_detail'),
    path('positions/<slug:pk>/update/', position_update, name='position_update'),

    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create', product_create, name='product_create'),
    path('products/<slug:pk>/delete/', product_delete, name='product_delete'),
    path('products/<slug:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<slug:pk>/update/', product_update, name='product_update'),

    path('providers/', ProviderListView.as_view(), name='provider_list'),
    path('providers/create', provider_create, name='provider_create'),
    path('providers/<slug:pk>/delete/', provider_delete, name='provider_delete'),
    path('providers/<slug:pk>/', ProviderDetailView.as_view(), name='provider_detail'),
    path('providers/<slug:pk>/update/', provider_update, name='provider_update'),
]
