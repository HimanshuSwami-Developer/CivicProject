from django.db import migrations, models


def forwards(apps, schema_editor):
    Feedback = apps.get_model("core", "Feedback")
    Feedback.objects.filter(type="suggestion").update(type="feedback")
    Feedback.objects.filter(status="closed").update(status="pending")


def backwards(apps, schema_editor):
    Feedback = apps.get_model("core", "Feedback")
    Feedback.objects.filter(type="feedback").update(type="suggestion")


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='response',
            new_name='remark',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='category',
        ),
        migrations.RunPython(forwards, backwards),
        migrations.AlterField(
            model_name='feedback',
            name='type',
            field=models.CharField(choices=[('feedback', 'Feedback'), ('complaint', 'Complaint')], max_length=20),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('resolved', 'Resolved')], default='pending', max_length=20),
        ),
    ]
