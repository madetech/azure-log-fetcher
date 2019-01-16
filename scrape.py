#!/usr/bin/env python
import os


from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity


try:
    from dotenv import load_dotenv
except ImportError:
    pass
else:
    load_dotenv()


OUTPUT_TEMPLATE = """
name: {log_entry.RenderedMessage}
time: {log_entry.Timestamp}

{log_entry.Exception}
"""


def default_table_name(log_env: str) -> str:
    assert log_env
    return log_env + 'informationlogs'


CONFIG = {
    'ACCOUNT': os.getenv('COSMOSDB_ACCOUNT'),
    'KEY': os.getenv('COSMOSDB_KEY'),
    'TABLE': os.getenv('LOG_TABLE', default_table_name(os.environ['LOG_ENV'])),
}


def check_config(config):
    assert config['ACCOUNT']
    assert config['TABLE']
    assert config['KEY']


def get_service(config) -> TableService:
    check_config(config)
    return TableService(
        account_name=config['ACCOUNT'],
        account_key=config['KEY'],
    )


def get_log_entries(service: TableService, table_name, num_results=10):
    yield from service.query_entities(table_name, num_results=num_results)


def write_log_entry(log_entry):
    print(OUTPUT_TEMPLATE.format(log_entry=log_entry))



def main():
    service = get_service(CONFIG)
    for log_entry in reversed(list(get_log_entries(service, CONFIG['TABLE']))):
        write_log_entry(log_entry)



if __name__ == '__main__':
    main()
