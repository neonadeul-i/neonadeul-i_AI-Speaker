from models import Interlock
from session import session_scope

# 일련번호를 받아서 해당 테이블 삭제
def delete_peristalsis(seriaNamber):
    with session_scope() as session:

        ai = session.query(Interlock).filter(Interlock.seriaNamber == seriaNamber).first()

        session.delet(ai)

        return {"삭제 완료"}