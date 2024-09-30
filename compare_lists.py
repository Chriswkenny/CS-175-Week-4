#Christopher Kenny
#CS 175
#Setting lists

list1 = [1, 2, 3]
list2 = [1, 2, 3, 4]
list3 = [3, 4, 2, 1]
list4 = ["fee", "fo", "fi"]
list5 = ["fee", "fo", "fi", "fum"]


def compare_list(list1, list2):
  if len(list1) != len(list2):
    return False
  sorted_list1 = sorted(list1)
  sorted_list2 = sorted(list2)

  for i in range(len(sorted_list1)):
    if sorted_list1[i] != sorted_list2[i]:
      return False
  return True

print(compare_list(list1, list1))
print(compare_list(list1, list2))
print(compare_list(list2, list3))
print(compare_list(list3, list4))
print(compare_list(list4, list5))
