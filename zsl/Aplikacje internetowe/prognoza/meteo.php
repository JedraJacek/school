<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prognoza pogody Poznań</title>
    <link rel="stylesheet" href="styl4.css" type="text/css">
</head>
<body>
    <section id="topleft">
        <p>maj, 2019 r.</p>
    </section>
    <section id="topmid">
        <h2>Prognoza dla Poznania</h2>
    </section>
    <section id="topright">
        <img src="logo.png" alt="prognoza">
    </section>
    <section id="left">
        <a href="kwerendy.txt">Kwerendy</a>
    </section>
    <section id="right">
        <img src="obraz.jpg" alt="Polska, Poznań">
    </section>
    <section id="main">
        <table>
            <tr><th>Lp.</th><th>DATA</th><th>NOC - TEMPERATURA</th><th>DZIEŃ - TEMPERATURA</th><th>OPADY[mm/h]</th><th>CIŚNIENIE[hPa]</th></tr>
            <?php 
                $conn = new mysqli('localhost','root','','prognoza');
                $result = $conn->query("SELECT * FROM `pogoda` 
                WHERE miasta_id = 2
                ORDER BY data_prognozy DESC");
                $i = 0;
                while($row = $result->fetch_assoc()){
                    $i++;
                    echo "<tr>";
                    echo "<td>".$i."</td><td>".$row['data_prognozy']."</td><td>".$row['temperatura_noc']."</td><td>".$row['temperatura_dzien']."</td><td>".$row['opady']."</td><td>".$row['cisnienie']."</td>";
                    echo "</tr>";
                }
                $conn->close();
            ?>
        </table>
    </section>
    <footer>
        <p>Stronę wykonał: Jacek Jędra</p>
    </footer>
</body>
</html>