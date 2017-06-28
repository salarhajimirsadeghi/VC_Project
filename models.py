# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Companies(models.Model):
    cid = models.CharField(db_column='CID', primary_key=True, max_length=256)  # Field name made lowercase.
    company_name = models.CharField(db_column='COMPANY_NAME', max_length=256)  # Field name made lowercase.
    perma_link = models.CharField(db_column='PERMA_LINK', max_length=256)  # Field name made lowercase.
    image = models.CharField(db_column='IMAGE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=6000, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=256, blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=256)  # Field name made lowercase.
    total_funding = models.CharField(db_column='TOTAL_FUNDING', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMPANIES'


class VcCompany(models.Model):
    vid = models.ForeignKey('Vcs', models.DO_NOTHING, db_column='VID')  # Field name made lowercase.
    vc_name = models.CharField(db_column='VC_NAME', max_length=256)  # Field name made lowercase.
    cid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CID')  # Field name made lowercase.
    company_name = models.CharField(db_column='COMPANY_NAME', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VC_COMPANY'


class Vcs(models.Model):
    vid = models.CharField(db_column='VID', primary_key=True, max_length=256)  # Field name made lowercase.
    vc_name = models.CharField(db_column='VC_NAME', max_length=256)  # Field name made lowercase.
    perma_link = models.CharField(db_column='PERMA_LINK', max_length=256)  # Field name made lowercase.
    image = models.CharField(db_column='IMAGE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=6000, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=256, blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=256)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=256, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=256, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZIPCODE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VCs'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

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
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class VcplatformCompanies(models.Model):
    cid = models.CharField(db_column='CID', primary_key=True, max_length=10)  # Field name made lowercase.
    company_name = models.CharField(db_column='COMPANY_NAME', max_length=500)  # Field name made lowercase.
    perma_link = models.CharField(db_column='PERMA_LINK', max_length=500)  # Field name made lowercase.
    image = models.CharField(db_column='IMAGE', max_length=500)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=500)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=500)  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=500)  # Field name made lowercase.
    total_funding = models.CharField(db_column='TOTAL_FUNDING', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vcplatform_companies'
