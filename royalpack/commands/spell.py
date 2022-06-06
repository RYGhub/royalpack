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

    rows: list[str] = [f"✨ \uE012\uE01B{s.name}\uE00B\uE002"]

    if s.damage_component:
        dmg: royalspells.DamageComponent = s.damage_component
        constant_str: str = f"{dmg.constant:+d}" if dmg.constant != 0 else ""
        rows.append(f"Danni: \uE01B{dmg.dice_number}d{dmg.dice_type}{constant_str}\uE00B"
                    f" {', '.join(dmg.damage_types)}")
        rows.append(f"Precisione: \uE01B{dmg.miss_chance}%\uE00B")
        if dmg.repeat > 1:
            rows.append(f"Multiattacco: \uE01B×{dmg.repeat}\uE00B")
        rows.append("")

    if s.healing_component:
        heal: royalspells.HealingComponent = s.healing_component
        constant_str: str = f"{heal.constant:+d}" if heal.constant != 0 else ""
        rows.append(f"Cura: \uE01B{heal.dice_number}d{heal.dice_type}{constant_str}\uE00B")
        rows.append("")

    if s.stats_component:
        stats: royalspells.StatsComponent = s.stats_component
        rows.append("Il caster riceve: ")
        for stat_name in stats.stat_changes:
            rows.append(f"\uE01B{stat_name}{stats.stat_changes[stat_name]}\uE00B")
        rows.append("")

    if s.status_effect_component:
        se: royalspells.StatusEffectComponent = s.status_effect_component
        rows.append("Infligge al bersaglio: ")
        rows.append(f"\uE01B{se.effect}\uE00B ({se.chance}%)")
        rows.append("")

    await _msg.reply(text="\n".join(rows))


__all__ = ("spell",)
