# Generated by Django 4.1.6 on 2023-04-19 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='approved',
            new_name='Approved',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='approved_by',
            new_name='Approved_by',
        ),
        migrations.CreateModel(
            name='Read',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Score', models.IntegerField()),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.book')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.profile')),
            ],
        ),
    ]
