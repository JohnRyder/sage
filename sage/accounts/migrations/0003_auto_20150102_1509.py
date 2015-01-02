# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_created_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='isAdmin',
            new_name='is_admin',
        ),
    ]
