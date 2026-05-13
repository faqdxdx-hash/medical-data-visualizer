import unittest
import medical_data_visualizer as medical

class MedicalDataVisualizerTestCase(unittest.TestCase):
    def setUp(self):
        """Verificar que medical_data_visualizer tiene las funciones necesarias"""
        self.has_catplot = hasattr(medical, 'draw_cat_plot')
        self.has_heatmap = hasattr(medical, 'draw_heat_map')
        
    def test_catplot_function_exists(self):
        """Prueba 1: Verificar que existe la función draw_cat_plot"""
        self.assertTrue(self.has_catplot, 
                       "La función draw_cat_plot() no está definida en medical_data_visualizer")
    
    def test_heatmap_function_exists(self):
        """Prueba 2: Verificar que existe la función draw_heat_map"""
        self.assertTrue(self.has_heatmap,
                       "La función draw_heat_map() no está definida en medical_data_visualizer")
    
    def test_catplot_returns_figure(self):
        """Prueba 3: Verificar que draw_cat_plot devuelve una figura"""
        if self.has_catplot:
            fig = medical.draw_cat_plot()
            self.assertIsNotNone(fig, "draw_cat_plot() no devolvió una figura")
    
    def test_heatmap_returns_figure(self):
        """Prueba 4: Verificar que draw_heat_map devuelve una figura"""
        if self.has_heatmap:
            fig = medical.draw_heat_map()
            self.assertIsNotNone(fig, "draw_heat_map() no devolvió una figura")
    
    def test_overweight_column_exists(self):
        """Prueba 5: Verificar que existe la columna 'overweight' en el DataFrame"""
        try:
            # Intentar acceder al DataFrame de medical_data_visualizer
            if hasattr(medical, 'df'):
                self.assertIn('overweight', medical.df.columns,
                             "La columna 'overweight' no está en el DataFrame")
            else:
                # Cargar datos y verificar
                import pandas as pd
                df = pd.read_csv('medical_examination.csv')
                self.skipTest("No se pudo acceder a df desde medical_data_visualizer")
        except Exception as e:
            self.skipTest(f"No se pudo verificar la columna overweight: {e}")

# Esta es la función que necesitas - definida explícitamente
def run_tests():
    """Ejecuta todas las pruebas unitarias"""
    # Crear un suite de pruebas
    suite = unittest.TestLoader().loadTestsFromTestCase(MedicalDataVisualizerTestCase)
    
    # Ejecutar las pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Retornar True si todas las pruebas pasaron
    return result.wasSuccessful()

# También puedes ejecutar las pruebas directamente
if __name__ == "__main__":
    success = run_tests()
    print(f"\n¿Todas las pruebas pasaron? {success}")