import os
import pytest

def test_env_var_exists():
    assert 'PUBLIC_API_KEY' in os.environ
