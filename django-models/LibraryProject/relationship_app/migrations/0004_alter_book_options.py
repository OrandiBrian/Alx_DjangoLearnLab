# Generated by Django 5.1.6 on 2025-03-09 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0003_alter_userprofile_role'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('relationship_app.can_add_book', 'Can add book'), ('relationship_app.can_change_book', 'Can change book'), ('relationship_app.can_delete_book', 'Can delete book'))},
        ),
    ]
