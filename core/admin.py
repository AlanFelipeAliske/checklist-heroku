
from django.contrib import admin
from .models import AuthUser, Veiculos, EquipamentoSeguraca, CheckList

"""
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_filter = ('id',)
admin.site.register(AuthUser, AuthUserAdmin)
"""
#------------------------------------------------------------------------------

class VeiculosAdmin(admin.ModelAdmin):
    list_display = ('descricao_veiculo',)
    list_filter = ('descricao_veiculo',)
admin.site.register(Veiculos, VeiculosAdmin)

#------------------------------------------------------------------------------

class EquipamentoSeguracaAdmin(admin.ModelAdmin):
    list_display = ('descricao_equipamento_seguranca',)
    list_filter = ('descricao_equipamento_seguranca',)
admin.site.register(EquipamentoSeguraca, EquipamentoSeguracaAdmin)

#------------------------------------------------------------------------------
"""
class VeiculoEquipamentoAdmin(admin.ModelAdmin):
    list_display = ('veiculo',)
    list_filter = ('veiculo',)
admin.site.register(VeiculoEquipamento, VeiculoEquipamentoAdmin)

"""
#------------------------------------------------------------------------------

class CheckListAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    list_filter = ('descricao',)
admin.site.register(CheckList, CheckListAdmin)


#------------------------------------------------------------------------------
"""
class CheckListDetalheAdmin(admin.ModelAdmin):
    list_display = ('checklist', 'veiculo_equipamento',)
    list_filter = ('checklist', 'veiculo_equipamento',)
admin.site.register(CheckListDetalhe, CheckListDetalheAdmin)
"""

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
