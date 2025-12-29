from django.db import migrations

def fill_event_company_uuid(apps, schema_editor):
    Event = apps.get_model('ams_pk_uuid', 'Event')

    for event in Event.objects.all():
        event.company_uuid = event.company.company_uuid
        event.save()

class Migration(migrations.Migration):

    dependencies = [
        ('ams_pk_uuid', '0004_event_company_uuid'),
    ]

    operations = [
        migrations.RunPython(fill_event_company_uuid),
    ]
