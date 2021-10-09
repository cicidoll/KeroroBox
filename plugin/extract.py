from string import Template
class Extract:
    def __init__(self):
        pass
    @staticmethod
    def extractWav(parser):
        shell = './bin/ffmpeg -i $input -c:v copy -strict experimental $output.wav'
        group = parser.add_argument_group('音视频提取wav')
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
        