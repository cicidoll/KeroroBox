from string import Template
class FlvToMp4:
    def __init__(self):
        pass
    @staticmethod
    def extractMp4(parser):
        shell = './bin/ffmpeg -i $input -y -vcodec copy -acodec copy $output.mp4'
        group = parser.add_argument_group('flv转mp4')
        group.add_argument(
            'Filename',
            help = '支持直接拖入文件',
            metavar = u'选择文件',
            widget = "FileChooser" )
        group.add_argument(
            "outputFile",
            help = '支持直接拖入文件',
            metavar = u'输出文件名',
            default = 'output' )
        args = parser.parse_args()
        input = args.Filename
        output = args.outputFile
        shell = Template(shell).substitute(input=input, output=output)
        return parser, shell
        