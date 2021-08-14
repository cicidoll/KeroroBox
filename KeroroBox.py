from string import Template
import subprocess
from gooey import Gooey, GooeyParser

optionSetting = {
  '视频提取wav / 音频转wav': './bin/ffmpeg -i $input -c:v copy -strict experimental $output',
  'flv转mp4': './bin/ffmpeg -i $input -y -vcodec copy -acodec copy $output',
  '音频转mp3 （默认转换为320k）': './bin/ffmpeg -i  $input -b:a 320k $output',
  '片段截取': './bin/ffmpeg -ss $startTime -t $endTime -accurate_seek -i $input -codec copy -avoid_negative_ts 1 $output'
}

@Gooey
def main():
    optionSettingKeyList = list(optionSetting.keys())

    parser = GooeyParser(
        description = "      该工具箱提供简单的音视频操作。\n 如果好用的话，请大家给蛙吹Keroro点个关注吧！")

    parser.add_argument(
        'Filename',
        metavar = u'输入文件名',
        widget = "FileChooser" )
    parser.add_argument(
        "outputFile",
        help = '请根据需要输出的格式，自定义文件后缀名',
        metavar = u'输出文件名（例如：output.mp4）',
        default = 'output.mp4' )

    parser.add_argument(
        'startTime',
        help = '仅当选择功能: 片段截取 时，该选项生效',
        metavar = u'起始时间点（00:01:23）',
        widget = "TextField",
        default = "00:01:23")
    parser.add_argument(
        'endTime',
        help = '仅当选择功能: 片段截取 时，该选项生效',
        metavar = u'结束时间点（00:03:23）',
        widget = "TextField",
        default = "00:03:23")

    parser.add_argument(
        "option",
        metavar = u'视频操作功能选择：',
        choices = optionSettingKeyList,
        default = optionSettingKeyList[0] )

    args = parser.parse_args()
    input = args.Filename
    output = args.outputFile
    startTime = args.startTime
    endTime = args.endTime
    if (args.option == '片段截取'):
        shell = Template(optionSetting[args.option]).substitute(input=input, startTime=startTime, endTime=endTime, output=output)
    else:
        shell = Template(optionSetting[args.option]).substitute(input=input, output=output)
    runShell(shell)

def runShell(shell):
    subprocess.run(shell)

if   __name__ == '__main__':
    main()