# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 03:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type_id', models.IntegerField(choices=[(1, '服务器'), (2, '交换机'), (3, '防火墙')], default=1)),
                ('device_status_id', models.IntegerField(choices=[(1, '上架'), (2, '在线'), (3, '离线'), (4, '下架')], default=1)),
                ('cabinet_num', models.CharField(blank=True, max_length=30, null=True, verbose_name='机柜号')),
                ('cabinet_order', models.CharField(blank=True, max_length=30, null=True, verbose_name='机柜中序号')),
                ('latest_date', models.DateField(null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '资产表',
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=8, verbose_name='插槽位')),
                ('model', models.CharField(max_length=32, verbose_name='磁盘型号')),
                ('capacity', models.FloatField(verbose_name='磁盘容量GB')),
                ('pd_type', models.CharField(max_length=32, verbose_name='磁盘类型')),
            ],
            options={
                'verbose_name_plural': '硬盘表',
            },
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=32, verbose_name='插槽位')),
                ('manufacturer', models.CharField(blank=True, max_length=32, null=True, verbose_name='制造商')),
                ('model', models.CharField(max_length=64, verbose_name='型号')),
                ('capacity', models.FloatField(blank=True, null=True, verbose_name='容量')),
                ('sn', models.CharField(blank=True, max_length=64, null=True, verbose_name='内存SN号')),
                ('speed', models.CharField(blank=True, max_length=16, null=True, verbose_name='速度')),
            ],
            options={
                'verbose_name_plural': '内存表',
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('management_ip', models.CharField(blank=True, max_length=64, null=True, verbose_name='管理IP')),
                ('vlan_ip', models.CharField(blank=True, max_length=64, null=True, verbose_name='VlanIP')),
                ('intranet_ip', models.CharField(blank=True, max_length=128, null=True, verbose_name='内网IP')),
                ('sn', models.CharField(max_length=64, unique=True, verbose_name='SN号')),
                ('manufacture', models.CharField(blank=True, max_length=128, null=True, verbose_name='制造商')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='型号')),
                ('port_num', models.SmallIntegerField(blank=True, null=True, verbose_name='端口个数')),
                ('device_detail', models.CharField(blank=True, max_length=255, null=True, verbose_name='设置详细配置')),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='repository.Asset')),
            ],
            options={
                'verbose_name_plural': '网络设备',
            },
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='网卡名称')),
                ('hwaddr', models.CharField(max_length=64, verbose_name='网卡mac地址')),
                ('netmask', models.CharField(max_length=64)),
                ('ipaddrs', models.CharField(max_length=256, verbose_name='ip地址')),
                ('up', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': '网卡表',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=128, unique=True)),
                ('sn', models.CharField(db_index=True, max_length=64, verbose_name='SN号')),
                ('manufacturer', models.CharField(blank=True, max_length=64, null=True, verbose_name='制造商')),
                ('model', models.CharField(blank=True, max_length=64, null=True, verbose_name='型号')),
                ('manage_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='管理IP')),
                ('os_platform', models.CharField(blank=True, max_length=16, null=True, verbose_name='系统')),
                ('os_version', models.CharField(blank=True, max_length=16, null=True, verbose_name='系统版本')),
                ('cpu_count', models.IntegerField(blank=True, null=True, verbose_name='CPU个数')),
                ('cpu_physical_count', models.IntegerField(blank=True, null=True, verbose_name='CPU物理个数')),
                ('cpu_model', models.CharField(blank=True, max_length=128, null=True, verbose_name='CPU型号')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='repository.Asset')),
            ],
            options={
                'verbose_name_plural': '服务器表',
            },
        ),
        migrations.AddField(
            model_name='nic',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nic', to='repository.Server'),
        ),
        migrations.AddField(
            model_name='memory',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memory', to='repository.Server'),
        ),
        migrations.AddField(
            model_name='disk',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disk', to='repository.Server'),
        ),
    ]
