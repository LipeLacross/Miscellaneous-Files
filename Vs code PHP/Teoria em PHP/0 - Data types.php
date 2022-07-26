<?php
$x = "Hello World\n";#string
echo $x;

$X = 5985;//int
echo "$X\n";//printando uma variável" 

$s = 5975;
var_dump($s);//var_dump irá mostrar o tipo da variável

$x = 10.365;#float
var_dump($x);

$y = false;//boolean

$cars = array("Volvo","BMW","Toyota");// array
var_dump($cars);

$z = "Hello world!\n";
$z = null;//vai anular $z
var_dump($z);


class Car {/*classe com objetos*/
    public $color;
    public $model;
    public function __construct($color, $model) {
        $this->color = $color;
        $this->model = $model;
    }
    public function message() {
        return "My car is a ". $this->color. " ". $this->model. "!";
    }
}

$myCar = new Car("black", "Volvo");
echo $myCar -> message();

$myCar = new Car("red", "Toyota");
echo $myCar -> message();
?>