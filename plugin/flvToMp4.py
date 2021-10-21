from string import Template

class FlvToMp4:
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
            "outputFile",
            help = '无需后缀',
            metavar = u'输出视频文件名',
            default = 'output' )
        return parser

    @staticmethod
    def templateShell(inputName, outputName):
        shell = './bin/ffmpeg -i $input -y -vcodec copy -acodec copy $output.mp4'
        shell = Template(shell).substitute(input=inputName, output=outputName)
        return shell
        