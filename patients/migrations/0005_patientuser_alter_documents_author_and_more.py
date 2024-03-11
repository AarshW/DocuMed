# Generated by Django 5.0.3 on 2024-03-10 10:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_documents_author_medication_file'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='documents',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patientuser'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patientuser'),
        ),
    ]
