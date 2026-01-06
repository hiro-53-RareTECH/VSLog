from __future__ import annotations
from datetime import datetime

from flask import flash
from flask_login import current_user
from sqlalchemy.exe import IntegrityError

from ...extensions import db
from ...models.fields import Field
from ...models.studyLogs import StudyLog

def upsert_logs_bulk_usecase(*, user_id: str, form) -> dict:
    study_dates = form.getlist('study_dates[]')
    hours = form.getlist('hours[]')
    fieldnames = form.getlist('fieldnames[]')
    contents = form.getlist('contents[]')
    study_log_ids = form.getlist('study_log_ids[]')
    row_actions = form.getlist('row_actions[]')
    
    selected_date = ''.join(set(study_dates))
    is_registered = False

    try:
        for study_date, hour, fieldname, content, study_log_id, row_action in zip(study_dates, hours, fieldnames, contents, study_log_ids, row_actions):
            study_date_obj = datetime.strptime(study_date, '%Y-%m-%d').date() if study_date else None

            # 分野未登録チェック
            if fieldname.strip() and fieldname.strip() not in [f.fieldname for f in current_user.fields]:
                flash(f'{fieldname.strip()}が登録されていません。先に学習分野の登録をお願いします。', 'エラー')
                continue

            # 登録
            if row_action == 'new' and study_date_obj and hour and fieldname.strip():
                study_log = StudyLog(
                    user_id=user_id,
                    field_id=Field.get_field_id(user_id, fieldname),
                    study_date=study_date_obj,
                    hour=hour,
                    content=content,
                )
                db.session.add(study_log)
                is_registered = True
            
            # 編集
            elif row_action == 'update' and study_log_id:
                study_log = StudyLog.query.get(study_log_id)
                if study_log and study_log.user_id == user_id:
                    study_log.field_id = Field.get_field_id(user_id, fieldname)
                    study_log.study_date = study_date_obj
                    study_log.hour = hour
                    study_log.content = content
                    is_registered = True
            
            # 削除
            elif row_action == 'delete' and study_log_id:
                study_log = StudyLog.query.get(study_log_id)
                if study_log and study_log.user_id == user_id:
                    db.session.delete(study_log)
                    is_registered = True
        
        db.session.commit()
        if is_registered:
            flash('学習記録の更新が完了しました', '正常')

    except IntegrityError:
        db.session.rollback()
        flash('学習記録の更新ができませんでした（重複または制約違反）', 'エラー')
    
    except Exception:
        db.session.rollback()
        flash('予期しないエラーが発生しました', 'エラー')
    
    finally:
        db.session.close()
    
    return {'selected_data': selected_date}
