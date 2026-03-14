from flask import flash
from sqlalchemy.exc import IntegrityError

from ...extensions import db
from ...models.fields import Field

def upsert_fields_bulk_usecase(user_id: str, form) -> None:
    fieldnames = form.getlist('fieldname[]')
    color_codes = form.getlist('color_code[]')
    field_ids = form.getlist('field_id[]')
    row_actions = form.getlist('row_action[]')
    print(fieldnames, color_codes, field_ids, row_actions)

    is_registered = False
    db_fields = Field.get_fields_all(user_id)
    existing_names = [f.fieldname.lower() for f in db_fields]

    try:
        for fieldname, color_code, field_id, row_action in zip(fieldnames, color_codes, field_ids, row_actions):
            # 登録
            if row_action == 'new' and fieldname.strip():
                if fieldname.strip().lower() in existing_names:
                    flash(f'{fieldname}は既に登録されています', 'エラー')
                else:
                    field = Field(
                        user_id=user_id,
                        fieldname=fieldname,
                        color_code=color_code,
                    )
                    db.session.add(field)
                    is_registered = True
            
            # 編集
            elif row_action == 'update' and fieldname.strip() and field_id:
                field = db.session.get(Field, field_id)
                if field and user_id == user_id:
                    field.fieldname = fieldname
                    field.color_code = color_code
                    is_registered = True
            
            # 削除
            elif row_action == 'delete' and field_id:
                field = db.session.get(Field, field_id)
                if field and user_id == user_id:
                    db.session.delete(field)
                    is_registered = True
        
        db.session.commit()
        if is_registered:
            flash('学習分野の更新に成功しました', '正常')
    
    except IntegrityError:
        db.session.rollback()
        flash('学習分野の更新ができませんでした（重複または制約違反）', 'エラー')
    
    except Exception:
        db.session.rollback()
        flash('予期しないエラーが発生しました', 'エラー')

