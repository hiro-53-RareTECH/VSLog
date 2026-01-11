# Plotデータの生成ファイル
from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence
from ..types import VerticalAxis
import platform
from datetime import datetime, date, timedelta

@dataclass(frozen=True)
class PlotData:
    labels: list[str]
    values: dict[str, list[float]]
    colors: dict[str, str]

def build_plot_data(logs: Sequence[tuple[str, str, str, float | None]], *, period: str, verticalAxis: VerticalAxis, first_day=None, last_day=None, year=None, month=None, month_num=None,) -> PlotData:
    # x, height
    def make_xaxis(period, logs, first_day, year) -> tuple[list[str], dict[str, int]]:
        if period in ('this_week', 'last_week', 'month'):
            date_num = month_num or 7
            date_format = '%#m/%#d(%a)' if platform.system() == 'Windows' else '%-m/%-d(%a)'
            axis_keys = [first_day + timedelta(days=i) for i in range(date_num)]
            labels = [d.strftime(date_format) for d in axis_keys]
            index_map = {d: i for i, d in enumerate(axis_keys)}
            return labels, index_map
        if period == 'year':
            date_num = 12
            date_format = '%#Y/%#m' if platform.system() == 'Windows' else '%Y/%-m'
            axis_keys = [f'{m:02d}' for m in range(1, date_num + 1)]
            labels = [date(year, int(m), 1).strftime(date_format) for m in range(1, date_num + 1)]
            index_map = {d: i for i, d in enumerate(axis_keys)}
            return labels, index_map
        if period == 'all':
            axis_keys = sorted(set([selected_date for selected_date, _, _, _ in logs]))
            labels = axis_keys
            index_map = {d: i for i, d in enumerate(axis_keys)}
            return labels, index_map
        raise ValueError(f"Unsupported period: {period}")

    labels, index_map = make_xaxis(period, logs, first_day, year)

    # valuesの初期データの設定
    date_len = len(labels)
    fieldnames = sorted({fieldname for _, fieldname, _, _ in logs})
    values = {f: [0.0] * date_len for f in fieldnames}

    # 日付ごとの合計時間（percent計算用）
    total_by_date = [0.0] * date_len

    # 全期間合計
    total_all = 0.0

    # 1周目：時間を集計
    for selected_date, field, _, hour in logs:
        idx = index_map[selected_date]
        h = float(hour or 0.0)
        values[field][idx] += h
        total_all += h

    # 2周目：percentに変換
    if verticalAxis == 'percent':
        if total_all > 0:
            for field in fieldnames:
                for i in range(date_len):
                    values[field][i] = values[field][i] / total_all * 100
        else:
            for field in fieldnames:
                for i in range(date_len):
                    values[field][i] = 0.0

    # color
    colors = {fieldname: color for _, fieldname, color, _ in logs}

    return PlotData(labels=labels, values=values, colors=colors)
