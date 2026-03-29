from __future__ import annotations
from ..plot_data import PlotData
from ...types import VerticalAxis

class LineRenderer:
    def render(self, ax, data: PlotData, *, verticalAxis: VerticalAxis ) -> None:
        x = list(range(len(data.labels)))

        for field, series in data.values.items():
            ax.plot(
                x,
                series,
                label=field,
                color=data.colors.get(field),
                marker='o',
            )

        ax.set_xticks(x)
        if len(data.labels) <= 12:
            ax.set_xticklabels(data.labels, rotation=0, ha='center')
        else:
            ax.set_xticklabels(data.labels, rotation=270, ha='center')

        if verticalAxis == 'time':
            ax.set_ylabel('時間')
        else:
            ax.set_ylabel('%')
        
        ax.grid(True)
        ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1.0), borderaxespad=0)
