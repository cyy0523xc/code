# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2019年07月22日 星期一 15时10分32秒
from moviepy.editor import VideoFileClip


def audio_split(path):
    """从视频文件里分离出音频文件，保存为wav格式文件
    Args:
        path: 视频地址
    """
    print(path)
    save_fn = path.split('/')[-1]
    save_fn = save_fn.split('.')[0]
    data = {
        'audio_path': save_fn + '.wav'  # 获取保存目录
    }
    videoclip = VideoFileClip(path)
    audioclip = videoclip.audio
    audioclip.write_audiofile(data['audio_path'], verbose=True,
                              ffmpeg_params=["-ac", "1"],
                              fps=16000, nbytes=2, bitrate='256k',
                              codec='pcm_s16le')
    return data


if __name__ == '__main__':
    import sys
    import os
    path = sys.argv[1]
    if os.path.isfile(path):
        files = audio_split(path)
    elif os.path.isdir(path):
        for fn in os.listdir(path):
            fn = os.path.join(path, fn)
            files = audio_split(fn)
    else:
        raise Exception('缺少参数')
