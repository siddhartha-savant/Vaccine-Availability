from csv import DictReader
from django.core.management.base import BaseCommand
from availability.models import District_Mapping


ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the mapping data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from district_mapping.csv into our district_mapping mode"

    def handle(self, *args, **options):
        if District_Mapping.objects.exists():
            print('District mapping data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Creating mapping data")
        for row in DictReader(open('./district_mapping.csv')):
            dmap = District_Mapping()
            dmap.state_id = row['state_id']
            dmap.district_id = row['district_id']
            dmap.district_name = row['district_name']
            dmap.state_name = row['state_name']
            dmap.save()
