from iotManager import ConfiguracoesGlobais
from teste import testar_iot_manager


def main():
    instance = ConfiguracoesGlobais.get_instance()
    print("############################################")
    print(instance.ambiente)
    print("############################################")
    testar_iot_manager()
    print("############################################")
    print(instance.ambiente)

if __name__ == "__main__":
    main()