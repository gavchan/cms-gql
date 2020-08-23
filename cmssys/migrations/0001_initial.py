# Generated by Django 3.1 on 2020-08-23 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=0)),
                ('actor', models.CharField(blank=True, max_length=255, null=True)),
                ('class_name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('event_name', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('new_value', models.TextField(blank=True, null=True)),
                ('old_value', models.TextField(blank=True, null=True)),
                ('persisted_object_id', models.CharField(blank=True, max_length=255, null=True)),
                ('persisted_object_version', models.CharField(blank=True, max_length=255, null=True)),
                ('property_name', models.CharField(blank=True, max_length=255, null=True)),
                ('session_id', models.CharField(blank=True, max_length=255, null=True)),
                ('uri', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'audit_log',
                'ordering': ['-last_updated'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CmsUser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('cname', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('medical_council_reg_no', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('password_hash', models.CharField(max_length=255)),
                ('tel', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('ehr_uid', models.CharField(blank=True, max_length=255, null=True)),
                ('priority', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'user',
                'ordering': ['id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(default=0)),
            ],
            options={
                'db_table': 'user_profile',
                'managed': False,
            },
        ),
    ]
