# 4IRC_ASIROS_PLANCHON_EX1
## UDP
### Controle & sporadique
```mermaid
sequenceDiagram
    Controller->>Controller: Ouvre un socket UDP
    Equipement->>+Equipement: Démarre
    Equipement-->>Controller: (sur le socket UDP) envoi "on"
    loop Periodiquement
        Equipement-->>Controller: (sur le socket UDP) signale qu'il fonctionne
        alt Bouton presse
            Equipement-->>Controller: (sur le socket UDP) signale qu'un bouton a été pressé
        end
    end
    Equipement-->>Controller: (sur le socket UDP) envoi "off"
    Equipement->>-Equipement: S'arrête
```

### Flux
```mermaid
sequenceDiagram
    Controller->>Controller: Ouvre un socket UDP
    Equipement->>+Equipement: Démarre
    Equipement->>Controller: Envoie le format de la vidéo (un format avec gestion des parties incomplètes ou corrompues E.G mkv)
    Controller-->Equipement: Confirme la bonne réception du format / métadonnées
    loop Pour chaque frame video
        Equipement->>Equipement: Compresse la frame
        Equipement->>Controller: Envoie la frame
        Controller->>Controller: Conversion de la frame dans un format vidéo qui support les erreurs / frames manquantes
    end
    Equipement->>-Equipement: S'arrête
```
Un format vidéo qui supporte les erreurs peut-être du mkv par exemple qui est robuste au erreurs et frames manquantes ou du mp4 en mode "Fast Start" (avec les metadonnées en premier). 

## TCP

## Comparaison & avis
