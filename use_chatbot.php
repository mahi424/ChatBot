<?php
$query=$_POST['query'];
$output = system("python chatbot-client.py $query");
?>
