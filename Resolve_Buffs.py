def resolve_damage_buffs(buffs, debuffs, other_buffs, other_debuffs):
    enemy_calc_buffs = []
    for buff in buffs:
        if buff not in [1, 2, 3, 4, 8]:
            enemy_calc_buffs.append(buff)

    player_calc_buffs = []
    for buff in other_buffs:
        if buff in [1, 2, 3, 4, 8]:
            player_calc_buffs.append(buff)

    calc_buffs = player_calc_buffs + enemy_calc_buffs

    enemy_calc_debuffs = []
    for debuff in debuffs:
        if debuff not in [1, 2, 3, 4, 8]:
            enemy_calc_debuffs.append(debuff)

    player_calc_debuffs = []
    for debuff in other_debuffs:
        if debuff in [1, 2, 3, 4, 8]:
            player_calc_debuffs.append(debuff)

    calc_debuffs = player_calc_debuffs + enemy_calc_debuffs

    for i in range(1, 8):
        if i in calc_debuffs and i in calc_buffs:
            calc_buffs.remove(i)
            calc_buffs.remove(i)

    return [calc_buffs, calc_debuffs]


