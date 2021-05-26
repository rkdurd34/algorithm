# song = '동해물과 백두산이 마르고 닳도록\n하느님이 보우하사 우리나라 만세\n무궁화 삼천리 화려강산\n대한사람 대한으로 길이 보전하세'
# song_list = song.split('\n')
# s1 = song_list[0]
# s2 = song_list[1]
# s3 = song_list[2]
# s4 = song_list[3]
# print('song_list : ', song_list)
# print()


# print(f"{s1}, \n{s2}, \n{s3}, \n{s4}")
import sys
n, time = sys.stdin.readline().strip().split()
print(n)
music_list = []
for i in range(int(n)):
    music_list.append(sys.stdin.readline().strip())
print(n, time, music_list)
