<?php 
    session_start();
    if(isset($_SESSION['zalogowany'])){
    ?>
    <!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table border=1>
        <tr><th>ID</th><th>Nazwa</th></tr>
        <?php 
            $conn = new mysqli('localhost','root','','baza2');
            $result = $conn->query("SELECT * FROM przedmioty");
            while($row = $result->fetch_assoc()){
                echo "<tr>";
                echo "<td>".$row['id']."</td><td>".$row['nazwa']."</td>";
                echo "</tr>";
            }
            echo "</table>";
            if(isset($_SESSION['zalogowany']) && $_SESSION['zalogowany'] == 1){
                echo "<a href='admin.php'>Dodawanie i usuwanie z tabeli</a>";
            }
            $conn->close();
        ?>
    </table>
</body>
</html>
<?php 
    }else {
        echo "<a href='logowanie.php'>Zaloguj się</a>";
    }
?>