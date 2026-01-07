from __future__ import annotations
from collections import defaultdict
from datetime import date
import calendar

from ...models.studyLogs import StudyLog
from ...presenters.study.study_log import row_to_dict
from ...analytics.db.read import read_by_month

def get_logs_by_month_usecase(*, user_id: str, selected_date: str | None) -> dict:
    if not selected_date:
        return {'selectedDate': selected_date, 'studyDicts': {}}
    
    year, month = map(int, selected_date.split('-'))
    first_day = date(year, month, 1)
    month_num = calendar.monthrange(year, month)[1]
    last_day = date(year, month, month_num)
    study_logs = read_by_month(user_id, first_day, last_day)

    study_dicts: dict[str, list[dict]] = defaultdict(list)
    for row in study_logs:
        d = row_to_dict(row)
        study_dicts[d['study_date']].append(d)

    return {'selectedDate': selected_date, 'studyDicts': study_dicts}

