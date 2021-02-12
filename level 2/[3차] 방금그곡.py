def solution(m, musicinfos):

    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    answer=[]
    def find_time(m1, m2):
        m1 = m1.split(':')
        m2 = m2.split(':')
        return (int(m1[1])+int(m1[0])*60) - (int(m2[1])+int(m2[0])*60)
    print(m)
    for music in musicinfos:
        music = music.split(',')
        music[3] = music[3].replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        time = find_time(music[1],music[0])
        print(music)
        print(time)
        len_music = len(music[3])
        line = music[3]*(time//len_music) + music[3][0:time%len_music]
        print(line)
        if m in line:
            print(music[2])
            answer.append((music[2], time))
    if len(answer) == 0: return None
    answer.sort(key=lambda x:x[1])
    print(answer)
    return answer[0]


if __name__ == '__main__':
    m = "ABC"
    musicinfos =  ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    solution(m, musicinfos)