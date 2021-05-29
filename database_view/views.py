from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from database_view.forms.client_form import ClientForm
from database_view.models import ClientModel, DepartmentModel, DiscountCardModel, PositionModel, ProductModel, \
    ProviderModel, SaleModel, WorkerModel, WriteOffProductModel, WriteOffReasonModel

BASE_TEMPLATE_NAME = 'base_template.html'


def index(request):
    return render(request, 'menu.html')


class ClientListView(ListView):
    model = ClientModel
    template_name = BASE_TEMPLATE_NAME
    extra_context = {'create_form': ClientForm()}
    queryset = ClientModel.objects.all().order_by('client_id')


class ClientDetailView(DetailView):
    model = ClientModel
    template_name = 'clientmodel_detail.html'
    extra_context = {'update_form': ClientForm()}


def clients_delete(request, pk):
    client = ClientModel.objects.get(pk=pk)
    client.delete()
    return redirect(reverse('client_list'))


def clients_create(request):
    form = ClientForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect(reverse('client_list'))


def clients_update(request, pk):
    client = get_object_or_404(ClientModel, pk=pk)
    print(client)
    form = ClientForm(request.POST, instance=client)
    form.save()
    return redirect(reverse('client_list'))


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
