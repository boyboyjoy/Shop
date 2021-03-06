from django.urls import path
from .views import ClientListView, DepartmentListView, DiscountCardListView, ClientDetailView, \
    clients_delete, clients_create, index, clients_update, DepartmentDetailView, department_delete, department_create, \
    department_update, DiscountCardDetailView, discount_card_create, discount_card_update, discount_card_delete, \
    PositionListView, position_delete, PositionDetailView, position_update, ProductListView, product_create, \
    product_delete, ProductDetailView, product_update, ProviderListView, provider_create, provider_delete, \
    ProviderDetailView, provider_update, SaleListView, sale_create, WorkerListView, worker_create, worker_delete, \
    WorkerDetailView, worker_update, WriteOffReasonListView, write_off_reason_create, write_off_reason_delete, \
    write_off_reason_update, WriteOffReasonDetailView, WriteOffProductListView, write_off_product_create, \
    write_off_product_delete, WriteOffProductDetailView, write_off_product_update, sale_delete, SaleDetailView, \
    sale_update, SupplyListView, supply_create, supply_delete, supply_update, SupplyDetailView, position_create, \
    get_workers_list, get_worker_report, clients_finder, workers_finder, sales_finder, providers_finder, \
    products_finder, supplies_finder, write_off_products_finder

urlpatterns = [
    path('', index, name='index'),


    path('workers/reports', get_workers_list, name='reports'),
    path('workers/reports/<slug:pk>', get_worker_report, name='get_report'),

    path('clients/find/', clients_finder, name='client_find'),
    path('workers/find/', workers_finder, name='worker_find'),
    path('sales/find/', sales_finder, name='sale_find'),
    path('providers/find/', providers_finder, name='provider_find'),
    path('products/find/', products_finder, name='product_find'),
    path('supplies/find/', supplies_finder, name='supply_find'),
    path('write_off_products/find/', write_off_products_finder, name='write_off_product_find'),

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
    path('positions/create', position_create, name='position_create'),
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

    path('sales/', SaleListView.as_view(), name='sale_list'),
    path('sales/create', sale_create, name='sale_create'),
    path('sales/<slug:pk>/delete/', sale_delete, name='sale_delete'),
    path('sales/<slug:pk>/', SaleDetailView.as_view(), name='sale_detail'),
    path('sales/<slug:pk>/update/', sale_update, name='sale_update'),

    path('workers/', WorkerListView.as_view(), name='worker_list'),
    path('workers/create', worker_create, name='worker_create'),
    path('workers/<slug:pk>/delete/', worker_delete, name='worker_delete'),
    path('workers/<slug:pk>/', WorkerDetailView.as_view(), name='worker_detail'),
    path('workers/<slug:pk>/update/', worker_update, name='worker_update'),

    path('write_off_reasons/', WriteOffReasonListView.as_view(), name='write_off_reason_list'),
    path('write_off_reasons/create', write_off_reason_create, name='write_off_reason_create'),
    path('write_off_reasons/<slug:pk>/delete/', write_off_reason_delete, name='write_off_reason_delete'),
    path('write_off_reasons/<slug:pk>/', WriteOffReasonDetailView.as_view(), name='write_off_reason_detail'),
    path('write_off_reasons/<slug:pk>/update/', write_off_reason_update, name='write_off_reason_update'),

    path('write_off_products/', WriteOffProductListView.as_view(), name='write_off_product_list'),
    path('write_off_products/create', write_off_product_create, name='write_off_product_create'),
    path('write_off_products/<slug:pk>/delete/', write_off_product_delete, name='write_off_product_delete'),
    path('write_off_products/<slug:pk>/', WriteOffProductDetailView.as_view(), name='write_off_product_detail'),
    path('write_off_products/<slug:pk>/update/', write_off_product_update, name='write_off_product_update'),

    path('supplies/', SupplyListView.as_view(), name='supply_list'),
    path('supplies/create', supply_create, name='supply_create'),
    path('supplies/<slug:pk>/delete/', supply_delete, name='supply_delete'),
    path('supplies/<slug:pk>/', SupplyDetailView.as_view(), name='supply_detail'),
    path('supplies/<slug:pk>/update/', supply_update, name='supply_update'),

]
