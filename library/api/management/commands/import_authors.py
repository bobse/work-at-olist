from django.core.management.base import BaseCommand, CommandError
from api.models import Author
import csv


class Command(BaseCommand):
    help = 'Import authors from a csv file into the DB'

    def add_arguments(self, parser):
        parser.add_argument('file', type = str, help = 'Csv file to import from')

    def handle(self, *args, **kwargs):
        file = kwargs.get('file')
        try:
            with open(file) as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',')
                # skipping header in csv file
                next(csv_reader)
                authors = [Author(name=author[0]) for author in csv_reader]
                Author.objects.bulk_create(authors)
                print(f"Total of {len(authors)} authors imported into the database.")
        except Exception:
            raise CommandError(f"There was an error while importing {file}")
