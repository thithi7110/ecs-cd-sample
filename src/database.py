from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infra.repository.models import mapper_registry

SQLALCHEMY_DATABASE_URI = 'sqlite:///tasks.db'


class DatabaseContext:
    def initialize(self):

        engine = create_engine(
            SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False}, echo=True
        )

        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=engine)
        
        #初回時のみ実施する
        Base = mapper_registry.generate_base()
        Base.metadata.create_all(bind=engine)


database_context = DatabaseContext()


def get_db():
    """
    Get database

    Yields:
        SessionLocal: Local session for database connection
    """
    db = database_context.SessionLocal()
    try:
        yield db
    finally:
        db.close()