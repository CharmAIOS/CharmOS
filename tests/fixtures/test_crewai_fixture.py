from pathlib import Path
import importlib.util

def test_fixture_agents_exist():
    path = Path("fixtures/crewai/research_agent/agents.py")
    assert path.exists(), "Fixture agents.py not found"

def test_fixture_importable():
    spec = importlib.util.spec_from_file_location("fixture_agents", "fixtures/crewai/research_agent/agents.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert hasattr(mod, "project_analyst"), "Agent 'project_analyst' missing in fixture"
