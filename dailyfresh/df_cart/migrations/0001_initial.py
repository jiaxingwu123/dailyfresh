# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=0)),
                ('goods', models.ForeignKey(to='df_goods.GoodsInfo')),
                ('user', models.ForeignKey(to='df_user.UserInfo')),
            ],
            options={
                'verbose_name': '\u8d2d\u7269\u8f66\u5546\u54c1\u4fe1\u606f',
                'verbose_name_plural': '\u8d2d\u7269\u8f66\u5546\u54c1\u4fe1\u606f',
            },
        ),
    ]
