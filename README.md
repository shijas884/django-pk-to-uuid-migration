🟢 PART 0: FIRST —>CREATE THE MODEL (NORMAL WAY)

This is how every Django project starts.

Example: Company model (initial)
from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    discription = models.TextField()

then migrate

-------------------------------------------------------------------------

🟢 STEP 1: Modify the model (ADD ONE FIELD)
import uuid
from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)   # keep this
    company_uuid = models.UUIDField(null=True)        # 👈 NEW FIELD
    name = models.CharField(max_length=100)
    discription = models.TextField()
    
(the full model-code ams_pk_uuid.models )

Important:
    Old PK stays
    New UUID field is empty
    Nothing breaks

-------------------------------------------------------------------
🟢 Step 2 – Populate UUID Values (Data Migration)
Objective

After adding a temporary UUID column in Step 1, all existing records contain NULL values in that column.
This step generates and stores a unique UUID for each existing row.
These UUIDs will later be promoted to primary keys.

___________________________________________________________________________
Step 3 – Propagate UUIDs to Related Tables (Foreign Keys)
Objective

After generating UUIDs for the primary table (Company) in Step 2, related tables still reference the old integer primary key.
This step copies the generated UUID values into related tables so relationships remain intact when the primary key is switched.
_________________________________________________________________________________
STEP 4.1 – Modify Event model
❌ OLD Event model
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_uuid = models.UUIDField(null=True)
    title = models.CharField(max_length=100)

✅ NEW Event model (remove FK)
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    company_uuid = models.UUIDField()   # now NOT NULL
    title = models.CharField(max_length=100)
