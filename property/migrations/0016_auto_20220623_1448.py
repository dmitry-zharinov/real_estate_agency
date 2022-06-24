# Generated by Django 2.2.24 on 2022-06-23 11:48

from django.db import migrations


def fill_owners_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owner, created = Owner.objects.get_or_create(
            owner=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone)
        owner.owner_flats.set([flat.id])


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20220623_1416'),
    ]

    operations = [
        migrations.RunPython(fill_owners_flats)
    ]
