import threading

# ALTERNATIVA 2:
# Padrão de projeto usado = Singleton


class ConfiguracoesGlobais:
    _instancia = None
    _lock = threading.Lock()

    def __init__(self):
        self._ambiente = "desenvolvimento"
        self._maximo_conexoes = 10

    @property
    def ambiente(self):
        return self._ambiente

    @ambiente.setter
    def ambiente(self, value):
        self._ambiente = value

    @property
    def maximo_conexoes(self):
        return self._maximo_conexoes

    @maximo_conexoes.setter
    def maximo_conexoes(self, value):
        self._maximo_conexoes = value

    @staticmethod
    def get_instance():
        if ConfiguracoesGlobais._instancia is None:
            with ConfiguracoesGlobais._lock:
                if ConfiguracoesGlobais._instancia is None:
                    ConfiguracoesGlobais._instancia = ConfiguracoesGlobais()
        return ConfiguracoesGlobais._instancia

    def __str__(self):
        return f"ConfiguracoesGlobais(ambiente='{self.ambiente}', maximo_conexoes={self.maximo_conexoes})"
