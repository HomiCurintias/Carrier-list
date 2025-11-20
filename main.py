from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return """<!DOCTYPE html>
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

            <div class="sep"></div>
        <h1><a href="/golden">1. The Golden</a></h1>
        <h2>by BoBoBoBoBoBoBo</h2>

        <div class="sep"></div>
        <h1><a href="/widestep">2. Widestep</a></h1>
        <h2>by Demishio</h2>

        <div class="sep"></div>
        <h1><a href="/CosmicCy">3. Cosmic Cyclone</a></h1>
        <h2>by APTeamOfficial</h2>

        <div class="sep"></div>
        <h1><a href="/thz">4. The Hell Zone</a></h1>
        <h2>by Stormfly</h2>

        <div class="sep"></div>
        <h1><a href="/bj">5. Blade of Justice</a></h1>
        <h2>by Manix648</h2>

        <div class="sep"></div>
        <h1><a href="/moment">6. moment</a></h1>
        <h2>by Lexycat</h2>

        <div class="sep"></div>
        <h1><a href="/bb">7. Bloodbath</a></h1>
        <h2>by Riot</h2>

        <div class="sep"></div>
        <h1><a href="/thd">8. The Hell Dignity</a></h1>
        <h2>by Stormfly</h2>

        <div class="sep"></div>
        <h1><a href="/reflective">9. Reflective</a></h1>
        <h2>by Mojitoz</h2>

        <div class="sep"></div>
        <h1><a href="/necropolix">10. NecropoliX</a></h1>
        <h2>by namtar</h2>

        <div class="sep"></div>
        <h1><a href="/tle">11. The Lost Existence</a></h1>
        <h2>by JonathanGD</h2>

        <div class="sep"></div>
        <h1><a href="/cata">12. Cataclysm</a></h1>
        <h2>by Ggb0y</h2>

        <div class="sep"></div>
        <h1><a href="/niwa">13. Niwa</a></h1>
        <h2>by Teno</h2>

        <div class="sep"></div>
        <h1><a href="/acu">14. Acu</a></h1>
        <h2>by neigefeu</h2>

        <div class="sep"></div>
        <h1><a href="/ICDX">15. ICE Carbon Diablo X</a></h1>
        <h2>by -Roadbose-</h2>

        <!-- A PARTIR DAQUI NÃO TEM ENDPOINT, ENTÃO SEM LINK -->

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
Deploy failed for c069638: Update main.py
Timed out
Port scan timeout reached, no open ports detected on 0.0.0.0. Detected open ports on localhost -- did you mean to bind one of these to 0.0.0.0?
November 20, 2025 at 3:04 PM
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

        <h3><a href="/info">Info</a> <a href="https://www.youtube.com/@anonimorandom">Carrier</a></h3>
    </div>

</body>
</html>"""

@app.route("/golden")
def index1():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#1 - The Golden - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>The Golden</h1>
        <p>By BoBoBoBoBoBoBo, Verified by nSwish</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/SJ7SIDO5sj4"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/widestep")
def wide():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#2 - Widestep - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Widestep</h1>
        <p>By 出見塩</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/TN8fHN_XV3o"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/CosmicCy")
def Cosmic():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#3 - Cosmic Cyclone - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Cosmic Cyclone</h1>
        <p>By APTeamOfficial, Verified by DoSh7t</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/MdCwu0W8"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/thz")
def thz():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#4 - The Hell Zone - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>The Hell Zone</h1>
        <p>By Koreaqwer, Verified by Stormfly</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/6ebIqtnGpdo"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/bj")
def bj():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#5 - Blade of Justice - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Blade of Justice</h1>
        <p>By Manix648, Verified by RicoLP</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/pQc8KL-n20Y"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/moment")
def moment():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#6 - moment - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>moment</h1>
        <p>By lexy, Verified by icedcave</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/bLfKsN4NCNY"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/bb")
def bb():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#7 - Bloodbath - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Bloodbath</h1>
        <p>By Riot, Verified by Riot</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/twTw4fjT0ik"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/thd")
def thd():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#8 - The Hell Dignity - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>The Hell Dignity</h1>
        <p>By Sohn0924, Verified by Stormfly</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/nQuVjZ11Lyw"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/reflective")
def reflective():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#9 - Reflective - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Reflective</h1>
        <p>By Mojitoz, Verified by Vorgogne</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/1fzhBT_7Fos"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/necropolix")
def necropolix():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#10 - NecropoliX - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>NecropoliX</h1>
        <p>By Namtar, Verified by Trusta</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/oV9Oj7YyhpQ"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/tle")
def tle():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#11 - The Lost Existence - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>The Lost Existence</h1>
        <p>By JonathanGD, Verified by Luqualizer</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/XztPxRuKPi4"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/cata")
def cata():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#12 - Cataclysm - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Cataclysm</h1>
        <p>By Ggb0y, Verified by Riot</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/vGV4j8C66JY"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/niwa")
def niwa():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#13 - Niwa - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Niwa</h1>
        <p>By Teno, Verified by Nicor77</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/RXf4PwKRo"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/acu")
def acu():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#14 - Acu - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Acu</h1>
        <p>By neigefeu, Verified by neigefeu</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/z6l74Mkoxm8"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/ICDX")
def ICDX():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#14 - Ice Carbon Diablo X - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Ice Carbon Diablo X</h1>
        <p>By roadbose, Verified by Riot</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/ykwlYeTJblc"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/info")
def info():
    return """<p><h1>this website was made by: ryofreefire32@gmail.com (Silva) and @yuridakbrada</h1></p>
<p><h2><a href="/">Back</a></h2></p>"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
