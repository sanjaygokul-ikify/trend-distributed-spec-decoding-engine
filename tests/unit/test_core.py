import unittest
from packages.core import SpeculativeAgent, ValidationService, AgentCoordinationManager, SpeculativeDecodingEngine

class TestCore(unittest.TestCase):
    def test_speculative_agent(self):
        agent = SpeculativeAgent(1, 1, 1)
        self.assertFalse(agent.is_busy)

    def test_validation_service(self):
        validation_service = ValidationService()
        self.assertIsNone(validation_service.validation_priority_queue)

    def test_agent_coordination_manager(self):
        manager = AgentCoordinationManager()
        self.assertIsNone(manager.agents)

    def test_speculative_decoding_engine(self):
        engine = SpeculativeDecodingEngine([], None)
        self.assertEqual(engine.worker_pool, [])
        self.assertIsNone(engine.validation_service)

if __name__ == '__main__':
    unittest.main()
