<?php 
    session_start();

    if(isset($_GET['akcja']) && $_GET['akcja'] == 'wyloguj'){//sprawdzanie czy kliknięto 'wyloguj'
        unset($_SESSION['zalogowany']); //rozłączenie sesji
    } 
    
    $conn = new mysqli('localhost','root','','baza2');
    if($result = $conn->query("SELECT * FROM uzytkownicy")){
        while($row = $result->fetch_assoc()){
            if(isset($_POST['login']) && isset($_POST['pass']) && $_POST['login'] == $row['login'] && $_POST['pass'] == $row['haslo']){
                $_SESSION['zalogowany'] = $row['ranga']; //ustawienie zmiennej sesyjnej po zalogowaniu
            }
        }
    }
    $conn->close();

    if(!isset($_SESSION['zalogowany'])){//wyświetlenie formularza do logowania, gdy nikt nie jest zalogowany
        ?>

        <!DOCTYPE HTML>
        <html lang="pl">
            <head>
                <meta charset="utf-8" />
                <title>Tytuł strony</title>
            </head>
            <body>
                <form method="POST">
                    Login: <input type="text" name="login"><br/>
                    Hasło: <input type="password" name="pass"><br/>
                    <input type="submit" value="Zaloguj">
                </form>
                <a href="rejestracja.php">Zarejestruj się</a>
            </body>
        </html>

        <?php
    } else {
        if(isset($_SESSION['zalogowany']) && $_SESSION['zalogowany'] == 1){
            echo "Witaj admin<br>";
            echo "<a href='user.php'>Przeglądaj tabele</a><br>";
        } elseif(isset($_SESSION['zalogowany']) && $_SESSION['zalogowany'] == 0){
            echo "Witaj user<br>";
            echo "<a href='user.php'>Przeglądaj tabele</a><br>";
        }
        echo "<a href='logowanie.php?akcja=wyloguj'>wyloguj</a>";
    }

?>