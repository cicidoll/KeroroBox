from gooey import Gooey, GooeyParser
import subprocess
from plugin.extract import Extract

@Gooey(
    program_name='Keroro Box',
    tabbed_groups=True,
    navigation='Tabbed'
    )
def main():
    settings_msg = "该工具箱提供简单的音视频操作。\n 如果好用的话，请大家给蛙吹Keroro点个关注吧！"
    parser = GooeyParser(description=settings_msg)
    parser, shell = Extract.extractWav(parser)

    args=parser.parse_args()
    runShell(shell)

def runShell(shell):
    subprocess.run(shell)    

if __name__ == '__main__':
    main()
