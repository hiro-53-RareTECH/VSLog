from flask import jsonify, request
from flask_login import login_required, current_user

from .. import study_bp
from ....usecases.study.get_graph_stats import get_graph_stats_usecase

# グラフ、統計値の取得
@study_bp.route('/graph/<user_id>', methods=['POST'])
@login_required
def get_graph_stats(user_id :str):
    if user_id != str(current_user.user_id):
        return jsonify({'error': 'forbidden'}), 403
    
    data = request.get_json(silent=True) or {}
    graph_stats_result = get_graph_stats_usecase(
        user_id=user_id,
        period=data.get('period'),
        year=data.get('year'),
        month_year=data.get('month-year'),
        month=data.get('month'),
        horizontalAxis=data.get('horizontalAxis'),
        verticalAxis=data.get('verticalAxis'),
        graphType=data.get('graphType')
        )
    svg = graph_stats_result.svg
    total_day = graph_stats_result.total_day
    total_hour = graph_stats_result.total_hour
    avg_hour = graph_stats_result.avg_hour
    
    return jsonify({
        'svg': svg,
        'total_day': total_day,
        'total_hour': total_hour,
        'avg_hour': avg_hour,
    })
