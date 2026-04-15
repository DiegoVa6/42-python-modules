def ft_count_harvest_recursive(a=int(input("Days until harvest: ")), i=1):
    if i > a:
        print("Harvest time!")
    else:
        print("Day", i)
        ft_count_harvest_recursive(a, i + 1)
