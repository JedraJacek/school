<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style12.css" type="text/css">
    <title>Gromady kręgowców</title>
</head>
<body>
    <section id="menu">
        <a href="gromada-ryby.html">gromada ryb</a>
        <a href="gromada-ptaki.html">gromada ptaków</a>
        <a href="gromada-ssaki.html">gromada ssaków</a>
    </section>
    <section id="logo">
        <h2>GROMADY KRĘGOWCÓW</h2>
    </section>
    <section id="left">
        <?php 
            $conn = new mysqli('localhost','root','','baza');
            $q1 = "SELECT id, Gromady_id, gatunek, wystepowanie FROM `zwierzeta` WHERE Gromady_id = 4 OR Gromady_id = 5;";
            $wynik = $conn->query($q1);
            while($wiersz = $wynik->fetch_assoc()){
                echo "<p>";
                echo $wiersz['id'].". ".$wiersz['gatunek'];
                echo "</p>";
                if($wiersz['Gromady_id'] == 4){
                    $x = "ptaki";
                } elseif($wiersz['Gromady_id'] == 5){
                    $x = "ssaki";
                }
                echo "<p>";
                echo "Występowanie: ".$wiersz['wystepowanie'].", gromada ".$x;
                echo "</p>";
                echo "<hr>";
            }
            $conn->close();
        ?>
    </section>
    <section id="right">
        <h1>PTAKI</h1>
        <ol>
            <?php 
                $conn = new mysqli('localhost','root','','baza');
                $q2 = "SELECT gatunek, obraz FROM `zwierzeta` WHERE Gromady_id = 4;";
                $wynik = $conn->query($q2);
                while($wiersz = $wynik->fetch_assoc()){
                    echo "<li>";
                    echo "<a href=".$wiersz['obraz'].">".$wiersz['gatunek']."</a>";
                    echo "</li>";
                }
                $conn->close();
            ?>
        </ol>
        <img src="sroka.jpg" alt="Sroka zwyczajna, gromada ptaki">
    </section>
    <footer>
        <p>Stronę o kręgowcach przygotował: 00000000000</p>
    </footer>
</body>
</html>