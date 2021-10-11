from gooey import Gooey, GooeyParser
import subprocess
from plugin.extractWav import ExtractWav
from plugin.flvToMp4 import FlvToMp4
import utils
from message import display_message
argumentGroup = {
    "ExtractWav": {
        "parser": None,
        "shell": None
    },
    "FlvToMp4": {
        "parser": None,
        "shell": None
    },
}

@Gooey(
    program_name='Keroro Box',
    tabbed_groups=True,
    navigation='Tabbed'
    )
def main():
    settings_msg = "test"
    parser = GooeyParser(description=settings_msg)
    # parser, argumentGroup.ExtractWav.shell = ExtractWav.extract(parser)
    parser = ExtractWav.extract(parser)
    # parser = argumentGroup.ExtractWav.parser
    # parser, argumentGroup.FlvToMp4.shell = FlvToMp4.extract(parser)
    parser = FlvToMp4.extract(parser)
    # parser = argumentGroup.FlvToMp4.parser
    args = parser.parse_args()

    inputName = args.Filename
    outputName = args.outputFile
    # shell = utils.convertShell(str(), inputName, outputName)
    # print(args)
    # runShell(shell)
    display_message(args)

def runShell(shell):
    subprocess.run(shell)    

if __name__ == '__main__':
    main()
