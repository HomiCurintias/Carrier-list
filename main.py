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
            color: #000;
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
            color: #000;
            text-decoration: black;
            font-size: inherit;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

        <div class="sep"></div>
        <h1><a href="/golden">1. Judgement Knights</a></h1>
        <h2>by HangerLord</h2>

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
        <h1><a href="/Crazy3">16. CraZy III</a></h1>
        <h2>by DavJT</h2>

        <div class="sep"></div>
        <h1><a href="/InfLol">17. Infinity LoL</a></h1>
        <h2>by Guimonteiro</h2>

        <div class="sep"></div>
        <h1><a href="/Necropolis">18. Necropolis</a></h1>
        <h2>by IIINePtunEIII</h2>

        <div class="sep"></div>
        <h1><a href="/Acropolis">19. Acropolis</a></h1>
        <h2>by Zobros</h2>

        <div class="sep"></div>
        <h1><a href="/UF">20. Ultra funky</a></h1>
        <h2>by Guimonteiro</h2>

        <div class="sep"></div>
        <h1><a href="/SuperS">21. Supersonic</a></h1>
        <h2>by ZenthicAlpha</h2>

        <div class="sep"></div>
        <h1><a href="/Slang">22. SlaughterHouse</a></h1>
        <h2>by Havok</h2>

        <div class="sep"></div>
        <h1><a href="/DN">23. Death Note</a></h1>
        <h2>by Ruf</h2>

        <div class="sep"></div>
        <h1><a href="/Manic">24. Manic</a></h1>
        <h2>by Guimonteiro</h2>

        <div class="sep"></div>
        <h1><a href="/Poltergeist">25. Poltergeist</a></h1>
        <h2>by Andromeda GMD</h2>

        <div class="sep"></div>
        <h1><a href="/PP">26. Plasma Pulse</a></h1>
        <h2>by Giron</h2>

        <div class="sep"></div>
        <h1><a href="/WL">27. Windy Landscape</a></h1>
        <h2>by Woogi1411</h2>

        <div class="sep"></div>
        <h1><a href="/Crazy2">28. CraZy II</a></h1>
        <h2>by DavJT</h2>

        <div class="sep"></div>
        <h1><a href="/Stealmate">29. Stalemate</a></h1>
        <h2>by Nox</h2>

        <div class="sep"></div>
        <h1><a href="/TF">30. The Furious</a></h1>
        <h2>by Knobbelboy</h2>

        <div class="sep"></div>
        <h1><a href="/ICFY">31. I Cant Fix You</a></h1>
        <h2>by IronIngot</h2>

        <div class="sep"></div>
        <h1><a href="/SW">32. Shonic wave</a></h1>
        <h2>by Guimonteiro</h2>

        <div class="sep"></div>
        <h1><a href="/CLT3X">33. Cant let troll 3xrow</a></h1>
        <h2>by Guimonteiro</h2>

        <div class="sep"></div>
        <h1><a href="/WC">34. Whatsapp circles</a></h1>
        <h2>by XKYY</h2>

        <div class="sep"></div>
        <h1><a href="/Hellaven2">35. Hellaven II</a></h1>
        <h2>by clasi</h2>

        <div class="sep"></div>
        <h1><a href="/Crazy">36. CraZy</a></h1>
        <h2>by DavJT</h2>

        <div class="sep"></div>
        <h1><a href="/CLT2">37. Cant troll twice</a></h1>
        <h2>by Guimonteiro</h2>

        <div class="sep"></div>
        <h1><a href="/Widder">38. widder</a></h1>
        <h2>by 2003devin</h2>

        <div class="sep"></div>
        <h1><a href="/PA3">39. Potatoguy adven 3</a></h1>
        <h2>by BearWare</h2>

        <div class="sep"></div>
        <h1><a href="/NC">40. Nine Circles</a></h1>
        <h2>by Zobros</h2>

        <div class="sep"></div>
        <h1><a href="/Jawbeaker">41. Jawbreaker</a></h1>
        <h2>by ZenthicAlpha</h2>

        <div class="sep"></div>
        <h1><a href="/CLT">42. Cant let troll</a></h1>
        <h2>by Defectum</h2>

        <div class="sep"></div>
        <h1><a href="/CasteloDaVania">43. Megalovania</a></h1>
        <h2>by EternaswipVMAX</h2>

        <div class="sep"></div>
        <h1><a href="/Hellaven">44. Hellaven</a></h1>
        <h2>by clasi</h2>

        <div class="sep"></div>
        <h1><a href="/Rhombus">45. Rhombus</a></h1>
        <h2>by Theixn</h2>

        <div class="sep"></div>
        <h1><a href="/BPN">46. BP night</a></h1>
        <h2>by -</h2>

        <div class="sep"></div>
        <h1><a href="/Aleph">47. Aleph</a></h1>
        <h2>by AlemaneiroGD</h2>

        <div class="sep"></div>
        <h1><a href="/Verity">48. VeritY</a></h1>
        <h2>by Serponge</h2>

        <div class="sep"></div>
        <h1><a href="/SE">49. Sakupen Egg</a></h1>
        <h2>by Sivlol</h2>

        <div class="sep"></div>
        <h1><a href="/EP">50. Extreme Park</a></h1>
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

@app.route("/Crazy3")
def Crazy3():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#16 - CraZy III - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>CraZy III</h1>
        <p>By DavJT, Verified by Nexus</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/1ynspvn8KSs"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/InfLol")
def InfLol():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#17 - Infinity LoL - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Infinity LoL</h1>
        <p>By guimonteiro, Verified by guimonteiro</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/2JPufkQtejs"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/Necropolis")
def Necropolis():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#18 - Necropolis - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Necropolis</h1>
        <p>By IIINePtunEIII</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/bVUVS5dG7qQ"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/Acropolis")
def Acropolis():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#19 - Acropolis - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Acropolis</h1>
        <p>By Zobros, Verified by Zobros</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/4v39XU7LW7M"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/UF")
def UF():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#20 - Ultra Funky - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Ultra Funky</h1>
        <p>By guimonteiro, Verified by guimonteiro</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/Q1byyj8ygs"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/SuperS")
def SuperS():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#21 - Supersonic - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Supersonic</h1>
        <p>By ZenthicAlpha</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/Q1byyj8ygs"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/Slang")
def Slang():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#22 - Slaughterhouse - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Slaughterhouse</h1>
        <p>By Havok</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/BIuUrSiU8"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/DN")
def DN():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#23 - Death Note - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Death Note</h1>
        <p>By Ruf</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/asQrt9B3aMo"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/Manic")
def Manic():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#24 - Manic - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Manic</h1>
        <p>By guimonteiro, Verified by guimonteiro</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/Poltergeist")
def Poltergeist():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#25 - Poltergesit - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Poltergeist</h1>
        <p>By Andromeda</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/63sr55FXqsI"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/PP")
def PP():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#26 - Plasma Pulse - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Plasma Pulse</h1>
        <p>By Giron, Verified by Giron</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/KkpIMc7DkiY"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/WL")
def WL():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#27 - Windy Landscape - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Windy landscape</h1>
        <p>By WOOGI1411, Verified by WOOGI1411</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/ICYmhBFVEOc"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/Crazy2")
def Crazy2():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#28 - CraZy II - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>CraZy II</h1>
        <p>By DavJT, Verified by DavJT</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/eGPNEaZV6cc"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/Stealmate")
def Stalemate():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#29 - Stalemate - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Stalemate</h1>
        <p>By Nox, Verified by Nox</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/rtm0flhztcU"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/TF")
def TF():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#30 - The Furious - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>The Furious</h1>
        <p>By knobbelboy, Verified by knobbelboy</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/BmRbvsYKPAk"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/ICFY")
def ICFY():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#31 - I Cant Fix You - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>I Cant Fix You</h1>
        <p>By IronIngot</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/2c6s-7625Iw"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/SN")
def SN():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#32 - Shonic Wave - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Shonic Wave</h1>
        <p>By guimonteiro, Verified by guimonteiro</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/CLT3X")
def CLT3X():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#33 - Cant let troll 3xrow - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Cant let troll 3xrow</h1>
        <p>By guimonteiro, Verified by guimonteiro</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/WC")
def WC():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#34 - WhatsApp Circles - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>WhatsApp Circles</h1>
        <p>By XKYY</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/PFyJakT40V0"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/Halleven2")
def Halleven2():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#35 - Hellaven II - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Hellaven II</h1>
        <p>By clasi</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/9my13Ak5VpE"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/Crazy")
def Crazy():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#36 - CraZy - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>CraZy</h1>
        <p>By DavJT</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/g_MP6BENHEs"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/CLT2")
def CLT2():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#37 - Cant let twice - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Cant let twice</h1>
        <p>By guimonteiro, Verified by guimonteiro</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/Widder")
def Widder():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#38 - Widder - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Widder</h1>
        <p>By 2003devin</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/4e99rXr_cuc"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/PA3")
def PA3():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#39 - Potatoguy adven 3 - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Potatoguy adven 3</h1>
        <p>By BearWare</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/_LDPKT1mW5c"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/NC")
def NC():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#40 - Nine Circles - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Nine Circles</h1>
        <p>By Zobros</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/dOdPoU1ncOc"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/Jawbraker")
def Jawbraker():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#41 - Jawbreaker - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Jawbreaker</h1>
        <p>By ZenthicAlpha</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/7lsLVVujIvg"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/CLT")
def CLT():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#42 - Cant Let Troll - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Cant Let Troll</h1>
        <p>By Defectum</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/1pf6HKJ_eh8"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/CasteloDaVania")
def CasteloDaVania():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#43 - Megalovania - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Megalovania</h1>
        <p>By EternaswipVMAX</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/7YoOzQ7hFewindex49.html"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/Hellaven")
def Hellaven():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#44 - Hellaven - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Hellaven</h1>
        <p>By clasi</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/I99AAU7a4M4"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/Rhombus")
def Rhombus():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#45 - Rhombus - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Rhombus</h1>
        <p>By Theixn</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/RX1Sw-A0zMk"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/BPN")
def BPN():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#46 - BP Night - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>BP Night</h1>
        <p>By RA7</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/vb7qxwExsFc"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/Aleph")
def Aleph():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#47 - Aleph - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Aleph</h1>
        <p>By AlemaneiroGD</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/Verity")
def Verity():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#48 - VeritY - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>VeritY</h1>
        <p>By Serponge</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/p15w9MB2eAc"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/SA")
def SA():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#49 - Sakupen Egg - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Sakupen Egg</h1>
        <p>By Sivlol</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/M61Vqi6ryj8"
    frameborder="0"
    allowfullscreen>
</iframe>
    </div>

</body>
</html>"""

@app.route("/EP")
def EP():
    return """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#50 - Extreme Park - Carrier List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="level">
        <h1>Extreme Park</h1>
        <p>By Rabbitical, Verified by Rabbitical</p>
        <iframe width="560" height="315"
    src="https://www.youtube.com/embed/re_CbPW12tE"
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
