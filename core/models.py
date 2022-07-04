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
    id = models.AutoField(primary_key=True)
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

    def __str__(self):
        return self.username

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
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

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



class Veiculos(models.Model):
    id = models.AutoField(primary_key=True)
    descricao_veiculo = models.CharField(verbose_name="Descrição do Veículo", max_length=256, blank=True, null=True)
    
    def __str__(self):
        return self.descricao_veiculo

class EquipamentoSeguraca(models.Model):
    id = models.AutoField(primary_key=True)
    descricao_equipamento_seguranca = models.CharField(verbose_name="Descrição do Equipamento de Segurança", max_length=256, blank=True, null=True)

    def __str__(self):
        return self.descricao_equipamento_seguranca

class VeiculoEquipamento(models.Model):
    id = models.AutoField(primary_key=True)
    veiculo = models.ForeignKey(Veiculos, on_delete=models.CASCADE, blank=True, null=True)
    equipamento_seguranca = models.ForeignKey(EquipamentoSeguraca, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.veiculo

class CheckList(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(verbose_name="Descrição do CheckList", max_length=256, blank=True, null=True)
    equipamento_seguranca = models.ManyToManyField(EquipamentoSeguraca)
    usuario = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    veiculos = models.ForeignKey(Veiculos, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class ChecklistEquipamentoSeguranca(models.Model):
    checklist = models.ForeignKey(CheckList, models.DO_NOTHING)
    equipamentoseguraca = models.ForeignKey('Equipamentoseguraca', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_checklist_equipamento_seguranca'
        unique_together = (('checklist', 'equipamentoseguraca'),)

class CheckListDetalhe(models.Model):
    id = models.AutoField(primary_key=True)
    checklist = models.ForeignKey(CheckList, on_delete=models.CASCADE)
    veiculo_equipamento = models.ForeignKey(VeiculoEquipamento, on_delete=models.CASCADE)
    checkbox = models.IntegerField(verbose_name='Checkbox', null=True, blank=True)
    
    def __str__(self):
        return self.checklist









"""


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


class CoreChecklist(models.Model):
    descricao = models.CharField(max_length=256, blank=True, null=True)
    usuario = models.ForeignKey(AuthUser, models.DO_NOTHING)
    veiculos = models.ForeignKey('CoreVeiculos', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_checklist'


class CoreChecklistEquipamentoSeguranca(models.Model):
    checklist = models.ForeignKey(CoreChecklist, models.DO_NOTHING)
    equipamentoseguraca = models.ForeignKey('CoreEquipamentoseguraca', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_checklist_equipamento_seguranca'
        unique_together = (('checklist', 'equipamentoseguraca'),)


class CoreChecklistdetalhe(models.Model):
    checkbox = models.IntegerField(blank=True, null=True)
    checklist = models.ForeignKey(CoreChecklist, models.DO_NOTHING)
    veiculo_equipamento = models.ForeignKey('CoreVeiculoequipamento', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_checklistdetalhe'


class CoreEquipamentoseguraca(models.Model):
    descricao_equipamento_seguranca = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_equipamentoseguraca'
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

"""