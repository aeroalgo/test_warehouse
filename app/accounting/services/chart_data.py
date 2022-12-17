from typing import *
from datetime import datetime, timedelta
from typing import Tuple, List, Optional, Dict, Any

from django.db.models import QuerySet
from app.accounting.services.forecast import Forecast
from app.accounting.static_models import LineChart, BarChart


class CreateChartData:

    def __init__(self, datas: QuerySet):
        self.datas = datas
        self.labels = []
        self.line_chart_datas = {}
        self.serialize_line_chart = []

    def get_line_chart(self) -> List[Dict]:
        for data in self.datas:
            if str(data.actual_date) not in self.labels:
                self.labels.append(str(data.actual_date))
            if self.line_chart_datas.get(data.sku.article):
                self.line_chart_datas.get(data.sku.article).data.append(data.count)
            else:
                element = LineChart(label=data.sku.article)
                element.set_color()
                element.data.append(data.count)
                self.line_chart_datas[data.sku.article] = element
        self.serialize_line_chart = [chart.dict() for chart in self.line_chart_datas.values()]
        return self.serialize_line_chart

    def get_bar_chart(self) -> List[Dict]:
        bar_chart_serialize = []
        for key, chart_instance in self.line_chart_datas.items():
            bar_chart = BarChart(label=chart_instance.label, data=chart_instance.data)
            bar_chart.get_procent_data()
            bar_chart_serialize.append(bar_chart.dict())

        return bar_chart_serialize

    def get_forecast_chart(self,
                           data: Dict[str, Any],
                           forecasts: List[Dict[str, Any]]) -> Tuple[List, List[Optional[LineChart]]]:
        min_last_update = datetime.now()
        max_end_date: datetime = forecasts[0].get("last_update")

        for forecast in forecasts:
            if forecast.get("last_update").timestamp() < min_last_update.timestamp():
                min_last_update = forecast.get("last_update")
            if forecast.get("end_date").timestamp() > max_end_date.timestamp():
                max_end_date = forecast.get("end_date")

        chart_instance = {}
        for article, article_data in data.items():
            element = LineChart(label=article)
            element.set_color()
            for count, actual_date in zip(article_data.get("count"), article_data.get("actual_date")):
                if actual_date.timestamp() >= min_last_update.timestamp():
                    element.data.append(count)
            chart_instance[article] = element.dict()

        serialize_chart = []
        for forecast in forecasts:
            chart_instance.get(forecast.get("article")).get("data").extend(forecast.get("results"))
            serialize_chart.append(chart_instance.get(forecast.get("article")))
        labels_chart = [min_last_update]
        while True:
            label = labels_chart[-1] + timedelta(hours=3)
            if label.timestamp() <= max_end_date.timestamp():
                labels_chart.append(label)
            else:
                break

        return [str(label) for label in labels_chart], serialize_chart
