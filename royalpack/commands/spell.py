import royalnet.engineer as engi
import royalspells
import royalpack.bolts as rb


@rb.capture_errors
@engi.TeleportingConversation
async def spell(*, _msg: engi.Message, spellname: str, **__):
    """
    Genera una spell casuale!
    """
    s = royalspells.Spell(spellname)

    rows: list[str] = [f"✨ \uE01B{s.name}\uE00B"]

    if s.damage_component:
        dmg: royalspells.DamageComponent = s.damage_component
        constant_str: str = f"{dmg.constant:+d}" if dmg.constant != 0 else ""
        rows.append(f"Danni: {dmg.dice_number}d{dmg.dice_type}{constant_str}"
                    f" {', '.join(dmg.damage_types)}")
        rows.append(f"Precisione: {dmg.miss_chance}%")
        if dmg.repeat > 1:
            rows.append(f"Multiattacco: ×{dmg.repeat}")
        rows.append("")

    if s.healing_component:
        heal: royalspells.HealingComponent = s.healing_component
        constant_str: str = f"{heal.constant:+d}" if heal.constant != 0 else ""
        rows.append(f"Cura: {heal.dice_number}d{heal.dice_type}{constant_str} HP")
        rows.append("")

    if s.stats_component:
        stats: royalspells.StatsComponent = s.stats_component
        rows.append("Il caster riceve: ")
        for stat_name in stats.stat_changes:
            rows.append(f"{stat_name}{stats.stat_changes[stat_name]}")
        rows.append("")

    if s.status_effect_component:
        se: royalspells.StatusEffectComponent = s.status_effect_component
        rows.append("Infligge al bersaglio: ")
        rows.append(f"{se.effect} ({se.chance}%)")
        rows.append("")

    await _msg.reply(text="\n".join(rows))


__all__ = ("spell",)
