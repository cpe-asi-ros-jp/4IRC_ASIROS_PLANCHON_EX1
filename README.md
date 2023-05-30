# 4IRC_ASIROS_PLANCHON_EX1
## UDP
### Controle & sporadique
L'exemple peut-être lancé avec les fichiers `udp_controller_simple.py` et `udp_equipment_simple.py` ou directement `start_simple.py`

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
L'exemple peut-être lancé avec les fichiers `udp_controller_video.py` et `udp_equipment_video.py` ou directement `start_video.py`

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
### Controle & sporadique
L'exemple peut-être lancé avec les fichiers `tcp_controller_simple.py` et `tcp_equipment_simple.py` ou directement `start_simple.py`

```mermaid
sequenceDiagram
    Controller->>Controller: Ouvre un socket TCP
    Equipement->>+Equipement: Démarre
    Equipement-->>Controller: Se connecte au socket TCP
    Equipement-->>Controller: (sur la connection TCP) envoi "on"
    loop Periodiquement
        Equipement-->>Controller: (sur la connection TCP) signale qu'il fonctionne
        alt Bouton presse
            Equipement-->>Controller: (sur la connection TCP) signale qu'un bouton a été pressé
        end
    end
    Equipement-->>Controller: (sur la connection TCP) envoi "off"
    Equipement-->>Controller: (clos le socket TCP)
    Equipement->>-Equipement: S'arrête
```

### Flux
L'exemple peut-être lancé avec les fichiers `tcp_controller_video.py` et `tcp_equipment_video.py` ou directement `start_video.py`

```mermaid
sequenceDiagram
    Controller->>Controller: Ouvre un socket TCP
    Equipement->>+Equipement: Démarre
    Equipement-->>Controller: Se connecte au socket TCP
    Equipement->>Controller: Envoie le format de la vidéo (un format avec gestion des parties incomplètes ou corrompues E.G mkv)
    Controller-->Equipement: Confirme la bonne réception du format / métadonnées
    loop Pour chaque frame video
        Equipement->>Equipement: Compresse la frame
        Equipement->>Controller: Envoie la frame
        Controller->>Controller: Conversion de la frame dans un format vidéo qui support les erreurs / frames manquantes
    end
    Equipement-->>Controller: (clos le socket TCP)
    Equipement->>-Equipement: S'arrête
```

## Avis
TCP devrait être utilisé pour les ressources critiques et ce qui ne devrait pas être loupé (les communications de contrôle qui ne sont pas périodiques par exemple) ou pour les évenements sporadiques. UDP devrait être plutôt utilisé pour les évenements sporadiques tel qu'un message "alive", ou pour la vidéo par exemple, une frame perdue ce n'est pas grave.