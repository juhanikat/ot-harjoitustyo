```mermaid
sequenceDiagram
    main->> HKLLaiteHallinto: HKLLaiteHallinto()
    main ->> LataajaLaite: LataajaLaite()
    main ->> LukijaLaite: LukijaLaite()
    main->> LukijaLaite: LukijaLaite()
    main ->> HKLLaiteHallinto: lisaa_lataaja()
    main ->> HKLLaiteHallinto: lisaa_lukija()
    main ->> HKLLaiteHallinto: lisaa_lukija()
    main ->> Kioski: Kioski()
    main ->> Kioski: osta_matkakortti("Kalle")
    Kioski ->> main: Matkakortti("Kalle")
    main ->> LataajaLaite: lataa_arvoa(kallen_kortti, 3)
    LataajaLaite ->> Matkakortti: kasvata_arvoa(3)
    main ->> LukijaLaite: osta_lippu(kallen_kortti, 0)
    LukijaLaite ->> Matkakortti: vahenna_arvoa(1.5)
    LukijaLaite -->> main: True
    main ->> LukijaLaite: osta_lippu(kallen_kortti, 2)
    LukijaLaite -->> main: False
    




    
```