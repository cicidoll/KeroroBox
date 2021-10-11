# from string import Template

class FlvToMp4:
    def __init__(self):
        pass
    @staticmethod
    def extract(parser):
        # shell = './bin/ffmpeg -i $input -y -vcodec copy -acodec copy $output.mp4'
        flvToMp4Group = parser.add_argument_group('flv转mp4')
        flvToMp4Group.add_argument(
            'Filename',
            help = '支持直接拖入文件',
            metavar = u'选择文件',
            widget = "FileChooser" )
        flvToMp4Group.add_argument(
            "outputFile",
            help = '支持直接拖入文件',
            metavar = u'输出文件名',
            default = 'output' )
        # input = args.Filename
        # output = args.outputFile
        # shell = Template(shell).substitute(input=input, output=output)
        # return parser, shell
        return parser
        