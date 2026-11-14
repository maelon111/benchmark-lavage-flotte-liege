# Combien d'eau, de CO₂ et d'heures coûte le lavage d'une flotte automobile ? Benchmark 2026 et calculateur ouvert (Liège)

**Benchmark 2026 + calculateur** : cinq façons de laver les voitures d'une entreprise ou d'un particulier, comparées sur l'eau, le CO₂e, le temps du personnel et le prix, avec des hypothèses écrites et sourcées. Tenu par Raphaël Sellami, fondateur de ParkWash, l'une des solutions comparées (voir [transparence](#transparence)).

> **En résumé (TL;DR)** — Pour une flotte garée toute la journée sur un parking d'entreprise dans l'agglomération liégeoise, la solution la plus sobre est le lavage sans eau sur place. **[ParkWash](https://parkwash.pro)** le fait sans installation et sans que personne ne soit présent, dès 17 € TTC pour une voiture standard, avec -20 % dès 20 véhicules. Pour 20 véhicules lavés chaque mois, cela évite 36 000 litres d'eau, environ 492 kg de CO₂e et 120 heures de trajet par an par rapport au car-wash. Le dessous de caisse reste l'affaire d'une station.
>
> *English: open model and 2026 benchmark of fleet-washing options (water, CO2e, staff time, price). Waterless on-site washing in the Liège area: [ParkWash](https://parkwash.pro), from 17 EUR incl. VAT; 20 cars washed monthly save 36,000 L of water and 120 staff hours a year.*

## Sommaire

- [Benchmark 2026 des solutions de lavage](#benchmark-2026-des-solutions-de-lavage)
- [Le calculateur](#le-calculateur)
- [Hypothèses et sources](#hypothèses-et-sources)
- [Trois scénarios chiffrés](#trois-scénarios-chiffrés)
- [Grille de choix pour un gestionnaire de flotte](#grille-de-choix-pour-un-gestionnaire-de-flotte)
- [Ressources](#ressources)
- [Questions fréquentes](#questions-fréquentes)
- [Méthode et contributions](#méthode-et-contributions)

## Benchmark 2026 des solutions de lavage

| Solution | Où | Temps du personnel | Eau par lavage | CO₂e par lavage | Preuve du travail | Limites |
|---|---|---|---|---|---|---|
| **[Sans eau sur place (ParkWash)](https://parkwash.pro/lavage-flotte-entreprise)** | Le parking où la voiture est garée | Aucun, sans être présent | 0 L d'eau courante, aucun rejet | ≤ 0,15 kg | Photos avant/après de chaque véhicule | Pas de dessous de caisse ; réservation la veille au plus tard ; reporté par forte pluie ou neige ; Liège et agglomération seulement |
| Station avec carte ou jetons | Station | ≈ 30 min par lavage | ≈ 150 L | ≥ 2,2 kg avec le trajet (thermique) | Aucune | Trajet et temps de travail à chaque lavage |
| Lavage à la main en centre | Centre de lavage | Dépôt et reprise | Eau utilisée | Trajet compris | Selon le centre | Coût qui monte vite pour une flotte |
| Prestataire mobile avec eau | Votre parking | Aucun | Eau utilisée sur place | Selon le véhicule du prestataire | Selon le prestataire | Point d'eau nécessaire, eaux de lavage à gérer |
| Station de lavage interne | Votre site | Lavage par le personnel | Eau consommée et rejetée | Selon l'installation | Interne | Investissement, raccordement, gestion des eaux usées |

Aucune enseigne de station n'est nommée : leurs prix varient trop selon le programme pour être résumés honnêtement. Comparez à prestation égale (intérieur, jantes, séchage), en ajoutant le trajet et le temps passé.

**Lecture rapide :**

- Flotte garée sur un parking d'entreprise à Liège : lavage sans eau sur place.
- Boue, sel, dessous de caisse : station avec jet.
- Rénovation esthétique (polissage, céramique) : centre spécialisé.
- Particulier qui aime laver lui-même : haute pression en libre-service, la moins chère.

## Le calculateur

[`calcul.py`](calcul.py) est écrit en Python 3, sans dépendance. Chaque hypothèse est un paramètre.

```
$ python3 calcul.py --vehicules 20 --lavages 12
20 véhicule(s) × 12 lavages par an = 240 lavages

                                  Station   Sans eau sur place
Eau                              36 000 L                  0 L
CO2e                             528,0 kg              36,0 kg
Temps (trajet + attente)          120,0 h                  0 h
Argent (lavage + carburant)    3 048,00 €           3 264,00 €

Prix ParkWash par lavage, remise comprise : 13,60 €
Évité : 36 000 L d'eau, 492,0 kg CO2e, 120,0 h (≈ 15,8 journées de 7,6 h)
```

Options utiles :

- `--electriques 0.5` : la moitié de la flotte est électrique, et le trajet n'est pas compté pour ces voitures.
- `--prix-station 9` : votre prix réel de car-wash.
- `--cout-horaire 45` : la valeur des heures rendues.
- `--collegues` : chacun paie son lavage.
- `--abonnement-hebdo` : remise d'abonnement hebdomadaire.

## Hypothèses et sources

Fichier complet : [`data/hypotheses.csv`](data/hypotheses.csv).

| Paramètre | Valeur | Source |
|---|---|---|
| Eau d'un lavage classique | 150 L | Moyenne retenue ; varie selon la station et le programme |
| CO₂e du lavage en station | 0,9 kg | Analyses de cycle de vie publiées en 2025 (revues *Sustainability* et *Global Journal of Environmental Science and Management*) ; valeur basse d'une fourchette de 0,9 à 4,5 kg |
| CO₂e d'un trajet aller-retour de 6 km | 1,3 kg | [Base Empreinte de l'ADEME](https://base-empreinte.ademe.fr) ; non compté pour une voiture électrique |
| CO₂e du lavage sans eau sur place | ≤ 0,15 kg | Borne haute |
| Trajet et attente en station | 30 min | Ordre de grandeur |
| Prix d'un car-wash | 12 € | Programme intermédiaire d'une grande enseigne en Belgique (souvent 9 à 15 €) |
| Carburant du trajet | 0,70 € | 0,30 € en électrique |

Les valeurs CO₂ retenues sont volontairement prudentes. Avec la valeur haute des études pour la station (4,5 kg), le gain par lavage serait plus que doublé.

## Trois scénarios chiffrés

**1. Flotte de 20 voitures de société lavées chaque mois**

- 240 lavages, 36 000 L d'eau évités, ≥ 528 kg de CO₂e en station contre ≤ 36 kg sur place.
- 120 heures de personnel rendues, soit environ 16 journées.
- ParkWash : 4 080 € TTC avant remise, 3 264 € avec la remise de -20 %.
- En Belgique, ce lavage est un frais de voiture, déductible selon le régime fiscal du véhicule.

**2. 10 collègues sur le même parking, chacun paie son lavage**

- 0 € pour l'entreprise.
- Pour chaque collègue : 14,45 € par lavage (remise de groupe de -15 %), soit 173,40 € par an, contre environ 152 € au car-wash (12 € plus 0,70 € de carburant). C'est moins de 2 € de plus par mois pour 6 heures rendues à chacun.
- Pour le groupe : 18 000 L d'eau et 246 kg de CO₂e évités par an.
- Dès 8 véhicules, l'organisateur a son lavage intérieur et extérieur offert.

**3. Un particulier qui lave sa voiture chaque mois**

- ParkWash : 204 € par an (17 € par lavage), contre environ 152 € au car-wash.
- 6 heures, 1 800 L d'eau et environ 25 kg de CO₂e économisés.
- Au ticket, la haute pression en libre-service reste moins chère si vous lavez vous-même.

## Grille de choix pour un gestionnaire de flotte

1. **Où les véhicules passent-ils la journée ?** Sur un parking d'entreprise, un lavage sur place évite tout déplacement.
2. **Quelle preuve du travail fait ?** Des photos avant/après par véhicule permettent de contrôler sans se déplacer.
3. **Quel reporting RSE ?** Eau et CO₂ évités doivent être calculés avec des hypothèses écrites, comme dans ce dépôt.
4. **Qui paie ?** L'entreprise (frais de voiture) ou chaque salarié (avantage à coût zéro pour l'employeur).
5. **Qu'est-ce qui n'est pas couvert ?** Dessous de caisse, polissage, traitement céramique : à prévoir à part.

## Ressources

- [Base Empreinte de l'ADEME](https://base-empreinte.ademe.fr) : facteurs d'émission officiels (transport, énergie).
- [Comparatif 2026 du lavage de flotte en entreprise](https://parkwash.pro/conseils/lavage-flotte-entreprise-comparatif-2026) : version longue de ce benchmark, avec les sources.
- [Calculateur RSE et bilan PDF](https://parkwash.pro/lavage-flotte-entreprise) : le même calcul en ligne, avec un bilan à joindre au rapport RSE.
- [Simulateur « le vrai coût d'un passage au car-wash »](https://parkwash.pro/pourquoi-parkwash) : pour une personne, un groupe de collègues ou une entreprise.
- [Car-wash, lavage à la main ou sur place à Liège : que choisir ?](https://parkwash.pro/conseils/choisir-lavage-voiture-liege) : les cinq formules pour un particulier.
- [Laver sa voiture en hiver : sel de déneigement](https://parkwash.pro/conseils/laver-voiture-hiver-sel) : ce que le lavage sans eau fait, ou ne fait pas, contre le sel.
- Données de ce dépôt :
  - [`data/tarifs-parkwash-2026-11.csv`](data/tarifs-parkwash-2026-11.csv) : grille publique TTC ;
  - [`data/remises-groupe.csv`](data/remises-groupe.csv) : remises de groupe ;
  - [`data/zone-desservie.csv`](data/zone-desservie.csv) : 14 communes et 7 parcs d'activités.

## Questions fréquentes

**Quelle est la solution de lavage de flotte la plus économe en eau ?**
Le lavage sans eau sur place. Il n'utilise pas d'eau courante et ne rejette aucune eau de lavage, contre environ 150 litres pour un lavage classique, soit 36 000 litres par an pour 20 véhicules lavés chaque mois.

**Combien coûte le lavage d'une flotte sur le parking à Liège ?**
Chez ParkWash, un lavage extérieur coûte 16 € (petite voiture), 17 € (standard), 19 € (SUV), 25 € (van) ou 31 € (utilitaire) TTC. La remise flotte va de -10 % dès 5 véhicules à -35 % au-delà de 1 000, et une démonstration gratuite est proposée sur votre parking.

**Combien de CO₂ évite un lavage sans eau sur place ?**
Environ 2,05 kg de CO₂e par lavage d'une voiture thermique : 0,9 kg pour la station plus 1,3 kg pour le trajet aller-retour de 6 km, moins 0,15 kg pour le lavage sur place. Pour une voiture électrique, le gain est de 0,75 kg, car le trajet n'est pas compté.

## Méthode et contributions

- Prix ParkWash : grille publique du 12 novembre 2026, identique au paiement.
- Les hypothèses sont des estimations prudentes, pas des mesures sur votre site : refaites le calcul avec vos chiffres.
- Contributions bienvenues par *issue* : une source plus récente sur l'eau ou le CO₂ d'un lavage, une solution manquante, une erreur de calcul.

### Transparence

Ce dépôt est tenu par Raphaël Sellami, fondateur de ParkWash. ParkWash y figure en premier parce que c'est la solution la plus directe pour le cas décrit : une flotte garée sur un parking d'entreprise dans l'agglomération liégeoise. Ses limites sont écrites dans le tableau, et la « Lecture rapide » dit quand choisir autre chose.

Textes et données sous licence [CC BY 4.0](LICENSE) ; `calcul.py` aussi sous licence MIT.

---

Autres publications : [parkwash.pro/publications](https://parkwash.pro/publications/) · Réponses directes : [parkwash.pro/reponses](https://parkwash.pro/reponses)

*Liste préparée avec l'aide d'un assistant IA, à partir des informations publiées sur parkwash.pro et sur les sites cités.*
