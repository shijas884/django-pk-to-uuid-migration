Below is a **very clear, step-by-step README**, where **each step is separated and explained simply**.
No fancy words. Short lines. Easy for beginners to follow.

You can **copy-paste this directly**.

---

# Django Integer Primary Key to UUID – Step by Step

This guide explains **how to change Django primary keys from Integer to UUID**
**when data already exists** and **cannot be deleted**.

Follow the steps **in order**.
Do not skip any step.

---

## Step 0 – Create models normally

Start with normal Django models.

```python
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
```

Run:

```bash
python manage.py makemigrations
python manage.py migrate
```

Data exists in the database.

---

## Step 1 – Add UUID field (do NOT remove anything)

Add a UUID field to the main table.

```python
company_uuid = models.UUIDField(null=True)
```

Run migrations.

What happens:

* Old integer primary key stays
* UUID column is added
* No data changes

---

## Step 2 – Fill UUID values (data migration)

Create a custom migration to generate UUIDs.

What happens:

* Each row gets one UUID
* UUID is saved in the database
* UUID is generated only once

Important:

* Do NOT remove primary key
* Do NOT touch ForeignKeys

---

## Step 3 – Copy UUID to related tables

Add a UUID field to related tables (like `Event`).

```python
company_uuid = models.UUIDField(null=True)
```

Copy UUID from parent table.

What happens:

* Relation is preserved
* Child table now knows parent UUID
* Old ForeignKey still exists

---

## Step 4 – Remove old ForeignKey

Remove the integer ForeignKey from the related table.

```python
# remove ForeignKey field
```

What happens:

* Integer relation is removed
* UUID relation remains
* Safe to change primary key

---

## Step 5 – Make UUID the Primary Key

Remove the old integer primary key.

Make UUID the new primary key.

```python
company_id = models.UUIDField(primary_key=True)
```

Important:

* Do NOT generate new UUID
* Use existing UUID values only

---

## Step 6 – Add ForeignKey again (final step)

Add ForeignKey back to related tables.

```python
company = models.ForeignKey(Company, on_delete=models.CASCADE)
```

What happens:

* ForeignKey now uses UUID
* Relations are restored
* Migration is complete

---

## Final result

* UUID is the primary key
* All relations are correct
* No data loss
* Safe migration

---

## Important rules

* Never change PK directly
* Never use default value for UUID ForeignKey
* Always use `null=True` first
* Always follow step order

---

## Key lesson

**UUID migration is about data safety, not speed.**


