from session import session_scope
from models import Senior, User

def create_helper(id, period, pay, record):
    with session_scope() as session:
        new_calendar = Senior(
            user_id=id,
            period=period,
            pay=pay,
            record=record
        )

        session.add(new_calendar)
        session.commit()

        return {
                   "message": "success"
               }, 201