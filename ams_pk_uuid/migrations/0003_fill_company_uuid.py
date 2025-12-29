from django.db import migrations
import uuid

def fill_company_uuid(apps, schema_editor):
    Company = apps.get_model('ams_pk_uuid', 'Company')
    for company in Company.objects.all():
        company.company_uuid = uuid.uuid4()
        company.save()

class Migration(migrations.Migration):

    dependencies = [
        ('ams_pk_uuid', '0002_company_company_uuid'),
    ]

    operations = [
        migrations.RunPython(fill_company_uuid),
    ]
