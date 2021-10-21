import sys

from gooey import Gooey, GooeyParser
from plugin.extractWav import ExtractWav
from plugin.flvToMp4 import FlvToMp4
from plugin.extractMp3 import ExtractMp3
from plugin.splitVideo import SplitVideo

@Gooey(
    program_name='Keroro Box',
    tabbed_groups=True,
    navigation='Tabbed'
    )
def main():
    settings_msg = "test"
    parser = GooeyParser(description=settings_msg)
    parser.add_argument('--verbose', help='be verbose', dest='verbose',
                        action='store_true', default=False)
    subs = parser.add_subparsers(help='commands', dest='command')
    # ########################################################
    # 音视频提取wav
    extract_wav_parser = subs.add_parser(
        '音视频提取wav', help='extractWav')
    extract_wav_parser = ExtractWav.extract(extract_wav_parser)
    # flv转mp4
    flv_to_mp4_parser = subs.add_parser(
        'flv转mp4', help='flvToMp4')
    flv_to_mp4_parser = FlvToMp4.extract(flv_to_mp4_parser)
    # 音频转mp3
    extract_mp3_parser = subs.add_parser(
        '音频转mp3', help='extractMp3')
    extract_mp3_parser = ExtractMp3.extract(extract_mp3_parser)
    # 片段截取
    split_video_parser = subs.add_parser(
        '片段截取', help='splitVideo')
    split_video_parser = SplitVideo.extract(split_video_parser)
    # ########################################################
    args = parser.parse_args()
    inputName = args.Filename
    outputName = args.outputFile
    tabName = sys.argv[1]
    # #############################
    if tabName == '音视频提取wav':
        shell = ExtractWav.templateShell(inputName, outputName)
    elif tabName == 'flv转mp4':
        shell = FlvToMp4.templateShell(inputName, outputName)
    elif tabName == '音频转mp3':
        bitrate = args.bitrate
        shell = ExtractMp3.templateShell(inputName, bitrate, outputName)
    elif tabName == '片段截取':
        startTime = args.startTime
        endTime = args.endTime
        shell = SplitVideo.templateShell(inputName, startTime, endTime, outputName)
    # ########################################################
    runShell(shell)

def runShell(shell):
    print(shell)
    # subprocess.run(shell)

if __name__ == '__main__':
    main()
