<!DOCTYPE html>
<?php
  if(isset($_GET['periodo'])){
    $num=$_GET['periodo'];

  }else {
    $num=1;
  }


?>
<html>
  <head>
    <style>

      .cuerpo{
        background-image: url("dragon-ball.jpg");

        background-repeat: no-repeat;

      };

    </style>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <meta charset="utf-8">
    <title>Tp1</title>
  </head>
  <body >
    <nav >
      <div class="jumbotron text-center cuerpo container" style="color:darkgrey">
        <h1>Taller de Proyecto II - 2017</h1>
        <p>Práctica 1</p>
      </div>
    </nav>
    <div class="container ">
      <div class="container ">
        <div class="row">
          <form action="sensores.php" method="GET">

        <div class="col-md-4">

          <div style="margin-bottom: 25px; opacity:1;" class="input-group">
            <span class=" input-group-addon" id="basic-addon1"><label class="glyphicon glyphicon-equalizer" for="periodo"></label></span>
              <select class="form-control" name="periodo" autofocus="autofocus" required="required">
                    <option value=""selected disabled hidden>Período de muestreo</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="5">5</option>
                    <option value="10">10</option>
                    <option value="30">30</option>
                    <option value="60">60</option>



              </select>
           </div>


         </div>
         <input type="submit" class="btn btn-success" name="enviado" value="Cambiar">
       </form>
      </div>

    </div>
    <div class="container">

        <div class="row">
          <div class="col-sm-6 ">
            <div class="panel panel-success">
              <div class="panel-heading">Temperatura</div>
              <div class="panel-body">
                <table class="table table-hover">
                    <thead>
                      <tr>
                        <th>Frecuencia de muestreo</th>
                        <th>Promedio de muestras </th>
                        <th>Última muestra </th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><?php echo $num*rand(0,5) . "\n";?></td>
                        <td><?php echo $num*rand(0,5) . "\n";?></td>
                        <td><?php echo $num*rand(0,5) . "\n";?></td>

                      </tr>

                    </tbody>
                  </table>
              </div>
           </div>
          </div>
          <div class="col-sm-6 ">
            <div class="panel panel-success">
              <div class="panel-heading">Humedad</div>
              <div class="panel-body">
                <table class="table table-hover">
                    <thead>
                      <tr>
                        <th>Frecuencia de muestreo</th>
                        <th>Promedio de muestras </th>
                        <th>Última muestra </th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><?php echo $num*rand(0,5) . "\n";?></td>
                        <td><?php echo $num*rand(0,5) . "\n";?></td>
                        <td><?php echo $num*rand(0,5) . "\n";?></td>

                      </tr>

                    </tbody>
                  </table>
              </div>
           </div>
          </div>
          <div class="col-sm-6 ">
            <div class="panel panel-success">
              <div class="panel-heading">Presión Atmosférica</div>
              <div class="panel-body">
                <table class="table table-hover">
                    <thead>
                      <tr>
                        <th>Frecuencia de muestreo</th>
                        <th>Promedio de muestras </th>
                        <th>Última muestra </th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><?php echo $num*rand(0,5) . "\n";?></td>
                        <td><?php echo $num*rand(0,5) . "\n";?></td>
                        <td><?php echo $num*rand(0,5) . "\n";?></td>

                      </tr>

                    </tbody>
                  </table>
              </div>
           </div>
          </div>
          <div class="col-sm-6 ">
            <div class="panel panel-success">
              <div class="panel-heading">Velocidad del viento</div>
              <div class="panel-body">
                <table class="table table-hover">
                    <thead>
                      <tr>
                        <th>Frecuencia de muestreo</th>
                        <th>Promedio de muestras </th>
                        <th>Última muestra </th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td><?php echo $num*rand(0,5) . "\n";?></td>
                        <td><?php echo $num*rand(0,5) . "\n";?></td>
                        <td><?php echo $num*rand(0,5) . "\n";?></td>

                      </tr>

                    </tbody>
                  </table>
              </div>
           </div>
          </div>
        </div>
      </div>
    </div>
  </body>
  <!-- FUNCION QUE REFRESCA LA PAGINA CADA 10 SEGUNDOS -->
 <script>setTimeout('document.location.reload()',5000); </script>

</html>
