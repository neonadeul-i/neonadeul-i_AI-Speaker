from models import Notice
from session import session_scope 

def get_notice(id):
    with session_scope() as session:
        notice = session.query(Notice.content).filter(Notice.seriaNumber == id).first()
        return {
                "content": notice.content
        }

