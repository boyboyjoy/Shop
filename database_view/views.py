from django.views.generic import ListView
from database_view.models import ClientModel, DepartmentModel, DiscountCardModel, PositionModel, ProductModel, \
    ProviderModel, SaleModel, WorkerModel, WriteOffProductModel, WriteOffReasonModel

BASE_TEMPLATE_NAME = 'base_template.html'


class ClientListView(ListView):
    model = ClientModel
    template_name = BASE_TEMPLATE_NAME


class DepartmentListView(ListView):
    model = DepartmentModel
    template_name = BASE_TEMPLATE_NAME


class DiscountCardListView(ListView):
    model = DiscountCardModel
    template_name = BASE_TEMPLATE_NAME


class PositionListView(ListView):
    model = PositionModel
    template_name = BASE_TEMPLATE_NAME


class ProductListView(ListView):
    model = ProductModel
    template_name = BASE_TEMPLATE_NAME


class ProviderListView(ListView):
    model = ProviderModel
    template_name = BASE_TEMPLATE_NAME


class SaleListView(ListView):
    model = SaleModel
    template_name = BASE_TEMPLATE_NAME


class SupplyListView(ListView):
    model = SaleModel
    template_name = BASE_TEMPLATE_NAME


class WorkerListView(ListView):
    model = WorkerModel
    template_name = BASE_TEMPLATE_NAME


class WriteOffProductListView(ListView):
    model = WriteOffProductModel
    template_name = BASE_TEMPLATE_NAME


class WriteOffReasonListView(ListView):
    model = WriteOffReasonModel
    template_name = BASE_TEMPLATE_NAME
