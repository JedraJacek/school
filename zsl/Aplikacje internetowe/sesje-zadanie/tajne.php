<?php 
    session_start();

    if(isset($_SESSION['zalogowany']) && $_SESSION['zalogowany'] == 1){
        echo "jest dostęp :) <br>admin";
    } elseif(isset($_SESSION['zalogowany']) && $_SESSION['zalogowany'] == 0){
        echo "jest dostęp :) <br>user";
    } else {
        echo "brak dostępu :(";
    }
?>