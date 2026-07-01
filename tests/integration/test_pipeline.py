import unittest
from packages.core import SpeculativeDecodingEngine, SpeculativeAgent, ValidationService
from services.orchestrator import Orchestrator

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        agent = SpeculativeAgent(1, 1, 1)
        validation_service = ValidationService()
        engine = SpeculativeDecodingEngine([agent], validation_service)
        orchestrator = Orchestrator(engine)

        orchestrator.start()
        self.assertTrue(agent.is_busy)
        orchestrator.stop()

if __name__ == '__main__':
    unittest.main()
