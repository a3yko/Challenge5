<!DOCTYPE html>
<html lang="en">
	<head>
	</head>
	<body>
    <form method="get">
    <input type="submit" name="test" id="showdata" value="Show Scrapy Data" /><br>
    </form>
	</body>
    <?php
    if(array_key_exists('test',$_GET)){
        getData();
    }
   function getData(){ 
        $mng = new MongoDB\Driver\Manager("mongodb://localhost:27017");
        $qry = new MongoDB\Driver\Query([]);

        
        $rows = $mng->executeQuery("tech.posts", $qry);

        foreach ($rows as $row){
        echo "<div>";
        echo "<br><tr><br>";
        echo trim("<td> $row->title </td> <br>");
        echo trim("<td> $row->author </td> <br>");
        echo trim("<td> $row->date </td> <br>");
        echo "</tr>";
        echo "</div>";
        }
    }
    ?>
</html>