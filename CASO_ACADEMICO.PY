print("================================================")
print("\t SISTEMAS DE NOTAS")
print("================================================")
suma_notas=0
cantidad_materias=0
nota_max=-1
nota_min=21
materia_mayor=""
materia_menor=""
reporte_notas=""
continuar="s"
while continuar.lower()=="s":
    print("materia#",(cantidad_materias+1))
    materia=input("ingresar nombre de materia:")
    nota=float(input("ingresa la nota[0-20]:"))
    if nota<0 or nota>20 or materia=="":
        print("error: la nota debe ser entre 0 y 20 y la materia no se púede estar vacia!!!!")
    else:
        suma_notas=suma_notas+nota
        cantidad_materias=cantidad_materias+1
        reporte_notas=reporte_notas+f"{materia}:{nota}\n"
        if nota>nota_max:
            nota_max=nota
            materia_mayor=materia
        if nota<nota_min:
            nota_min=nota
            materia_menor=materia 
        print("materia registrada exitosamente!!!!")
    continuar=input("¿Desea continuar?..(s/n):")
        
print("************************************************")
print("\t\tBOLETIN DE NOTAS")
print("************************************************")
if cantidad_materias>0:
    promedio=suma_notas/cantidad_materias
    print("reporte de notas\n", reporte_notas)
    print("materias evaluadas: ", cantidad_materias)
    print("promedio general:", promedio)
    print("nota maxima:", materia_mayor, "", nota_max)
    print("nota minima:", materia_menor,"", nota_min)
    if promedio>=13:
        print("condicion academica:APROBADO")
    elif promedio>=10.5:
        print("condicion academica: RECUPERACION")
    else:
        print("condicion academica: DESAPROBADO")
else:
    print("No registro materias")
    
    