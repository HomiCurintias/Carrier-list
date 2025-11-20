import jester

routes:
    get "/":
        resp """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carrier list</title>
    <link rel="icon" type="image/png" href="/icon.png">

    <style>
        body {
            background: #ffffffff;
            font-family: Arial, Helvetica, sans-serif;
            margin: 0;
            padding: 20px;
            text-align: center;
        }

        .container {
            background: white;
            max-width: 600px;
            margin: auto;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }

        h1 {
            margin: 10px 0;
        }

        h2 {
            margin: 5px 0 20px 0;
            color: #555;
            font-weight: normal;
        }

        .sep {
            width: 80%;
            height: 2px;
            background: #ddd;
            margin: 25px auto;
            border-radius: 5px;
        }

        a {
            color: #0077ff;
            text-decoration: none;
            font-size: 20px;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Carrier list</h1>
        <h2>By Silva</h2>

        <div class="sep"></div>

        <h1>1. The Golden</h1>
        <h2>by BoBoBoBoBoBoBo</h2>

        <div class="sep"></div>
        <h1>2. Widestep</h1>
        <h2>by Demishio</h2>

        <div class="sep"></div>
        <h1>3. Cosmic Cyclone</h1>
        <h2>by APTeamOfficial</h2>

        <div class="sep"></div>
        <h1>4. The Hell Zone</h1>
        <h2>by Stormfly</h2>

        <div class="sep"></div>
        <h1>5. Blade of Justice</h1>
        <h2>by Manix648</h2>

        <div class="sep"></div>
        <h1>6. moment</h1>
        <h2>by Lexycat</h2>

        <div class="sep"></div>
        <h1>7. Bloodbath</h1>
        <h2>by Riot</h2>

        <div class="sep"></div>
        <h1>8. The Hell Dignity</h1>
        <h2>by Stormfly</h2>

        <div class="sep"></div>
        <h1>9. Reflective</h1>
        <h2>by Mojitoz</h2>

        <div class="sep"></div>
        <h1>10. NecropoliX</h1>
        <h2>by namtar</h2>

        <div class="sep"></div>
        <h1>11. The Lost Existence</h1>
        <h2>by JonathanGD</h2>

        <div class="sep"></div>
        <h1>12. Cataclysm</h1>
        <h2>by Ggb0y</h2>

        <div class="sep"></div>
        <h1>13. Niwa</h1>
        <h2>by Teno</h2>

        <div class="sep"></div>
        <h1>14. Acu</h1>
        <h2>by neigefeu</h2>

        <div class="sep"></div>
        <h1>15. ICE Carbon Diablo X</h1>
        <h2>by -Roadbose-</h2>

        <div class="sep"></div>
        <h1>16. CraZy III</h1>
        <h2>by DavJT</h2>

        <div class="sep"></div>
        <h1>17. Infinity LoL</h1>
        <h2>by Guimonteiro</h2>

        <div class="sep"></div>
        <h1>18. Necropolis</h1>
        <h2>by IIINePtunEIII</h2>

        <div class="sep"></div>
        <h1>19. Acropolis</h1>
        <h2>by Zobros</h2>

        <div class="sep"></div>
        <h1>20. Ultra funky</h1>
        <h2>by Guimonteiro</h2>

        <div class="sep"></div>
        <h1>21. Supersonic</h1>
        <h2>by ZenthicAlpha</h2>

        <div class="sep"></div>
        <h1>22. SlaughterHouse</h1>
        <h2>by Havok</h2>

        <div class="sep"></div>
        <h1>23. Death Note</h1>
        <h2>by Ruf</h2>

        <div class="sep"></div>
        <h1>24. Manic</h1>
        <h2>by Guimonteiro</h2>

        <div class="sep"></div>
        <h1>25. Poltergeist</h1>
        <h2>by Andromeda GMD</h2>

        <div class="sep"></div>
        <h1>26. Plasma Pulse</h1>
        <h2>by Giron</h2>

        <div class="sep"></div>
        <h1>27. Windy Landscape</h1>
        <h2>by Woogi1411</h2>

        <div class="sep"></div>
        <h1>28. CraZy II</h1>
        <h2>by DavJT</h2>

        <div class="sep"></div>
        <h1>29. Stalemate</h1>
        <h2>by Nox</h2>

        <div class="sep"></div>
        <h1>30. The Furious</h1>
        <h2>by Knobbelboy</h2>

        <div class="sep"></div>
        <h1>31. I Cant Fix You</h1>
        <h2>by IronIngot</h2>

        <div class="sep"></div>
        <h1>32. Shonic wave</h1>
        <h2>by Guimonteiro</h2>

        <div class="sep"></div>
        <h1>33. Cant let troll 3xrow</h1>
        <h2>by Guimonteiro</h2>

        <div class="sep"></div>
        <h1>34. Whatsapp circles</h1>
        <h2>by XKYY</h2>

        <div class="sep"></div>
        <h1>35. Hellaven II</h1>
        <h2>by clasi</h2>

        <div class="sep"></div>
        <h1>36. CraZy</h1>
        <h2>by DavJT</h2>

        <div class="sep"></div>
        <h1>37. Cant troll twice</h1>
        <h2>by Guimonteiro</h2>

        <div class="sep"></div>
        <h1>38. widder</h1>
        <h2>by 2003devin</h2>

        <div class="sep"></div>
        <h1>39. Potatoguy adven 3</h1>
        <h2>by BearWare</h2>

        <div class="sep"></div>
        <h1>40. Nine Circles</h1>
        <h2>by Zobros</h2>

        <div class="sep"></div>
        <h1>41. Jawbreaker</h1>
        <h2>by ZenthicAlpha</h2>

        <div class="sep"></div>
        <h1>42. Cant let troll</h1>
        <h2>by Defectum</h2>

        <div class="sep"></div>
        <h1>43. Megalovania</h1>
        <h2>by EternaswipVMAX</h2>

        <div class="sep"></div>
        <h1>44. Hellaven</h1>
        <h2>by clasi</h2>

        <div class="sep"></div>
        <h1>45. Rhombus</h1>
        <h2>by Theixn</h2>

        <div class="sep"></div>
        <h1>46. BP night</h1>
        <h2>by -</h2>

        <div class="sep"></div>
        <h1>47. Aleph</h1>
        <h2>by AlemaneiroGD</h2>

        <div class="sep"></div>
        <h1>48. VeritY</h1>
        <h2>by Serponge</h2>

        <div class="sep"></div>
        <h1>49. Sakupen Egg</h1>
        <h2>by Sivlol</h2>

        <div class="sep"></div>
        <h1>50. Extreme Park</h1>
        <h2>by Rabbitical</h2>

        <div class="sep"></div>

        <h3><a href="/info">Info</a></h3>
    </div>

</body>
</html>"""

    get "/info":
        resp """<p><h1>this website was made by: ryofreefire32@gmail.com (Silva)</h1></p> <p><h2><a href="/">Back</h2>"""