from models import Calendar, Interlock
from session import session_scope

def get_calender(seriaNamber, startdDay):
    with session_scope() as session:
        user_id = session.query(Interlock.user_id).filter(Interlock.seriaNamber ==seriaNamber).first()
        print(user_id)
        calendar = session.query(Calendar.id, Calendar.startdDay, Calendar.endDay, Calendar.title,Calendar.content).filter(Calendar.startdDay.like(f"%{startdDay}%"),Calendar.user_id == user_id).first()

        return {
            "start-date": calendar.startDay
            }

calender = get_calender("00000000", "2022-10-06")
print(calender["start-date"])
