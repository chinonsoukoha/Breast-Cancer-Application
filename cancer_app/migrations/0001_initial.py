# Generated by Django 3.2.5 on 2021-07-05 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_db',
            fields=[
                ('patient_name', models.CharField(max_length=100)),
                ('patient_id', models.CharField(default='1701775', max_length=100, primary_key=True, serialize=False)),
                ('hist_image', models.FileField(blank=True, max_length=254, upload_to=None)),
                ('diagnosis_result', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menopause', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('density', models.CharField(max_length=100)),
                ('bmi', models.CharField(max_length=100)),
                ('agefirst', models.CharField(max_length=100)),
                ('nrelbc', models.CharField(max_length=100)),
                ('brstproc', models.CharField(max_length=100)),
                ('lastmamm', models.CharField(max_length=100)),
                ('surgmeno', models.CharField(max_length=100)),
                ('hrt', models.CharField(max_length=100)),
                ('invasive', models.CharField(max_length=100)),
                ('risk_result', models.CharField(max_length=100)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cancer_app.patient_db')),
            ],
        ),
    ]
