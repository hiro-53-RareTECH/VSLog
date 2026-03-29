# グラフ描画のエントリーポイント
from __future__ import annotations
from ...types import GraphType
from .bar import BarRenderer
from .pie import PieRenderer
from .line import LineRenderer
from .base import DaysRenderer

def get_renderer(graphType: GraphType) -> DaysRenderer:
    if graphType == 'bar':
        return BarRenderer()
    if graphType == 'pie':
        return PieRenderer()
    if graphType == 'line':
        return LineRenderer()
    raise ValueError(f'invalid graphType: {graphType}')