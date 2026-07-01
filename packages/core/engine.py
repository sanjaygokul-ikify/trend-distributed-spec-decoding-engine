import logging
from typing import List, Tuple
from .types import SpeculativeAgent, ValidationService
from .exceptions import SpeculativeDecodingException
import heapq

class SpeculativeDecodingEngine:
    def __init__(self, worker_pool: List[SpeculativeAgent], validation_service: ValidationService):
        self.worker_pool = worker_pool
        self.validation_service = validation_service
        self.memory_coherence_cache = {}
        self.persistent_memory_store = {}
        self.agent_coordination_manager = None

    def allocate(self, task: Tuple[str, str]) -> None:
        # Allocate task to available worker
        available_workers = [worker for worker in self.worker_pool if not worker.is_busy()]
        if available_workers:
            worker = available_workers[0]
            worker.allocate(task)
            worker.start()  # Added start() call
        else:
            raise SpeculativeDecodingException('No available workers')

    def propose(self, speculative_token: str, validation_priority: int) -> None:
        # Propose speculative token to validation service
        self.validation_service.propose(speculative_token, validation_priority)

    def validate(self, speculative_token: str) -> bool:
        # Validate speculative token
        return self.validation_service.validate(speculative_token)

    def update_memory_coherence_cache(self, speculative_token: str, validated_token: str) -> None:
        # Update memory coherence cache
        self.memory_coherence_cache[speculative_token] = validated_token

    def update_persistent_memory_store(self, speculative_token: str, validated_token: str) -> None:
        # Update persistent memory store
        self.persistent_memory_store[speculative_token] = validated_token

    def get_agent_coordination_manager(self) -> 'AgentCoordinationManager':
        # Get agent coordination manager
        return self.agent_coordination_manager

    def set_agent_coordination_manager(self, agent_coordination_manager: 'AgentCoordinationManager') -> None:
        # Set agent coordination manager
        self.agent_coordination_manager = agent_coordination_manager

    def start(self) -> None:
        # Start speculative decoding engine
        logging.info('Starting speculative decoding engine')
        for worker in self.worker_pool:
            worker.start()
        self.validation_service.start()
        self.agent_coordination_manager.start()

    def stop(self) -> None:
        # Stop speculative decoding engine
        logging.info('Stopping speculative decoding engine')
        for worker in self.worker_pool:
            worker.stop()
        self.validation_service.stop()
        self.agent_coordination_manager.stop()

    def join(self) -> None:
        # Join speculative decoding engine
        logging.info('Joining speculative decoding engine')
        for worker in self.worker_pool:
            worker.join()
        self.validation_service.join()
        self.agent_coordination_manager.join()

    def is_alive(self) -> bool:
        # Check if speculative decoding engine is alive
        return any(worker.is_alive() for worker in self.worker_pool) or self.validation_service.is_alive() or self.agent_coordination_manager.is_alive()

    def __str__(self) -> str:
        # String representation of speculative decoding engine
        return f'SpeculativeDecodingEngine(worker_pool={self.worker_pool}, validation_service={self.validation_service})'

    def __repr__(self) -> str:
        # Representation of speculative decoding engine
        return f'SpeculativeDecodingEngine(worker_pool={self.worker_pool}, validation_service={self.validation_service})'

