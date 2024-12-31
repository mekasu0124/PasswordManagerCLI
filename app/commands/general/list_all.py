from app.utilities.json import JsonEngine

import click


@click.command(name="list")
def list_entries():
    json_engine = JsonEngine()

    all_entries = json_engine.list_all_entries()

    