"""
This code is for automatically committing every day while I am at the boot camp.
"""

from os import system
import time


def job():
    print('{:-^60}'.format(' Git Contribution: make md file, git add, git commit, git push '))
    prefix: str = str(time.strftime('%Y-%m-%d-%a', time.localtime(time.time())))
    d_day, last_day = 8, 29
    month, today = int(prefix[5:7]), int(prefix[8:10])
    start: bool = False
    head: str = str()
    content: str = str()
    if month == 6:
        count_day: int = d_day + 30 - today
        head: str = '# D-' + str(count_day)
        content: str = head + '\n삭제 또는 작성 예정\n'
    elif month == 7:
        if today < d_day:
            count_day: int = d_day - today
            head: str = '# D-' + str(count_day)
            content: str = head + '\n삭제 또는 작성 예정\n'
        elif last_day >= today >= d_day:
            count_day: int = today - d_day + 1
            # head_legacy: str = '# :gun: D+' + str(count_day - 1) + ' (훈련소에서 ' + str(count_day) + ' 번째날)'
            head: str = '# :gun: 훈련소에서 ' + str(count_day) + '번째날 (D+' + str(count_day - 1) + ')'
            content: str = head + '\n내용은 지금쯤 훈련소에서 열심히 일기를 쓰고, 그 내용을 바탕으로 쓸 예정입니다.\n'
        elif today == 30 or today == 31:
            head: str = '# Review'
            content: str = head + '\n삭제 또는 작성 예정\n'
    else:
        print('Wrong month.')
        exit()

    folder: str = 'Diary\\'
    file_name: str = prefix + '.md'
    file_path: str = folder + file_name

    # Do not use quotation marks as they are included in the content as well.
    # command_legacy: str = 'echo ' + content + ' > ' + file_path
    # If there is a newline character, the file is not created.
    command: str = 'echo ' + head + ' > ' + file_path
    system(command) #; print(command)
    command: str = 'git add ' + file_path
    system(command) #; print(command)
    command: str = 'git commit -m "create ' + file_name + '"'
    system(command) #; print(command)
    command: str = 'git push origin master'
    system(command) #; print(command)
