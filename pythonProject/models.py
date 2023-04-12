# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TAgentErrors(models.Model):
    agent_step = models.IntegerField(blank=True, null=True)
    agent_error_value = models.FloatField(blank=True, null=True)
    datetime_create = models.DateTimeField(blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_agent_errors'


class TAgentFiles(models.Model):
    agent_id = models.CharField(max_length=250, blank=True, null=True)
    file_name = models.CharField(max_length=250, blank=True, null=True)
    file_type = models.CharField(max_length=250, blank=True, null=True)
    file_path = models.CharField(max_length=250, blank=True, null=True)
    file_description = models.CharField(max_length=250, blank=True, null=True)
    create_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_agent_files'


class TAgentGroups(models.Model):
    agent_group_name = models.CharField(max_length=100)
    agent_group_priority = models.IntegerField()
    datetime_create = models.DateTimeField()
    datetime_change = models.DateTimeField()
    agent_group_description = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_agent_groups'


class TAgentTypes(models.Model):
    agent_type = models.CharField(max_length=100)
    agent_type_description = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_agent_types'


class TAgents(models.Model):
    id = models.OneToOneField(TAgentFiles, models.DO_NOTHING, db_column='id', primary_key=True, blank=True, null=True)
    agent_name = models.CharField(blank=True, null=True)
    agent_group = models.ForeignKey(TAgentGroups, models.DO_NOTHING, blank=True, null=True)
    agent_status = models.IntegerField(blank=True, null=True)
    agent_description = models.CharField(blank=True, null=True)
    datetime_create = models.DateTimeField(blank=True, null=True)
    datetime_change = models.DateTimeField(blank=True, null=True)
    agent_type = models.ForeignKey(TAgentTypes, models.DO_NOTHING, blank=True, null=True)
    agent_port = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_agents'
