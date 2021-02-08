def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        line = ''
        for i in tree:
            if i in skill:
                line+=str(i)
        print(line)
        if skill.startswith(line):
            answer+=1

    print(answer)

    return answer


if __name__ == '__main__':
    skill = 'CBD'
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    solution(skill, skill_trees)