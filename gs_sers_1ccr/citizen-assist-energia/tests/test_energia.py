import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from energia import (carregar_parametros, comparar, consumo_geladeira_etiqueta, consumo_kwh,
                     conta_sem_mudancas, led, solar)
import respostas as r


class TestCalculos(unittest.TestCase):
    def setUp(self):
        self.p = carregar_parametros()

    def test_formula(self):
        self.assertAlmostEqual(consumo_kwh(100, 5, 30, 2), 30)

    def test_geladeira(self):
        self.assertEqual(consumo_geladeira_etiqueta(32.7), 32.7)

    def test_negativo(self):
        with self.assertRaises(ValueError):
            consumo_kwh(-1, 2)

    def test_conta_respeita_minimo(self):
        self.assertAlmostEqual(conta_sem_mudancas(self.p, 0), self.p['custo_disponibilidade_brl'])
        self.assertAlmostEqual(conta_sem_mudancas(self.p, 200), 200 * self.p['tarifa_energia_brl_kwh'])

    def test_solar_nao_supera_consumo(self):
        a = solar(self.p, 40)
        self.assertLessEqual(a['energia_compensada_kwh_mes'], 40)

    def test_solar_nao_zera_conta(self):
        a = solar(self.p, 100)
        self.assertGreaterEqual(a['depois_brl'], self.p['custo_disponibilidade_brl'])

    def test_solar_investimento_por_wp(self):
        a = solar(self.p, 200)
        esperado = self.p['potencia_solar_kwp'] * 1000 * self.p['custo_solar_brl_por_wp']
        self.assertAlmostEqual(a['investimento_brl'], esperado)

    def test_payback_mesma_unidade(self):
        comp = comparar(self.p, 200)
        for alt in ('a2_solar', 'a3_led'):
            self.assertAlmostEqual(comp[alt]['payback_meses'] / 12, comp[alt]['payback_anos'])

    def test_led_energia_positiva(self):
        self.assertGreater(led(self.p, 200)['economia_kwh_mes'], 0)

    def test_led_sem_economia_se_ja_e_led(self):
        a = led(self.p, 200, potencia_atual_w=9)
        self.assertEqual(a['economia_kwh_mes'], 0)
        self.assertIsNone(a['payback_meses'])

    def test_led_usa_dados_do_usuario(self):
        a = led(self.p, 200, potencia_atual_w=20, quantidade=4, horas_dia=3)
        self.assertAlmostEqual(a['economia_kwh_mes'], (20 - 9) * 3 * 30 * 4 / 1000)

    def test_led_respeita_custo_minimo(self):
        a = led(self.p, 37)
        self.assertGreaterEqual(a['depois_brl'], self.p['custo_disponibilidade_brl'])

    def test_economia_nunca_negativa(self):
        for c in (0, 10, 100, 200, 500):
            a = comparar(self.p, c)
            self.assertGreaterEqual(a['a2_solar']['economia_brl_mes'], 0)
            self.assertGreaterEqual(a['a3_led']['economia_brl_mes'], 0)


class TestRespostas(unittest.TestCase):
    def setUp(self):
        self.p = carregar_parametros()

    def test_formato_brasileiro(self):
        self.assertEqual(r.brl(1234.5), 'R$ 1.234,50')

    def test_intencoes(self):
        casos = {
            'Vale a pena colocar placa solar?': 'solar',
            'quanto economizo trocando as lâmpadas?': 'led',
            'Quanto vou pagar na conta?': 'conta',
            'qual o impacto no meio ambiente?': 'ambiental',
            'o que é kWh?': 'unidades',
            'qual a melhor opção para economizar?': 'comparar',
            'de onde vêm os dados?': 'fontes',
            'qual a previsão do tempo?': None,
        }
        for pergunta, esperado in casos.items():
            self.assertEqual(r.identificar_intencao(pergunta), esperado, pergunta)

    def test_respostas_tem_fonte_e_aviso(self):
        for texto in (r.resposta_conta(self.p, 200), r.resposta_solar(self.p, 200),
                      r.resposta_led(self.p, 200), r.resposta_comparacao(self.p, 200)):
            self.assertIn('Fontes:', texto)
            self.assertIn('estimativas', texto)

    def test_recomendacao_coerente_com_calculo(self):
        texto = r.recomendacao(self.p, 200)
        self.assertIn('Comece pelo LED', texto)
        texto_ja_led = r.recomendacao(self.p, 200, potencia_atual_w=9)
        self.assertIn('não traz economia', texto_ja_led)

    def test_solar_nao_compensa_consumo_minimo(self):
        self.assertIn('Solar não compensa', r.recomendacao(self.p, 30))

    def test_pergunta_fora_do_tema(self):
        self.assertIsNone(r.responder('qual a previsão do tempo?', self.p))


if __name__ == '__main__':
    unittest.main()
