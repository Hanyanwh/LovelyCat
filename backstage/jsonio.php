<?php
    $jon_string = file_get_contents('user_information.json');
    $data = json_decode($jon_string, true);
    if ($_POST['kcal'] != "" and $_POST['protein'] !="" and $_POST['carbohydrate'] != "" and $_POST['fat'] != "" ){
        $data['kcal'] = $_POST['kcal'];
        $data['protein'] = $_POST['protein'];
        $data['carbohydrate'] = $_POST['carbohydrate'];
        $data['fat'] = $_POST['fat'];
    }
    $data_str = json_encode($data);
    
    file_put_contents('user_information.json', $data_str);
    header("Location: http://47.103.4.22:1080"); 
?>
