from django.contrib import admin
from .models import AuthUser, Veiculos, EquipamentoSeguraca, CheckList


class VeiculosAdmin(admin.ModelAdmin):
    list_display = ('descricao_veiculo',)
    list_filter = ('descricao_veiculo',)
admin.site.register(Veiculos, VeiculosAdmin)


class EquipamentoSeguracaAdmin(admin.ModelAdmin):
    list_display = ('descricao_equipamento_seguranca',)
    list_filter = ('descricao_equipamento_seguranca',)
admin.site.register(EquipamentoSeguraca, EquipamentoSeguracaAdmin)


class CheckListAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    list_filter = ('descricao',)
admin.site.register(CheckList, CheckListAdmin)
