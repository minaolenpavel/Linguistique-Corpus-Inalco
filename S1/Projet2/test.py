TERM_PARTICIPE_PASSE = ("é", "ée", "és", "ées", "t", "te", "ts", "tes", "i", "ie", "is", "ies", "s", "se", "ses", "u", "ue", "us", "ues")
AUXILIAIRES = ("suis", "es", "est", "sommes", "êtes", "sont",  "été", "étais", "étais", "était", "étions", "étiez", "étaient","serai", "seras", "sera", "serons", "serez", "seront",  "serais", "serais", "serait", "serions", "seriez", "seraient",  "sois", "sois", "soit", "soyons", "soyez", "soient", "ai", "as", "a", "avons", "avez", "ont", "eu", "avais", "avais", "avait", "avions", "aviez", "avaient", "aurai", "auras", "aura", "aurons", "aurez", "auront",  "aurais", "aurais", "aurait", "avions", "aviez", "auraient", "aie", "aies", "ait", "ayons", "ayez", "aient", "n'est", "n'ai", "n'as", "n'a", "n'avons", "n'avez", "n'ont", "n'étais", "n'était", "n'étions", "n'étiez", "n'étaient", "n'aurai", "n'auras", "n'aura", "n'aurons", "n'aurez", "n'auront", "n'aurais", "n'aurais", "n'aurait", "n'avions", "n'aviez", "n'auraient", "n'aie", "n'aies", "n'ait", "n'ayons", "n'ayez", "n'aient")
TERM_1_PERSON_PLURAL = "ons"
TERM_2_PERSON_PLURAL = "ez"
TERM_3_PERSON_PLURAL = ("ent", "ont")

word = "ont"

if word.endswith(TERM_3_PERSON_PLURAL):
    print("ok")

