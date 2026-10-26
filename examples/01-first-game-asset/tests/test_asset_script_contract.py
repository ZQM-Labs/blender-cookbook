import ast
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "create_lantern.py"


class LanternAssetContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SCRIPT.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source)

    def test_script_is_valid_python_and_has_clear_entry_point(self):
        functions = {node.name for node in self.tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
        self.assertTrue({"parse_output_path", "build_lantern", "export_glb", "main"} <= functions)
        self.assertIn('if __name__ == "__main__":', self.source)

    def test_asset_has_named_components_and_materials(self):
        for required in (
            "Lantern_Base", "Lantern_Roof", "Lantern_Glow_Core", "Lantern_Handle",
            "Midnight enamel", "Warm brass", "Lantern glow",
        ):
            with self.subTest(required=required):
                self.assertIn(required, self.source)

    def test_export_is_glb_and_creates_parent_directory(self):
        self.assertIn('output_path.parent.mkdir(parents=True, exist_ok=True)', self.source)
        self.assertIn('export_format="GLB"', self.source)
        self.assertIn('export_apply=True', self.source)
        self.assertIn('export_yup=True', self.source)

    def test_no_network_or_shell_execution_in_asset_generator(self):
        forbidden = {"subprocess", "socket", "urllib", "requests", "os.system", "eval", "exec"}
        used = {node.id for node in ast.walk(self.tree) if isinstance(node, ast.Name)}
        used |= {
            f"{node.value.id}.{node.attr}"
            for node in ast.walk(self.tree)
            if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name)
        }
        self.assertFalse(forbidden & used)


if __name__ == "__main__":
    unittest.main()
