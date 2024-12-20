from web.database import Base, Session
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Text
from sqlalchemy.sql import func
import streamlit as st


class Workflow(Base):
    __tablename__ = 'workflows'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, index=True)
    owner = Column(String(32))
    experiment_id = Column(Integer)
    dataset_ids = Column(String(4096))
    knowledge_id = Column(Integer)
    create_at = Column(DateTime, default=func.datetime('now', 'localtime'))
    update_at = Column(DateTime, default=func.datetime('now', 'localtime'))

    def __init__(self, **kwargs):
        super(Workflow, self).__init__(**kwargs)

    @staticmethod
    def create_workflow(workflow):
        try:
            session = Session()
            session.add(workflow)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @staticmethod
    def get_workflows_by_owner():
        try:
            session = Session()
            return session.query(Workflow).filter(Workflow.owner == st.session_state.current_username).all()
        except Exception as e:
            raise e
        finally:
            session.close()

    @staticmethod
    def get_workflow_by_id(id):
        try:
            session = Session()
            return session.query(Workflow).filter(Workflow.id == id).first()
        except Exception as e:
            raise e
        finally:
            session.close()

    @staticmethod
    def get_workflow_by_owner_name(name):
        try:
            session = Session()
            return session.query(Workflow).filter(Workflow.owner == st.session_state.current_username,
                                                  Workflow.name == name).first()
        except Exception as e:
            raise e
        finally:
            session.close()


    def __repr__(self):
        return '<Workflow %r>' % self.name

