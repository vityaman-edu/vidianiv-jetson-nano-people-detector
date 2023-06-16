from typing import NamedTuple
from argparse import (
    ArgumentParser, 
    RawTextHelpFormatter,
)
import sys


class Arguments(NamedTuple):
    output: str

    @classmethod
    def parse_argv(cls) -> 'Arguments':
        parser = ArgumentParser(
            description="Locate objects in a live camera stream using an object detection DNN.", 
            formatter_class=RawTextHelpFormatter
        )
        parser.add_argument(
            "--output", type=str, default="", nargs='?', 
            help="URI of the output stream, example: localhost:10101"
        )
        try:
            args = parser.parse_known_args()[0]
            return Arguments(
                output = args.output,
            )
        except Exception as e:
            print(e)
            parser.print_help()
            sys.exit(0)
