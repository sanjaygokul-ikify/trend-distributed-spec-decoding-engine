import argparse
from packages.core import SpeculativeDecodingEngine
from services.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', action='store_true')
    parser.add_argument('--stop', action='store_true')
    args = parser.parse_args()

    engine = SpeculativeDecodingEngine([], None)
    orchestrator = Orchestrator(engine)

    if args.start:
        orchestrator.start()
    elif args.stop:
        orchestrator.stop()

if __name__ == '__main__':
    main()
