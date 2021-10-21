from string import Template

class SplitVideo:
    def __init__(self):
        pass

    @staticmethod
    def extract(parser):
        parser.add_argument(
            'startTime',
            help = '举例：00:01:23',
            metavar = u'填写起始时间点',
            widget = "TextField",
            default = "00:01:23")
        parser.add_argument(
            'endTime',
            help = '举例：00:03:23',
            metavar = u'填写结束时间点',
            widget = "TextField",
            default = "00:03:23")
        parser.add_argument(
            'Filename',
            help = '支持直接拖入文件',
            metavar = u'选择文件',
            widget = "FileChooser" )
        parser.add_argument(
            "outputFile",
            help = '需要后缀',
            metavar = u'输出视频文件名',
            default = 'output.mp4' )
        return parser

    @staticmethod
    def templateShell(inputName, startTime, endTime, outputName):
        shell = './bin/ffmpeg -ss $startTime -t $endTime -accurate_seek -i $input -codec copy -avoid_negative_ts 1 $output'
        shell = Template(shell).substitute(input=inputName, startTime=startTime, endTime=endTime, output=outputName)
        return shell
        