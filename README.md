🟢 PART 0 — Create Model (Normal Way)

What you do

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    discription = models.TextField()


Then

python manage.py makemigrations
python manage.py migrate


What this does

Creates table

Uses integer primary key

Everything works normally

🟢 STEP 1 — Add UUID Field (Preparation)

What you change

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_uuid = models.UUIDField(null=True)
    name = models.CharField(max_length=100)
    discription = models.TextField()


Then

python manage.py makemigrations
python manage.py migrate


What this does

Adds a new UUID column

Old primary key stays

No data is changed

Safe step

🟢 STEP 2 — Fill UUID Values (Data Migration)

What you do

Generate UUID for each row

Save it in company_uuid

Why

UUID must exist before becoming primary key

Result

Every company now has its own UUID

UUID is generated once

🟢 STEP 3 — Copy UUID to Related Tables (Event)

What you do

Add company_uuid field to Event

Copy Company.company_uuid into Event.company_uuid

Why

Event still uses old integer FK

UUID relationship must be saved first

Result

Event now knows company by UUID

Old FK still exists (for now)

🟢 STEP 4 — Remove Old ForeignKey (Event)
❌ OLD
company = models.ForeignKey(Company, on_delete=models.CASCADE)
company_uuid = models.UUIDField(null=True)

✅ NEW
company_uuid = models.UUIDField()


What this does

Removes integer FK

Keeps UUID link

Prepares for PK change

🟢 STEP 5 — Promote UUID to Primary Key (Company)

What you do

class Company(models.Model):
    company_id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    discription = models.TextField()


Important

❌ Do NOT generate new UUID

Use existing values only

Result

UUID becomes primary key

Old integer PK is gone

🟢 STEP 6 — Restore ForeignKey (Final)

What you do

class Event(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


Result

ForeignKey now uses UUID

Relationship restored

Migration complete