from iotManager import ConfiguracoesGlobais


def testar_iot_manager():
    configuracoes = ConfiguracoesGlobais.get_instance()
    print("\nConfigurações iniciais:", configuracoes)

    configuracoes.ambiente = "produção"
    configuracoes.maximo_conexoes = 50

    mesma_instancia = ConfiguracoesGlobais.get_instance()
    print("\nConfigurações alteradas:", mesma_instancia)

    print("\nÉ a mesma instância?", configuracoes is mesma_instancia)


testar_iot_manager()
