import royalnet.engineer as engi
import royalspells


@engi.TeleportingConversation
async def spell(*, _msg: engi.Message, spellname: str, **__):
    """
    Genera una spell casuale!
    """
    spell = royalspells.Spell(spellname)

    rows: list[str] = [f"✨ {spell.name}"]

    if spell.damage_component:
        dmg: royalspells.DamageComponent = spell.damage_component
        constant_str: str = f"{dmg.constant:+d}" if dmg.constant != 0 else ""
        rows.append(f"Danni: {dmg.dice_number}d{dmg.dice_type}{constant_str}"
                    f" {', '.join(dmg.damage_types)}")
        rows.append(f"Precisione: {dmg.miss_chance}%")
        if dmg.repeat > 1:
            rows.append(f"Multiattacco: ×{dmg.repeat}")
        rows.append("")

    if spell.healing_component:
        heal: royalspells.HealingComponent = spell.healing_component
        constant_str: str = f"{heal.constant:+d}" if heal.constant != 0 else ""
        rows.append(f"Cura: {heal.dice_number}d{heal.dice_type}{constant_str} HP")
        rows.append("")

    if spell.stats_component:
        stats: royalspells.StatsComponent = spell.stats_component
        rows.append("Il caster riceve: ")
        for stat_name in stats.stat_changes:
            rows.append(f"{stat_name}{stats.stat_changes[stat_name]}")
        rows.append("")

    if spell.status_effect_component:
        se: royalspells.StatusEffectComponent = spell.status_effect_component
        rows.append("Infligge al bersaglio: ")
        rows.append(f"{se.effect} ({se.chance}%)")
        rows.append("")

    await _msg.reply(text="\n".join(rows))


__all__ = ("spell",)
