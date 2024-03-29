# Generated by Django 2.2.5 on 2019-10-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('enable', models.BooleanField(default=True)),
                ('x_consumer_id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('x_consumer_custom_id', models.CharField(max_length=256, null=True)),
                ('x_consumer_username', models.CharField(max_length=256, null=True)),
                ('x_authenticated_scope', models.CharField(max_length=256, null=True)),
                ('x_authenticated_userid', models.PositiveIntegerField(null=True)),
                ('x_anonymous_consumer', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]
