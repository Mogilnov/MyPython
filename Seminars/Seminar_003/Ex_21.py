list_1 = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},
          {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
list_2 = set()
for i in list_1:
    list_2.add(list(i.values())[0])
print(list_2)
