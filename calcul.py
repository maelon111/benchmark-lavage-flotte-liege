#!/usr/bin/env python3
"""Lavage de voitures : eau, CO2e, temps et argent sur un an (benchmark-lavage-flotte-liege).

Compare un passage en station (car-wash) avec un lavage sans eau sur place.
Toutes les hypothèses sont des paramètres ; valeurs par défaut et sources dans data/hypotheses.csv.

    python3 calcul.py --vehicules 20 --lavages 12                 # flotte d'entreprise
    python3 calcul.py --vehicules 10 --lavages 12 --collegues     # 10 collègues, chacun paie
    python3 calcul.py --vehicules 1 --lavages 12 --prix-station 9  # un particulier
"""
import argparse

PRIX_PARKWASH = {"petite": 16, "standard": 17, "suv": 19, "van": 25, "utilitaire": 31}
REMISES = [(1000, .35), (200, .30), (50, .25), (20, .20), (10, .15), (5, .10)]


def remise_groupe(vehicules, abonnement_hebdo=False):
    """Remise publique ParkWash : la meilleure s'applique, sans cumul."""
    r = next((taux for seuil, taux in REMISES if vehicules >= seuil), 0.0)
    return max(r, 0.10 if abonnement_hebdo else 0.0)


def bilan(vehicules, lavages, part_electrique=0.0, eau_l=150, co2_station=0.9, co2_trajet=1.3,
          co2_sans_eau=0.15, minutes=30, prix_station=12.0, carburant=0.70, vehicule="standard",
          abonnement_hebdo=False):
    n = vehicules * lavages
    thermiques = 1 - part_electrique
    carbu = carburant * thermiques + 0.30 * part_electrique
    prix_pw = PRIX_PARKWASH[vehicule] * (1 - remise_groupe(vehicules, abonnement_hebdo))
    return {
        "lavages": n,
        "station": {
            "eau_l": n * eau_l,
            "co2_kg": n * (co2_station + thermiques * co2_trajet),
            "heures": n * minutes / 60,
            "eur": n * (prix_station + carbu),
        },
        "sans_eau_sur_place": {
            "eau_l": 0,
            "co2_kg": n * co2_sans_eau,
            "heures": 0,
            "eur": n * prix_pw,
            "prix_par_lavage": prix_pw,
        },
    }


def fr(x, d=0):
    s = f"{x:,.{d}f}".replace(",", " ").replace(".", ",")
    return s


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--vehicules", type=int, default=20)
    p.add_argument("--lavages", type=int, default=12, help="lavages par véhicule et par an")
    p.add_argument("--electriques", type=float, default=0.0, help="part de voitures électriques, 0 à 1")
    p.add_argument("--vehicule", choices=PRIX_PARKWASH, default="standard")
    p.add_argument("--prix-station", type=float, default=12.0)
    p.add_argument("--minutes", type=float, default=30, help="trajet + attente par passage en station")
    p.add_argument("--cout-horaire", type=float, default=0, help="coût d'une heure de travail (entreprise)")
    p.add_argument("--abonnement-hebdo", action="store_true")
    p.add_argument("--collegues", action="store_true", help="chacun paie son lavage : coût pour l'entreprise = 0")
    a = p.parse_args()

    b = bilan(a.vehicules, a.lavages, a.electriques, minutes=a.minutes, prix_station=a.prix_station,
              vehicule=a.vehicule, abonnement_hebdo=a.abonnement_hebdo)
    s, w = b["station"], b["sans_eau_sur_place"]
    print(f"{a.vehicules} véhicule(s) × {a.lavages} lavages par an = {b['lavages']} lavages\n")
    print(f"{'':28} {'Station':>12} {'Sans eau sur place':>20}")
    print(f"{'Eau':28} {fr(s['eau_l']) + ' L':>12} {'0 L':>20}")
    print(f"{'CO2e':28} {fr(s['co2_kg'], 1) + ' kg':>12} {fr(w['co2_kg'], 1) + ' kg':>20}")
    print(f"{'Temps (trajet + attente)':28} {fr(s['heures'], 1) + ' h':>12} {'0 h':>20}")
    print(f"{'Argent (lavage + carburant)':28} {fr(s['eur'], 2) + ' €':>12} {fr(w['eur'], 2) + ' €':>20}")
    print(f"\nPrix ParkWash par lavage, remise comprise : {fr(w['prix_par_lavage'], 2)} €")
    print(f"Évité : {fr(s['eau_l'])} L d'eau, {fr(s['co2_kg'] - w['co2_kg'], 1)} kg CO2e, "
          f"{fr(s['heures'], 1)} h (≈ {fr(s['heures'] / 7.6, 1)} journées de 7,6 h)")
    if a.collegues:
        print(f"Coût pour l'entreprise : 0 € ; écart par personne : "
              f"{fr((w['eur'] - s['eur']) / a.vehicules / 12, 2)} € par mois")
    if a.cout_horaire:
        print(f"Valeur du temps rendu à {fr(a.cout_horaire)} €/h : {fr(s['heures'] * a.cout_horaire)} €")


if __name__ == "__main__":
    main()
