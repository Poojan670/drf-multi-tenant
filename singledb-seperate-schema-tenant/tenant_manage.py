#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seperate_schema.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    from django.db import connection

    args = sys.argv
    schema = args[1]

    with connection.cursor() as cursor:
        cursor.execute(f"SET search_path to {schema}")
        del args[1]
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
