import logging
from typing import List
from . import engine
from packages.core.engine import SpeculativeDecodingEngine

class RuntimeExecutor:
    def __init__(self, speculative_decoding_engine: SpeculativeDecodingEngine):
        self.speculative_decoding_engine = speculative_decoding_engine

    def start(self) -> None:
        # Start runtime executor
        logging.info('Starting runtime executor')
        self.speculative_decoding_engine.start()

    def stop(self) -> None:
        # Stop runtime executor
        logging.info('Stopping runtime executor')
        self.speculative_decoding_engine.stop()

    def join(self) -> None:
        # Join runtime executor
        logging.info('Joining runtime executor')
        self.speculative_decoding_engine.join()

    def is_alive(self) -> bool:
        # Check if runtime executor is alive
        return self.speculative_decoding_engine.is_alive()

