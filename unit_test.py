import unittest

# (e.g., MenuPanel)
class MenuPanel:
    def calcCubeArea(self, length):
        return 6 * (length ** 2)  # Example calculation for cube surface area

    def calcArea(self, length, width, height):
        return 2 * (length * width + width * height + height * length)  # Example for rectangular prism surface area

    def calc_cylinder_surface_area(self, radius, height):
        return 2 * 3.14159 * radius * (radius + height)  # Example for cylinder surface area

# Test class
class TestMenuPanel(unittest.TestCase):
    
    def setUp(self):
        # Initialize the menu_panel object before each test
        self.menu_panel = MenuPanel()

    def test_calcCubeArea(self):
        length = 3
        expected_area = 54  # 6 * 3^2
        self.assertEqual(self.menu_panel.calcCubeArea(length), expected_area)

    def test_calcArea(self):
        length = 2
        width = 3
        height = 4
        expected_area = 52  # 2*(2*3 + 3*4 + 4*2)
        self.assertEqual(self.menu_panel.calcArea(length, width, height), expected_area)

    def test_calc_cylinder_surface_area(self):
        radius = 5
        height = 10
        expected_area = 471.24  # 2 * π * r * (r + h)
        self.assertAlmostEqual(self.menu_panel.calc_cylinder_surface_area(radius, height), expected_area, places=2)

if __name__ == '__main__':
    unittest.main()
