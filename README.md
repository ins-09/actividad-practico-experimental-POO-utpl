### <center> Universidad Técnica Particular de Loja (UTPL)  
##### <center>Carrera de Redes y Analítica de Datos

# Programación Orientada a Objetos #
ℹ️ Docente: WAYNER XAVIER BUSTAMANTE GRANDA  
ℹ️ Elaborado por: YEREMI ALEXANDER ROMAN RIVERA

> Resultados de aprendizaje que se espera lograr:
>
> Diseña modelos avanzados con Programación Orientada a Objetos (POO) desarrollando soluciones innovadoras que optimicen la visualización de datos y la adaptación en infraestructuras tecnológicas.       
---
**Figura 1**    
Diseño UML del código
![alt text](https://github.com/user-attachments/assets/39116efa-39c8-4780-8891-fc80cf9c4320)
---
## **¿Qué es un método?**

Un método son comportamientos/acciones definidos en una clase para poder ser utilizados dentro o fuera de ella. Estos métodos permiten interactuar con los datos del objeto gracias al parámetro *self*.

La creación de estos métodos se hacen atraves de la implementación de la palabra reservada *def* dentro de una clase, donde podrán recibir **parámetros** como entrada y modificar el estado de los atributos de la instancia.

Se clasifican en:

- Métodos de instancia "normales".
- Métodos de clase por medio del decorador @classmethod.
- Métodos estáticos usando el decorador @staticmethod.

**Figura 2**    
Código fuente de métodos de una clase en Python
![alt text](https://github.com/user-attachments/assets/fe1a8a99-c084-474b-99ec-71411d10933d)

En la **Figura 2** tenemos un método *informacion* el cual define dos parámetros, el *self* que hace referencia a la propia instancia cuando sea llamada y el *tipoVehiculo* para saber que tipo de vehiculo ejecuta este método. Por último retorna una string con la información de la clase *VehiculoMotocicleta*.

--- 
## **¿Qué es un parámetro?**

Un parametro es una variable que recibe un método o constructor para procesar información externa. Espera valores (argumentos) cuando el método es invocado, permitiendo que el código sea flexible y reutilizable.

Por lo tanto el paso de un parámetro es un tipo de mecanismo que nos permite enviar datos a los métodos o constructores de un objeto. Nos permite configurar su comportamiento o interactuar con otros objetos.

**Figura 3**    
Código fuente del paso de parámetros de una clase en Python
![alt text](https://github.com/user-attachments/assets/b0f2f1f9-c5a7-4608-9c49-64cbd6a58032)

Para la **Figura 4** tenemos el constructor *__init__* de la clase *Vehiculo* el cual define sus parámetros (*self, color, marca, numeroRuedas, numeroAsientos*).

**Figura 4**    
Parámetros del constructor de la clase Vehiculo.
![alt text](https://github.com/user-attachments/assets/e0ef9b6e-8744-4e96-9462-769674407502)

Estos parámetros permitiran el flujo de información que comunican al objeto con el mundo exterior (u otras partes del código), dejando alterar su estado físico y definir cómo ejectuar su acciones.

--- 
## **Creación de objetos con manejo de excepciones**

La creación de objetos con manejo de excepciones permite validar datos durante la instanciación (creación del objeto). Se realiza lanzando errores (*raise*) en cualquier parte de la clase ante datos u operaciones inválidas y capturándolos (*try-except*) al crear el objeto, lo que evita que el programa falle abruptamente.

**Figura 5**    
Manejo de excepciones en el constructor __init__ de la clase Vehiculo.
![alt text](https://github.com/user-attachments/assets/241430d1-4fa6-4f39-8adf-bb8930953346)

En la **Figura 5** en el constructor *__init__* de la clase Vehiculo establecemos una pequeña validación que comprueba que los parámetros *numeroRuedas* y *numeroAsientos* sean de tipo **int** (valor númerico), descartando cualquier otro tipo de valor (string, bool). Al momento de crear la instancia de la clase Vehiculo si se llegase a pasar como argumento un valor que no sea número se lanzaría un **raise** de tipo **ValueError** indicando el problema. 

---
##Referencias bibliográficas

> Ramírez Coronel, R. L. (2025). Programación Orientada a Objetos: Guía didáctica (1.ª ed.). Ediloja Cia. Ltda.
