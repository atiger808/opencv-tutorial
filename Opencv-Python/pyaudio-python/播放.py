# _*_ coding: utf-8 _*_
# @Time     : 2019/5/8 18:11
# @Author   : Ole211
# @Site     : 
# @File     : 播放.py    
# @Software : PyCharm

# 引入库
import pyaudio
import wave
import sys

# 定义数据流
CHUNK = 1024*50

if len(sys.argv) < 2:
    print('Plays a wave file.\n\nUsage: %s filename.wave' % sys.argv[0])
    sys.exit(-1)

# 只读方式打开wav
wf = wave.open('output.wav', 'rb')

p = pyaudio.PyAudio()

# 打开数据流
stream = p.open(format= p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# 读取数据
data = wf.readframes(CHUNK)

# 播放
while data is not None:
    stream.write(data)
    data = wf.readframes(CHUNK)

# 停止数据流
stream.stop_stream()
stream.close()

# 关闭PyAudio
p.terminate()