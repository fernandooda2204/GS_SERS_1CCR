import unittest
from energia import carregar_parametros,consumo_kwh,consumo_geladeira_etiqueta,comparar
class TestCalculos(unittest.TestCase):
 def setUp(self): self.p=carregar_parametros()
 def test_formula(self): self.assertAlmostEqual(consumo_kwh(100,5,30,2),30)
 def test_geladeira(self): self.assertEqual(consumo_geladeira_etiqueta(32.7),32.7)
 def test_negativo(self):
  with self.assertRaises(ValueError): consumo_kwh(-1,2)
 def test_solar_nao_supera_consumo(self):
  a=comparar(self.p,40)['a2_solar'];self.assertLessEqual(a['energia_compensada_kwh_mes'],40)
 def test_conta_nao_negativa(self): self.assertGreaterEqual(comparar(self.p,0)['a2_solar']['depois_brl'],0)
 def test_led_energia_positiva(self): self.assertGreater(comparar(self.p,200)['a3_led']['economia_kwh_mes'],0)
 def test_economia_nunca_negativa(self):
  for c in (0,10,100,200,500):
   a=comparar(self.p,c)
   self.assertGreaterEqual(a['a2_solar']['economia_brl_mes'],0)
   self.assertGreaterEqual(a['a3_led']['economia_brl_mes'],0)
if __name__=='__main__': unittest.main()
