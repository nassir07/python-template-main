"""Test MyModule."""
from python_template.application.my_module import MyModule


class TestMyModule:
    """Test MyModule."""

    def test_one(self):
        """Implement test 1."""
        self.value = 1
        assert MyModule.my_function() is None
