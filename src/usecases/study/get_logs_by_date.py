from __future__ import annotations
from ...analytics.db.read import read_by_date
from ...presenters.study.study_log import row_to_dict

def get_logs_by_date_usecase(*, user_id: str, selected_date: str | None) -> dict:
    study_logs = read_by_date(user_id, selected_date)

    if not study_logs:
        return {'studyDicts': study_logs, 'selected_date': selected_date}
    
    study_dicts: list[dict] = []
    for row in study_logs:
        d = row_to_dict(row)
        study_dicts.append(d)
    
    return {'studyDicts': study_dicts, 'selected_date': selected_date}
