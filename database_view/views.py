from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from database_view.forms.client_form import ClientForm
from database_view.forms import DepartmentForm, DiscountCardForm, PositionForm, ProductForm, ProviderForm, SaleForm, \
    WorkerForm, WriteOffReasonForm, WriteOffProductForm, SupplyForm
from database_view.models import ClientModel, DepartmentModel, DiscountCardModel, PositionModel, ProductModel, \
    ProviderModel, SaleModel, WorkerModel, WriteOffProductModel, WriteOffReasonModel, SupplyModel


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
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
    return redirect(reverse('client_list'))


def clients_update(request, pk):
    client = get_object_or_404(ClientModel, pk=pk)
    form = ClientForm(request.POST, instance=client)
    if form.is_valid():
        form.save()
        return redirect(reverse('client_list'))
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
    return redirect(reverse('client_detail', kwargs={'pk': pk}))


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
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
        return redirect(reverse('department_list'))


def department_update(request, pk):
    department = get_object_or_404(DepartmentModel, pk=pk)
    form = DepartmentForm(request.POST, instance=department)
    if form.is_valid():
        form.save()
        return redirect(reverse('department_list'))
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
    return redirect(reverse('department_detail', kwargs={'pk': pk}))


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
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
    return redirect(reverse('discount_card_list'))


def discount_card_update(request, pk):
    card = get_object_or_404(DiscountCardModel, pk=pk)
    form = DiscountCardForm(request.POST, instance=card)
    if form.is_valid():
        form.save()
        return redirect(reverse('discount_card_list'))
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
    return redirect(reverse('discount_card_detail', kwargs={'pk': pk}))


def discount_card_delete(request, pk):
    DiscountCardModel.objects.get(pk=pk).delete()
    return redirect(reverse('discount_card_list'))


class PositionListView(ListView):
    model = PositionModel
    template_name = 'position/position_list.html'
    extra_context = {'create_form': PositionForm()}
    queryset = PositionModel.objects.all().order_by('-position_id')


def position_create(request):
    form = PositionForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('position_list'))
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
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
    if form.is_valid():
        form.save()
        return redirect(reverse('position_list'))
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
    return redirect(reverse('position_detail', kwargs={'pk': pk}))


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
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
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
    if form.is_valid():
        form.save()
        return redirect(reverse('product_list'))
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
    return redirect(reverse('product_detail', kwargs={'pk': pk}))


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
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
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
    if form.is_valid():
        form.save()
        return redirect(reverse('provider_list'))
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
    return redirect(reverse('provider_detail', kwargs={'pk': pk}))


class SaleListView(ListView):
    model = SaleModel
    template_name = 'sale/sale_list.html'
    extra_context = {'create_form': SaleForm()}
    queryset = SaleModel.objects.all().order_by('-sale_id')


def sale_create(request):
    form = SaleForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('sale_list'))
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
    return redirect(reverse('sale_list'))


def sale_delete(request, pk):
    SaleModel.objects.get(pk=pk).delete()
    return redirect(reverse('sale_list'))


class SaleDetailView(DetailView):
    model = SaleModel
    template_name = 'sale/sale_detail.html'
    extra_context = {'update_form': SaleForm()}


def sale_update(request, pk):
    sale = get_object_or_404(SaleModel, pk=pk)
    form = SaleForm(request.POST, instance=sale)
    if form.is_valid():
        form.save()
        return redirect(reverse('sale_list'))
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
    return redirect(reverse('sale_detail', kwargs={'pk': pk}))


class WorkerListView(ListView):
    model = WorkerModel
    template_name = 'worker/worker_list.html'
    extra_context = {'create_form': WorkerForm()}
    queryset = WorkerModel.objects.all().order_by('-worker_id')


def worker_create(request):
    form = WorkerForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('worker_list'))
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
    return redirect(reverse('worker_list'))


def worker_delete(request, pk):
    WorkerModel.objects.get(pk=pk).delete()
    return redirect(reverse('worker_list'))


class WorkerDetailView(DetailView):
    model = WorkerModel
    template_name = 'worker/worker_detail.html'
    extra_context = {'update_form': WorkerForm()}


def worker_update(request, pk):
    worker = get_object_or_404(WorkerModel, pk=pk)
    form = WorkerForm(request.POST, instance=worker)
    if form.is_valid():
        form.save()
        return redirect(reverse('worker_list'))
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
    return redirect(reverse('worker_detail', kwargs={'pk': pk}))


class WriteOffReasonListView(ListView):
    model = WriteOffReasonModel
    template_name = 'write_off_reason/write_off_reason_list.html'
    extra_context = {'create_form': WriteOffReasonForm()}
    queryset = WriteOffReasonModel.objects.all().order_by('-reason_id')


def write_off_reason_create(request):
    form = WriteOffReasonForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect(reverse('write_off_reason_list'))


def write_off_reason_delete(request, pk):
    WriteOffReasonModel.objects.get(pk=pk).delete()
    return redirect(reverse('write_off_reason_list'))


class WriteOffReasonDetailView(DetailView):
    model = WriteOffReasonModel
    template_name = 'write_off_reason/write_off_reason_detail.html'
    extra_context = {'update_form': WriteOffReasonForm()}


def write_off_reason_update(request, pk):
    reason = get_object_or_404(WriteOffReasonModel, pk=pk)
    form = WriteOffReasonForm(request.POST, instance=reason)
    form.save()
    return redirect(reverse('write_off_reason_list'))


class WriteOffProductListView(ListView):
    model = WriteOffProductModel
    template_name = 'write_off_product/write_off_product_list.html'
    extra_context = {'create_form': WriteOffProductForm}
    queryset = WriteOffProductModel.objects.all().order_by('-write_off_product_id')


def write_off_product_create(request):
    form = WriteOffProductForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('write_off_product_list'))
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
    return redirect(reverse('write_off_product_list'))


def write_off_product_delete(request, pk):
    WriteOffProductModel.objects.get(pk=pk).delete()
    return redirect(reverse('write_off_product_list'))


class WriteOffProductDetailView(DetailView):
    model = WriteOffProductModel
    template_name = 'write_off_product/write_off_product_detail.html'
    extra_context = {'update_form': WriteOffProductForm()}


def write_off_product_update(request, pk):
    product = get_object_or_404(WriteOffProductModel, pk=pk)
    form = WriteOffProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect(reverse('write_off_product_list'))
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
    return redirect(reverse('write_off_product_detail', kwargs={'pk': pk}))


class SupplyListView(ListView):
    model = SupplyModel
    template_name = 'supply/supply_list.html'
    extra_context = {'create_form': SupplyForm()}
    queryset = SupplyModel.objects.all().order_by('-supply_id')


class SupplyDetailView(DetailView):
    model = SupplyModel
    template_name = 'supply/supply_detail.html'
    extra_context = {'update_form': SupplyForm()}


def supply_create(request):
    form = SupplyForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('supply_list'))
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
    return redirect(reverse('supply_list'))


def supply_delete(request, pk):
    SupplyModel.objects.get(pk=pk).delete()
    return redirect(reverse('supply_list'))


def supply_update(request, pk):
    supply = get_object_or_404(SupplyModel, pk=pk)
    form = SupplyForm(request.POST, instance=supply)
    if form.is_valid():
        form.save()
        return redirect(reverse('supply_list'))
    for error in form.errors:
        messages.add_message(request, messages.ERROR, form.errors.get(error))
    return redirect(reverse('supply_detail', kwargs={'pk': pk}))
