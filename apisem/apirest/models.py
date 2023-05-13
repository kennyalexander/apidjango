# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comuna(models.Model):
    id_comuna = models.FloatField(primary_key=True)
    comuna = models.CharField(max_length=40, blank=True, null=True)
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region')

    class Meta:
        managed = False
        db_table = 'comuna'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    id_empleado = models.FloatField(primary_key=True)
    p_nombre = models.CharField(max_length=15)
    s_nombre = models.CharField(max_length=15)
    p_apellido = models.CharField(max_length=15)
    s_apellido = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    rut = models.CharField(max_length=8)
    dv_rut = models.CharField(max_length=1)
    empresa_id_empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='empresa_id_empresa')

    class Meta:
        managed = False
        db_table = 'empleado'


class Empresa(models.Model):
    id_empresa = models.FloatField(primary_key=True)
    empresa = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna')

    class Meta:
        managed = False
        db_table = 'empresa'


class Region(models.Model):
    id_region = models.FloatField(primary_key=True)
    region = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'region'


class Reporte(models.Model):
    id_reporte = models.FloatField(primary_key=True)
    imagen = models.BinaryField()
    titulo = models.CharField(max_length=25)
    ingreso = models.DateField()
    descripcion = models.CharField(max_length=250)
    empleado_id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_empleado')

    class Meta:
        managed = False
        db_table = 'reporte'


class Solicitud(models.Model):
    id_solicitud = models.FloatField(primary_key=True)
    solicitud = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=50)
    fecha = models.DateField()
    empleado_id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_empleado')

    class Meta:
        managed = False
        db_table = 'solicitud'


class Tabla(models.Model):
    id = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tabla'


class Usuario(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    edad = models.FloatField(blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Yoryi(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'yoryi'
