# INTRO A PYTHON 2
Aqui tenemos algunos gráficos de los diferentes ejercicios para orientarlos

## IF ELSE
Veamos como se ve utilizar if else elif


### Ejercicio 1.2

```mermaid
graph LR
A(Inicio) --> B(Edad >= 18)
B(Edad >= 18) --> C(Mayor de edad)
B(Edad >= 18) --> D(Menor de edad)
```

### Ejercicio 1.7
```mermaid
graph TD;
    Inicio[Inicio] --> Condicion;
    Condicion -->|tipo_animal == 'perro'| Si;
    Condicion -->|tipo_animal != 'perro'| No;
    Si[Si] --> Imprimir1;
    No[No] --> Condicion2;
    Condicion2 -->|tipo_animal == 'gato'| Si2;
    Condicion2 -->|tipo_animal != 'gato'| No2;
    Si2 --> Imprimir2;
    No2 --> Imprimir3;
    Imprimir1[En esta veterinaria si atendemos perros];
    Imprimir2[En esta veterinaria si atendemos gatos];
    Imprimir3[En esta veterinaria solo atendemos perros y gatos];
```

### Ejercicio 1.8
```mermaid
graph TD;
    Inicio[Inicio] --> Condicion;
    Condicion -->|color_primario == 'azul'| Si;
    Condicion -->|color_primario != 'azul'| Condicion2;
    Si[Si] --> ImprimirAzul;
    Condicion2 -->|color_primario == 'rojo'| SiRojo;
    Condicion2 -->|color_primario != 'rojo'| Condicion3;
    SiRojo[SiRojo] --> ImprimirRojo;
    Condicion3 -->|color_primario == 'amarillo'| SiAmarillo;
    Condicion3 -->|color_primario != 'amarillo'| No;
    SiAmarillo[SiAmarillo] --> ImprimirAmarillo;
    No[No] --> ImprimirNoSeleccionado;
    ImprimirAzul[Color primario seleccionado: azul];
    ImprimirRojo[Color primario seleccionado: rojo]
    ImprimirAmarillo[Color primario seleccionado: amarillo];
    ImprimirNoSeleccionado[No ha seleccionado un color primario];
```

### Ejercicio 1.9
```mermaid
graph TD;
    Inicio[Inicio] --> Condicion1((Edad > 18?));
    Condicion1 -->|Sí| SiMayorDeEdad;
    Condicion1 -->|No| NoMenorDeEdad;
    SiMayorDeEdad[SiMayorDeEdad] --> ImprimirMayorDeEdad;
    NoMenorDeEdad[NoMenorDeEdad] --> ImprimirMenorDeEdad;
    SiEdadLaboral -->ImprimirEdadLaboral;
    SiEdadLaboral --> ImprimirEdadJubilatoria;
    ImprimirMayorDeEdad[Imprimir: Usted es mayor de edad] --> SiEdadLaboral;
    ImprimirMenorDeEdad[Imprimir: Usted es menor de edad];
    ImprimirEdadLaboral[Imprimir: Se encuentra en edad laboral];
    ImprimirEdadJubilatoria[Imprimir: Se encuentra en edad jubilatoria];
```

### Ejercicio 1.10
```mermaid
graph LR
A(Inicio) --> B(Edad >= 65 & Genero == 'M')
B(Edad >= 65 & Genero == 'M') --> C(Jubilado: Imprimir 'Usted se encuentra en edad jubilatoria')
B(Edad >= 65 & Genero == 'M') --> D(No Jubilado: Imprimir 'No se encuentra en edad jubilatoria')
D(No Jubilado) --> E(Edad >= 62 & Genero == 'F')
E(Edad >= 62 & Genero == 'F') --> F(Jubilada: Imprimir 'Usted se encuentra en edad jubilatoria')
E(Edad >= 62 & Genero == 'F') --> G(No Jubilada: Imprimir 'No se encuentra en edad jubilatoria')
```
