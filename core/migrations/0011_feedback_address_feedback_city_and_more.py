from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_simplify_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='feedback',
            name='city',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='feedback',
            name='state',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='feedback',
            name='pincode',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
