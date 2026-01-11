# 円グラフの描画
from __future__ import annotations
from ..plot_data import PlotData
from ...types import VerticalAxis
import matplotlib.pyplot as plt

class PieRenderer:
    def render(self, ax, data: PlotData, *, verticalAxis: VerticalAxis) -> None:
        date_len = len(data.labels)
        totals = [0.0] * date_len

        for series in data.values.values():
            for i, v in enumerate(series):
                totals[i] += float(v)

        filtered = [(label, total) for label, total in zip(data.labels, totals) if total > 0]
        filtered_labels = [label for label, _ in filtered]
        filtered_totals = [total for _, total in filtered]

        cmap = plt.get_cmap('tab20')
        colors = [cmap(i % cmap.N) for i in range(len(filtered_totals))]

        def format_value(pct: float, allvalues: list[float]) -> str:
            total = sum(allvalues)
            value = pct / 100.0 * total
            if verticalAxis == 'time':
                return f'{value:.2f}時間'
            return f'{pct:.2f}%'

        wedges, texts, autotexts = ax.pie(
            x=filtered_totals,
            labels=filtered_labels,
            colors=colors,
            counterclock=False,
            startangle=90,
            autopct=lambda pct: format_value(pct, filtered_totals),
        )

        ax.axis('equal')
        ax.legend(wedges, data.labels, loc='upper left', bbox_to_anchor=(0.8, 1), edgecolor='black', borderaxespad=0)
