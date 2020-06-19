

# ar = []
# for i in range(16):
#     ar.append(i)
#
# br=[]
# for i in range(15):
#     s = input()
#     br.append(int(s))
# k=0
# for i in ar:
#     k=0
#     for j in range(15):
#         if br[j]==i:
#             d=j-i
#             if d%2==0:
#                 print(1,"even")
#                 k=1
#                 break
#     if k==0:
#         print(0,"odd")

# def is_permutation(p):
#     return (set(p) == set(range(len(p))))
#
# print(is_permutation([0]))
# print(is_permutation([0, 2, 1]))
# print(is_permutation([1, 2, 3]))

all=list()
def solution(position):
    k = 0
    for i in range(len(position)-2):
        for j in range(i+1,len(position)-1):
            if position[i]>position[j]:
              if position[i] not in all:
                  all.append(position[i])
              t=position[i]
              position[i]=position[j]
              position[j]=t
              k=k+1

    # if (k%2)==0:
    #     # return True
    return all


# def is_even(p):
#     count = 0
#     for i in range(len(p)):
#           m = i;
#     for j in range(i + 1, len(p)):
#           if p[m] > p[j]:
#                m = j
#           if m != i:
#             p[i],p[m]=p[m],p[i]
#             count += 1
#     if count % 2 == 0:
#         return True
#     else:
#         return False

# for i in range(len(p)-1):
#         for j in range(i+1, len(p)):
#          if p[i]>p[j]:
#            temp=p[i]
#            p[i]=p[j]
#            p[j]=temp
#            parity=parity+1

# print(is_even([0,3,2,4,5,6,7,1,9,8]))
# if(is_even([0,3,2,4,5,6,7,1,9,8])):
#     print(all)
# print(is_even([4, 2, 1, 0, 3, 5]))
# print(solution([0,3,2,4,5,6,7,1,9,8]))
print(solution([1,2,3,4,5,6,7,8,13,9,11,12,10,14,15,0]))
