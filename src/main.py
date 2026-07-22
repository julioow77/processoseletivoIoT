from machine import Pin
import time

class HX711:
    def __init__(self, dout, pd_sck):
        self.pSCK = Pin(pd_sck, Pin.OUT)
        self.pOUT = Pin(dout, Pin.IN)
        self.pSCK.value(0)

    def read(self):
        if self.pOUT.value() == 1:
            return None
        
        val = 0
        for _ in range(24):
            self.pSCK.value(1)
            val = (val << 1) | self.pOUT.value()
            self.pSCK.value(0)
        
        self.pSCK.value(1)
        self.pSCK.value(0)
        
        if val & (1 << 23):
            val -= 1 << 24
        return val

hx = HX711(dout=21, pd_sck=22)

print("Sistema Kanban Inicializado")

estado_atual = "DESCONHECIDO"
ultimo_tempo_leitura = time.ticks_ms()

while True:
    tempo_atual = time.ticks_ms()
    
    if time.ticks_diff(tempo_atual, ultimo_tempo_leitura) >= 500:
        ultimo_tempo_leitura = tempo_atual
        
        leitura_bruta = hx.read()
        
        if leitura_bruta is not None:
            peso_gramas = int(leitura_bruta / 420)
            
            if peso_gramas == 0:
                if estado_atual != "ERRO":
                    print("ALERTA: Caixa ausente ou erro de calibração no sensor HX711!")
                    estado_atual = "ERRO"
            
            elif peso_gramas <= 150:
                if estado_atual != "ALERTA_REPOSICAO":
                    print("Evento de reposição disparado! Caixa vazia detectada.")
                    estado_atual = "ALERTA_REPOSICAO"
                    
            elif peso_gramas >= 5000:
                if estado_atual == "ALERTA_REPOSICAO":
                    print("Abastecimento concluído. Caixa cheia.")
                estado_atual = "CARGA_CHEIA"
                
            elif 150 < peso_gramas < 5000:
                if estado_atual != "REGULAR_" + str(peso_gramas):
                    print(f"Status: Estoque Regular ({peso_gramas}g)")
                    estado_atual = "REGULAR_" + str(peso_gramas)
