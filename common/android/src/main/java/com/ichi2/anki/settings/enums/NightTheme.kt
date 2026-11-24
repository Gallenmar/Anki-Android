// SPDX-License-Identifier: GPL-3.0-or-later

package com.ichi2.anki.settings.enums

import com.ichi2.anki.common.android.R

/** [R.array.night_theme_values] */
enum class NightTheme(
    override val entryResId: Int,
    override val styleResId: Int,
) : Theme {
    BLACK(R.string.theme_black_value, R.style.Theme_AnkiDroid_Black),
    DARK(R.string.theme_dark_value, R.style.Theme_AnkiDroid),
    EINK(R.string.theme_eink_night_value, R.style.Theme_AnkiDroid_Eink),
    DRACULA(R.string.theme_dracula_value, R.style.Theme_AnkiDroid_Dracula),
    T3_CHAT(R.string.theme_t3_chat_value, R.style.Theme_AnkiDroid_T3Chat),
    MONOKAI(R.string.theme_monokai_value, R.style.Theme_AnkiDroid_Monokai),
    MONOKAI_PRO(R.string.theme_monokai_pro_value, R.style.Theme_AnkiDroid_MonokaiPro),
}
