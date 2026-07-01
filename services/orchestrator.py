from packages.core import SpeculativeDecodingEngine

class Orchestrator:
    def __init__(self, engine: SpeculativeDecodingEngine):
        self.engine = engine

    def start(self):
        logging.info('Starting orchestrator')
        self.engine.start()

    def stop(self):
        logging.info('Stopping orchestrator')
        self.engine.stop()
