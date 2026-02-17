def count_inventory(fruit_list: list[str]) -> dict[str, int]: 
    d = {} 
    for f in fruit_list: 
        d[f] = d.get(f, 0) + 1 
    return d 

Teamname-{CodeTrio}
