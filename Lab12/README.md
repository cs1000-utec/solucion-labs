# Solución de la parte práctica
La solución de esta parte sera realizada en google colab, por ello ingrese al siguiente enlace, que esta a continuación:


![Alt text](https://i.ibb.co/4MLwNZb/Punto.png)

# Pasos:

## Realize una copia

Esto se hace para que pueda tenerlo usted, de modo que no sucede lo mismo cuando otras personas quieran trabajar en el mismo colab.

![Alt text](https://i.ibb.co/V9CkQ1w/Captura-de-pantalla-4.png)

Cuando la copia este lista entre al mismo archivo

![Alt text](https://i.ibb.co/T8v5xPK/Captura-de-pantalla-3.png)

##  Inicializa en la imagen de play de la magia negra

![Alt text](https://i.ibb.co/0nzT4qd/Captura-de-pantalla-5.png)

Cuando este listo realize lo msimo con el siguiente, pero cambie el parámetro de (k) cluster para que la probabilidad de similitud aumente, esto dependera de usted.

![Alt text](https://i.ibb.co/b5XWscv/Captura-de-pantalla-6.png)


![Alt text](https://i.ibb.co/2N4SqrN/Captura-de-pantalla-7.png)

## Verifique el resultado en accuracy_score

![Alt text](https://i.ibb.co/fpqkn4K/Captura-de-pantalla-8.png)

Mientras más se aproxime a 1 más se porcentaje de similitud tendrá.

##  Ejecute esta linea de codigo al final, para clasificar la cedula:
```py
sample = [[-39.673293,-44.627058,-10.258163,-18.879989,-49.299946,91.763878,-29.933047,-5.855481,0.393467,15.983484,1.883337,3.035447,-1.117402,-2.636451,-2.063941,2.701432,6.150914,-1.907788,4.144850,-3.033022,2.985857,0.960868,1.994154,3.374098,6.217091,0.024324,0.359676,-4.418659,-1.293296,1.454574,-0.923630,-0.056892,4.999286,4.701583,-1.639602,1.832796,-3.537451,-0.423164,-12.912299,8.454091,-5.329655,0.676623,1.912994,-5.360271,-0.292433,-11.401383,-0.123102,5.145642,-5.092689,-8.202529]]
kmeans.predict(sample)
```


