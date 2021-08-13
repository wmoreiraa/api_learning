import databases
import sqlalchemy as _sql
from sqlalchemy.orm import joinedload, relationship
from sqlalchemy.orm.query import Query
from sqlalchemy.sql.schema import ForeignKey

DATABASE_URL = "sqlite:///./test.db"
database = databases.Database(DATABASE_URL)

metadata = _sql.MetaData()

models = _sql.Table(
    "models",
    metadata,
    _sql.Column("mid", _sql.Integer, primary_key=True),
    _sql.Column("model_name", _sql.String),
    _sql.Column("cod_params", _sql.Integer, ForeignKey("params.cod_params")),
)

params = _sql.Table(
    "params",
    metadata,
    _sql.Column("cod_params", _sql.Integer, primary_key=True),
    _sql.Column("n_estimators", _sql.Integer),
    _sql.Column("learning_rate", _sql.Float, nullable=True),
)

engine = _sql.create_engine(DATABASE_URL)

metadata.create_all(engine)
