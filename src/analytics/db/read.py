# StudyLogの読み込み用のクエリ
from __future__ import annotations

from datetime import date, datetime

from ....extensions import db
from ....models import Field
from ....models import StudyLog

# 共通のフィルター条件
def _build_filters(user_id: str, first_day: date | None = None, last_day: date | None = None):
    filters = [StudyLog.user_id == user_id]
    if first_day:
        filters.append(StudyLog.study_date >= first_day)
    if last_day:
        filters.append(StudyLog.study_date <= last_day)
    return filters

# ユーザー毎の全学習履歴取得
def read_all(user_id: str):
    return StudyLog.query.filter_by(user_id=user_id).all()

# 学習日に応じたユーザー毎の学習履歴取得
def read_by_date(user_id: str, date: str):
    study_date = datetime.strptime(date, "%Y-%m-%d").date()
    logs = (
        db.session.query(StudyLog.study_log_id, StudyLog.study_date, Field.fieldname.label('fieldname'), StudyLog.content, StudyLog.hour)
        .join(Field, StudyLog.field_id == Field.field_id)
        .filter(
        StudyLog.user_id == user_id,
        StudyLog.study_date == study_date
        )
        .all()
    )
    return logs

# 月に応じたユーザー毎の学習履歴取得
def read_by_month(user_id: str, first_day: date, last_day: date):
    filters = _build_filters(user_id, first_day, last_day)
    logs = (
        db.session.query(StudyLog.study_log_id, StudyLog.study_date, Field.fieldname.label('fieldname'), StudyLog.content, StudyLog.hour)
        .join(Field, StudyLog.field_id == Field.field_id)
        .filter(*filters)
        .all()
    )
    return logs
