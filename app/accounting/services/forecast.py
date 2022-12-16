import numpy as np
from datetime import timedelta


class Forecast:

    def __init__(self, datas):
        self.datas = datas
        self.sku_data = {}

    def get_forecast(self):
        for data in self.datas:
            if data.sku.article not in self.sku_data.keys():
                self.sku_data[data.sku.article] = {"count": [data.count]}
                self.sku_data[data.sku.article].update({"actual_date": [data.actual_date]})
            else:
                self.sku_data[data.sku.article]["count"].append(data.count)
                self.sku_data[data.sku.article]["actual_date"].append(data.actual_date)

        forecasts = []
        for article, article_data in self.sku_data.items():
            count_product = article_data.get("count")
            diffs = []
            for i in range(1, len(count_product)):
                diff = count_product[i - 1] - count_product[i]
                if diff > 0:
                    diffs.append(diff)
            x = np.arange(0, 3)
            y = np.array(diffs[-3:])
            coeffs = np.polyfit(x, y, 1)
            result = count_product[-1] - (coeffs[0] * 2 + coeffs[1])
            count = 1
            results = []
            while result >= 0:
                results.append(round(result))
                result = result - (coeffs[0] * (2 + count) + coeffs[1])
                count += 1
            results.append(result)
            end_date = article_data.get("actual_date")[-1] + timedelta(hours=3 * count)
            sku_forecast = {
                "article": article,
                "count": count_product[-1],
                "last_update": article_data.get("actual_date")[-1],
                "end_date": end_date,
                "results": results
            }
            forecasts.append(sku_forecast)
        return forecasts
