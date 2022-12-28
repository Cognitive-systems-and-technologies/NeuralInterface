# Generated by Django 4.1.1 on 2022-12-22 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_group_name', models.CharField(max_length=100)),
                ('agent_group_priority', models.IntegerField()),
                ('datetime_create', models.DateTimeField(auto_now_add=True)),
                ('datetime_change', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AgentTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_port', models.IntegerField()),
                ('agent_name', models.CharField(max_length=100)),
                ('agent_status', models.IntegerField()),
                ('datetime_create', models.DateTimeField(auto_now_add=True)),
                ('datetime_change', models.DateTimeField(auto_now_add=True)),
                ('agent_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.agentgroups')),
                ('agent_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.agenttypes')),
            ],
        ),
        migrations.CreateModel(
            name='AgentErrors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_step', models.IntegerField()),
                ('agent_error_value', models.FloatField()),
                ('datetime_create', models.DateTimeField(auto_now_add=True)),
                ('agent_port', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.agents')),
            ],
        ),
    ]
