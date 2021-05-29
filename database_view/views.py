from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from database_view.forms.client_form import ClientForm
from database_view.forms import DepartmentForm, DiscountCardForm, PositionForm, ProductForm, ProviderForm
from database_view.models import ClientModel, DepartmentModel, DiscountCardModel, PositionModel, ProductModel, \
    ProviderModel, SaleModel, WorkerModel, WriteOffProductModel, WriteOffReasonModel


def index(request):
    return render(request, 'menu.html')


class ClientListView(ListView):
    model = ClientModel
    template_name = 'client/clientmodel_list.html'
    extra_context = {'create_form': ClientForm()}
    queryset = ClientModel.objects.all().order_by('-client_id')


class ClientDetailView(DetailView):
    model = ClientModel
    template_name = 'client/clientmodel_detail.html'
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
    form = ClientForm(request.POST, instance=client)
    form.save()
    return redirect(reverse('client_list'))


class DepartmentListView(ListView):
    model = DepartmentModel
    template_name = 'department/departmentmodel_list.html'
    extra_context = {'create_form': DepartmentForm()}
    queryset = DepartmentModel.objects.all().order_by('-department_id')


class DepartmentDetailView(DetailView):
    model = DepartmentModel
    template_name = 'department/departmentmodel_detail.html'
    extra_context = {'update_form': DepartmentForm()}


def department_delete(request, pk):
    department = DepartmentModel.objects.get(pk=pk)
    department.delete()
    return redirect(reverse('department_list'))


def department_create(request):
    form = DepartmentForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect(reverse('department_list'))


def department_update(request, pk):
    department = get_object_or_404(DepartmentModel, pk=pk)
    form = DepartmentForm(request.POST, instance=department)
    form.save()
    return redirect(reverse('department_list'))


class DiscountCardListView(ListView):
    model = DiscountCardModel
    template_name = 'discount_card/discountcardmodel_list.html'
    extra_context = {'create_form': DiscountCardForm()}
    queryset = DiscountCardModel.objects.all().order_by('-card_id')


class DiscountCardDetailView(DetailView):
    model = DiscountCardModel
    template_name = 'discount_card/discountcardmodel_detail.html'
    extra_context = {'update_form': DiscountCardForm()}


def discount_card_create(request):
    form = DiscountCardForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect(reverse('discount_card_list'))


def discount_card_update(request, pk):
    card = get_object_or_404(DiscountCardModel, pk=pk)
    form = DiscountCardForm(request.POST, instance=card)
    form.save()
    return redirect(reverse('discount_card_list'))


def discount_card_delete(request, pk):
    DiscountCardModel.objects.get(pk=pk).delete()
    return redirect(reverse('discount_card_list'))


class PositionListView(ListView):
    model = PositionModel
    template_name = 'position/position_list.html'
    extra_context = {'create_form': PositionForm()}
    queryset = PositionModel.objects.all().order_by('-position_id')


def discount_card_create(request):
    form = PositionForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect(reverse('position_list'))


def position_delete(request, pk):
    PositionModel.objects.get(pk=pk).delete()
    return redirect(reverse('position_list'))


class PositionDetailView(DetailView):
    model = PositionModel
    template_name = 'position/position_detail.html'
    extra_context = {'update_form': PositionForm()}


def position_update(request, pk):
    position = get_object_or_404(PositionModel, pk=pk)
    form = PositionForm(request.POST, instance=position)
    form.save()
    return redirect(reverse('position_list'))


class ProductListView(ListView):
    model = ProductModel
    template_name = 'product/product_list.html'
    extra_context = {'create_form': ProductForm()}
    queryset = ProductModel.objects.all().order_by('-product_id')


def product_create(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect(reverse('product_list'))


def product_delete(request, pk):
    ProductModel.objects.get(pk=pk).delete()
    return redirect(reverse('product_list'))


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'product/product_detail.html'
    extra_context = {'update_form': ProductForm()}


def product_update(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    form = ProductForm(request.POST, instance=product)
    form.save()
    return redirect(reverse('product_list'))


class ProviderListView(ListView):
    model = ProviderModel
    template_name = 'provider/provider_list.html'
    extra_context = {'create_form': ProviderForm()}
    queryset = ProviderModel.objects.all().order_by('-provider_id')


def provider_create(request):
    form = ProviderForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect(reverse('provider_list'))


def provider_delete(request, pk):
    ProviderModel.objects.get(pk=pk).delete()
    return redirect(reverse('provider_list'))


class ProviderDetailView(DetailView):
    model = ProviderModel
    template_name = 'provider/provider_detail.html'
    extra_context = {'update_form': ProviderForm()}


def provider_update(request, pk):
    provider = get_object_or_404(ProviderModel, pk=pk)
    form = ProviderForm(request.POST, instance=provider)
    form.save()
    return redirect(reverse('provider_list'))