import re
def solution(file_names):
    answer=0

    filt = re.compile(r'([a-zA-Z\-\n\s.]+)([0-9]{0,5})(.*)')
    files = []
    for file_name in file_names:
        files.extend(filt.findall(file_name))
    files.sort(key=lambda x: (x[0].lower(), int(x[1])))
    for i in files:
        answer=[''.join(i) for i in files]
    return answer