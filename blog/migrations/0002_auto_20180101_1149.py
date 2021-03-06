# Generated by Django 2.0 on 2018-01-01 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='blurb',
            field=models.TextField(blank=True, help_text='Enter movie blurb', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(help_text='Write your blog post here.', max_length=2000),
        ),
    ]
