import pytest
import typing as T

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from project.scripts.generate import AircraftGenerator


def test_db_row_counts(session, gen):

    assert gen.config.db_url
    # gen is already populated

    gen.to_sql(session=session, db_url=gen.config.db_url)
    # assert that at least some elements are in the tables
    count_query = 'SELECT COUNT(*) FROM "%s".%s'  # "schema".table

    print(gen.config)
    for k, v in gen.state.items():
        if getattr(v[0], "__mapper__", False):
            schema = v[0].__table__.schema
            table = v[0].__table__.name
            count = session.execute(count_query % (schema, table)).first()
            print(count[0], len(v), v[0].__class__)

            assert count[0] == len(v)


def test_db_row_counts_with_noisy_data(session, gen_noisy):
    "This test aims to detect if noisy data is aligned with SQL tables"
    assert gen_noisy.config.db_url
    # gen_noisy is already populated

    gen_noisy.to_sql(session=session, db_url=gen_noisy.config.db_url)
    # assert that at least some elements are in the tables
    count_query = 'SELECT COUNT(*) FROM "%s".%s'  # "schema".table

    print(gen_noisy.config)
    for k, v in gen_noisy.state.items():
        if getattr(v[0], "__mapper__", False):
            schema = v[0].__table__.schema
            table = v[0].__table__.name
            count = session.execute(count_query % (schema, table)).first()
            print(count[0], len(v), v[0].__class__)

            assert count[0] == len(v)


def test_db_row_counts_with_bad_data(session, gen_bad):
    "This test aims to detect if bad data is aligned with SQL tables"
    assert gen_bad.config.db_url
    # gen_bad is already populated

    gen_bad.to_sql(session=session, db_url=gen_bad.config.db_url)
    # assert that at least some elements are in the tables
    count_query = 'SELECT COUNT(*) FROM "%s".%s'  # "schema".table

    print(gen_bad.config)
    for k, v in gen_bad.state.items():
        if getattr(v[0], "__mapper__", False):
            schema = v[0].__table__.schema
            table = v[0].__table__.name
            count = session.execute(count_query % (schema, table)).first()
            print(count[0], len(v), v[0].__class__)

            assert count[0] == len(v)


#     result = sess(
#         """
# select
#   *
# from
#   pg_catalog.pg_tables
# where
#   schemaname != 'information_schema'
#   and schemaname != 'pg_catalog';"""
#     )

#     for _r in result:
#         print(_r)

