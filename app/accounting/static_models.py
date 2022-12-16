from pydantic import BaseModel, Field
from typing import *


class LineChart(BaseModel):
    """Класс данных для линейного графика"""
    label: str
    data: List[float] = Field(default=[])
    backgroundColor: str = Field(default='transparent')
    borderColor: str = Field(default='rgba(220,53,69,0.75)')
    borderWidth: int = Field(default=3)
    pointStyle: str = Field(default='circle')
    pointRadius: int = Field(default=3)
    pointBorderColor: str = Field(default='transparent')
    pointBackgroundColor: str = Field(default='rgba(220,53,69,0.75)')

    def set_color(self):
        color_magazine = {
            "1000001": "rgba(174, 221, 125, 0.9)",  # Светло зеленый
            "1000002": "rgba(95,222,112, 0.9)",  # Зеленый
            "1000003": "rgba(138, 180, 255, 0.9)",  # Синий
            "1000004": "rgba(168, 228, 252, 0.9)",  # Голубой
        }
        self.borderColor = color_magazine.get(self.label)
        self.pointBackgroundColor = color_magazine.get(self.label)


class BarChart(BaseModel):
    """Класс данных для бар графика"""

    label: str
    data: List[float] = Field(default=[])
    borderColor: str = Field(default="rgba(0, 194, 146, 0.9)")
    borderWidth: int = Field(default=0)
    backgroundColor: str = Field(default='rgba(0, 194, 146, 0.5)')

    def get_procent_data(self):
        for idx in range(1, len(self.data)):
            if self.data[-idx] - self.data[-idx - 1] > 0:
                self.data = [round((self.data[-1] - self.data[-idx]) * 100 / self.data[0], 1)]
                break
        else:
            self.data = [round((self.data[-1] - self.data[0]) * 100 / self.data[0], 1)]
