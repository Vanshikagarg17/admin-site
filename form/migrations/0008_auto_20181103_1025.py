# Generated by Django 2.1.2 on 2018-11-03 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('form', '0007_auto_20181005_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='CI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_address', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='ci',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='form.CI'),
        ),
    ]
