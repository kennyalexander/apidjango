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


class CargoEmp(models.Model):
    id_cargo_emp = models.FloatField(primary_key=True)
    cargo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cargo_emp'


class Comuna(models.Model):
    id_comuna = models.FloatField(primary_key=True)
    comuna = models.CharField(max_length=50)
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
    rut = models.FloatField(primary_key=True)
    dv_rut = models.CharField(max_length=1)
    p_nombre = models.CharField(max_length=50)
    s_nombre = models.CharField(max_length=50)
    s_apellido = models.CharField(max_length=50)
    p_apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    empresa_id_empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='empresa_id_empresa')
    cargo_emp_id_cargo_emp = models.ForeignKey(CargoEmp, models.DO_NOTHING, db_column='cargo_emp_id_cargo_emp')
    imagen = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class Empresa(models.Model):
    id_empresa = models.FloatField(primary_key=True)
    empresa = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    n_direccion = models.FloatField()
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna')

    class Meta:
        managed = False
        db_table = 'empresa'


class EstadoR(models.Model):
    id_estado = models.FloatField(primary_key=True)
    estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_r'


class EstadoS(models.Model):
    id_estado_solicitud = models.FloatField(primary_key=True)
    estado_solicitud = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_s'


class Piso(models.Model):
    id_piso = models.FloatField(primary_key=True)
    piso = models.FloatField()

    class Meta:
        managed = False
        db_table = 'piso'


class Prioridad(models.Model):
    id_prioridad = models.FloatField(primary_key=True)
    prioridad = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'prioridad'


class Region(models.Model):
    id_region = models.FloatField(primary_key=True)
    region = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'region'


class Reporte(models.Model):
    id_repote = models.FloatField(primary_key=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    fecha_ingreso = models.DateField()
    usuario_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_usuario')
    prioridad_id_prioridad = models.ForeignKey(Prioridad, models.DO_NOTHING, db_column='prioridad_id_prioridad')
    piso_id_piso = models.ForeignKey(Piso, models.DO_NOTHING, db_column='piso_id_piso')
    sector_id_sector = models.ForeignKey('Sector', models.DO_NOTHING, db_column='sector_id_sector')
    estado_r_id_estado = models.ForeignKey(EstadoR, models.DO_NOTHING, db_column='estado_r_id_estado')
    imagen = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reporte'


class Sector(models.Model):
    id_sector = models.FloatField(primary_key=True)
    sector = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sector'


class Solicitud(models.Model):
    id_solicitud = models.FloatField(primary_key=True)
    solicitud = models.CharField(max_length=50)
    attribute_3 = models.DateField()
    usuario_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_usuario')
    estado_s_id_estado_solicitud = models.ForeignKey(EstadoS, models.DO_NOTHING, db_column='estado_s_id_estado_solicitud')

    class Meta:
        managed = False
        db_table = 'solicitud'


class Usuario(models.Model):
    usuario = models.CharField(primary_key=True, max_length=50)
    contrasena = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)
    empleado_rut = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_rut')

    class Meta:
        managed = False
        db_table = 'usuario'
