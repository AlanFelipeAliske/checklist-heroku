from django.db import models


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