def find_common_participants(g1, g2, razd=","):
    participants1 = g1.split(razd)
    participants2 = g2.split(razd)

    obsch=list(set(participants1).intersection(participants2))
    obsch.sort()

    return obsch

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group,razd="|"))