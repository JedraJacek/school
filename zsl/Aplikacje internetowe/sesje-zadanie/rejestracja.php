<!DOCTYPE HTML>
<html lang="pl">
    <head>
        <meta charset="utf-8" />
        <title>Tytuł strony</title>
    </head>
    <body>
        <form action="rejestracja.php" method="POST">
            Login: <input type="text" name="login" required><br/>
            Hasło: <input type="password" name="pass" required><br/>
            Imie: <input type="text" name="name" required><br/>
            Nazwisko: <input type="text" name="surname" required><br/>
            <input type="submit" value="Zarejestruj się">
        </form>
        <?php 
            if(isset($_POST['login']) && isset($_POST['pass']) && isset($_POST['name']) && isset($_POST['surname'])){
                $name = $_POST['name'];
                $pass = $_POST['pass'];
                $login = $_POST['login'];
                $surname = $_POST['surname'];

                $conn0 = new mysqli('localhost','root','','baza2');
                $result0 = $conn0->query("SELECT * FROM uzytkownicy");
                $j=0;
                while($row0 = $result0->fetch_assoc()){
                    if($row0['login'] == $login){
                        $j++;
                    }
                }
                if($j==0){
                    $conn = new mysqli('localhost','root','','baza2');
                    mysqli_set_charset($conn,"utf-8");
                    $q = "INSERT INTO uzytkownicy(`imie`, `nazwisko`, `login`, `haslo`)
                        VALUES
                        ('$name','$surname','$login','$pass')";
                    $conn->query($q);
                    $conn->close();
                    header("location: rejestracja.php");
                } else {
                    echo "Podany login jest już zajęty";
                }
            }
        ?>
    </body>
</html>