def solution(numbers):
    answer = []
    for num in numbers:
        if num%2==0:
            answer.append(num+1)
        else:
            bin_num=bin(num)[2:]
            bin_num="0"+bin_num
            idx1=bin_num.rfind("0")
            bin_num=list(bin_num)
            bin_num[idx1]="1"
            bin_num[idx1+1]="0"
            str="".join(bin_num)
            final_num=int(str, 2)
            answer.append(final_num)
    return answer