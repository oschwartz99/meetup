# Generated by Django 2.1.7 on 2019-03-31 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0010_auto_20190331_1923'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DebugEvent',
        ),
        migrations.RemoveField(
            model_name='event',
            name='number_going',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('Party', 'Party'), ('Concert', 'Concert'), ('Study', 'Study'), ('Speech', 'Speech'), ('Meal', 'Meal')], max_length=50),
        ),
    ]