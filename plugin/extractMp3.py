from string import Template

class ExtractMp3:
    def __init__(self):
        pass

    @staticmethod
    def extract(parser):
        parser.add_argument(
            'Filename',
            help = '支持直接拖入文件',
            metavar = u'选择文件',
            widget = "FileChooser" )
        parser.add_argument(
            'bitrate',
            help = '码率（128、192、320）',
            metavar = u'选择输出音频',
            widget = "TextField",
            default = "320")
        parser.add_argument(
            "outputFile",
            help = '无需后缀',
            metavar = u'输出音频文件名',
            default = 'output' )
        return parser

    @staticmethod
    def templateShell(inputName, bitrate, outputName):
        shell = './bin/ffmpeg -i  $input -b:a $bitratek $output'
        shell = Template(shell).substitute(input=inputName, bitrate=bitrate, output=outputName)
        return shell
        