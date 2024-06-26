# Generated by Django 4.2.1 on 2024-04-04 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gpa_app', '0006_alter_student_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='user_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecturer_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
