# 年月日別グラフ描画の型定義
from __future__ import annotations
from typing import Protocol
from ..plot_data import PlotData
from ...types import VerticalAxis

class DaysRenderer(Protocol):
    def render(self, ax, data: PlotData, *, verticalAxis: VerticalAxis) -> None:
        ...
