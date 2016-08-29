from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
import pkg_resources

Base = declarative_base()


class Feed(Base):
    __tablename__ = 'feed'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)


def session():
    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    resource_package = __name__  # Could be any module/package name.
    resource_path = '/'.join(['data', 'evetide.db'])
    dbfile = pkg_resources.resource_filename(resource_package, resource_path)
    engine = create_engine('sqlite:///%s' % dbfile)

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
