function display_form(){
    meg = "<div class=\"input\"><form id=\"main_form\" action=\"backstage/jsonio.php\", method=\"POST\" onsubmit=\"return saveReport();\">"
    meg += "<div class=\"inputbox\"><label for=\"kcal\" class=\"title\">卡路里：</label><input placeholder=\"4080 每100g(kcal)\" type=\"text\" id=\"kcal\" name=\"kcal\" oninput = \"value=value.replace(/[^\\d]/g,\'\')\" /></div>"
    meg += "<div class=\"inputbox\"><label for=\"protein\" class=\"title\">蛋白质：</label><input placeholder=\"42 每100g\" type=\"text\" id=\"pr1otein\" name=\"protein\" oninput = \"value=value.replace(/[^\\d]/g,\'\')\" /></div>"
    meg += "<div class=\"inputbox\"><label for=\"carbohydrate\" class=\"title\">碳水化合物：</label><input placeholder=\"18 每100g\" type=\"text\" id=\"carbohydrate\" name=\"carbohydrate\" oninput = \"value=value.replace(/[^\\d]/g,\'\')\" /></div>"
    meg += "<div class=\"inputbox\"><label for=\"fat\" class=\"title\">脂肪：</label><input placeholder=\"20 每100g\" type=\"text\" id=\"fat\" name=\"fat\" oninput = \"value=value.replace(/[^\\d]/g,\'\')\" /></div>"
    meg += "<div class=\"submit\"><button id =\"submit\" type:\"submit\" style=\"vertical-align:middle\"><span>Upload </span></button></div></form></div>"
    
    $("div.form").html(meg);
}

function close_form(){
    $("div.input").remove();
}

