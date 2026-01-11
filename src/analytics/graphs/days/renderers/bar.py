# 棒グラフの描画
from __future__ import annotations
import matplotlib.pyplot as plt
from ..plot_data import PlotData
from ...types import VerticalAxis

class BarRenderer:
    def render(self, ax, data: PlotData, *, verticalAxis: VerticalAxis) -> None:
        x = list(range(len(data.labels)))
        bottom = [0.0] * len(data.labels)

        # フイールドごとに積み上げ描画
        for field, series in data.values.items():
            ax.bar(
                x,
                series,
                bottom=bottom,
                label=field,
                color=data.colors.get(field),
            )
            bottom = [b + v for b, v in zip(bottom, series)]
        
        # 軸、グリッド
        ax.grid(True)
        ax.set_xlabel('年月日')
        ax.set_ylabel('学習時間（時間）' if verticalAxis == 'time' else '学習時間（%）')

        ax.set_xticks(x)
        ax.set_xticklabels(data.labels, rotation=0, ha='center')

        # Y上限
        ymax_val = max(bottom) if bottom else 0.0
        padding = max(1, ymax_val * 0.1)
        ax.set_ylim(0, ymax_val + padding)

        # 合計値ラベル
        for xi, total in zip(x, bottom):
            if total > 0:
                label = f"{total:.2f}" if verticalAxis == "time" else f"{total:.2f}%"
                ax.text(xi, total, label, ha="center", va="bottom", fontsize=9)

        ax.legend(loc='upper left', bbox_to_anchor=(1.04, 1), edgecolor='black', borderaxespad=0)
