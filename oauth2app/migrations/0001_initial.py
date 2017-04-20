# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 10:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import oauth2app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=255, unique=True)),
                ('label', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('ttl', models.BigIntegerField(blank=True, help_text='Number of seconds before this scope is removed from an access token.', null=True)),
                ('permission_user', models.ForeignKey(blank=True, help_text='An auto-created user whose permissions this scope allows access to.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(db_index=True, default=oauth2app.models.KeyGenerator(20), max_length=20, unique=True)),
                ('refresh_token', models.CharField(blank=True, db_index=True, default=oauth2app.models.KeyGenerator(20), max_length=20, null=True, unique=True)),
                ('mac_key', models.CharField(blank=True, default=None, max_length=20, null=True, unique=True)),
                ('issue', models.PositiveIntegerField(default=oauth2app.models.TimestampGenerator(), editable=False)),
                ('expire', models.PositiveIntegerField(default=oauth2app.models.TimestampGenerator(3600))),
                ('refreshable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('key', models.CharField(db_index=True, default=oauth2app.models.KeyGenerator(30), max_length=30, unique=True)),
                ('secret', models.CharField(default=oauth2app.models.KeyGenerator(30), max_length=30, unique=True)),
                ('redirect_uri', models.URLField(null=True)),
                ('auto_authorize', models.BooleanField()),
                ('all_scopes_allowable', models.BooleanField()),
                ('allowable_scopes', models.ManyToManyField(blank=True, to='oauth2app.AccessRange')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, default=oauth2app.models.KeyGenerator(30), max_length=30, unique=True)),
                ('issue', models.PositiveIntegerField(default=oauth2app.models.TimestampGenerator(), editable=False)),
                ('expire', models.PositiveIntegerField(default=oauth2app.models.TimestampGenerator(120))),
                ('redirect_uri', models.URLField(null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth2app.Client')),
                ('scope', models.ManyToManyField(to='oauth2app.AccessRange')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MACNonce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nonce', models.CharField(db_index=True, max_length=30)),
                ('access_token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth2app.AccessToken')),
            ],
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth2app.Client'),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='scope',
            field=models.ManyToManyField(to='oauth2app.AccessRange'),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]