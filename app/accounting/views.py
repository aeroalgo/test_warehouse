from django.http import HttpResponseRedirect
from django.shortcuts import render

from app.accounting.forms import StorageForm
from app.accounting.models import Storage, Product
from app.accounting.services.chart_data import CreateChartData
from app.accounting.services.forecast import Forecast


def sku(request):
    if request.method == "POST":
        sku_id = request.POST.get("sku")
        sku = Product.objects.get(id=sku_id)
        form = StorageForm(request.POST)
        if form.is_valid():
            obj = Storage.objects.filter(sku_id=sku.id).last()
            new_obj = Storage()
            new_obj.sku = sku
            new_obj.count = form.cleaned_data['count'] + obj.count
            new_obj.save()
            return HttpResponseRedirect('/sku')

    datas = Storage.objects.all().select_related("sku")
    data = CreateChartData(datas=datas)
    line_chart = data.get_line_chart()
    bar_chart = data.get_bar_chart()
    instance = Forecast(datas=datas)
    forecasts = instance.get_forecast()
    forecast_labels, forecast_chart = data.get_forecast_chart(instance.sku_data, forecasts)
    labels = data.labels
    return render(request, "product_item.html", context={
        "request": request, "labels": labels, "chart_data": line_chart, "bar_chart": bar_chart,
        "forecasts": forecasts, "forecast_labels": forecast_labels, "forecast_chart": forecast_chart,
    })
