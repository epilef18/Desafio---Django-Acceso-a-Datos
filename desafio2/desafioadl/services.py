from .models import Tarea, Subtarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.filter(eliminada=False)
    for tarea in tareas:
        print(f"[{tarea.id}] {tarea.descripcion}")
        subtareas = SubTarea.objects.filter(tarea=tarea, eliminada=False)
        for subtarea in subtareas:
            print(f"....[{subtarea.id}] {subtarea.descripcion}")

def crear_nueva_tarea(nombre, descripcion):
    tarea = Tarea.objects.create(id=id, nombre=nombre, descripcion=descripcion)
    tarea.save()
    imprimir_en_pantalla()

def crear_sub_tarea(tarea, nombre, descripcion):
    subtarea = SubTarea.objects.create(tarea=tarea, nombre=nombre, descripcion=descripcion)
    subtarea.save()
    imprimir_en_pantalla()

def elimina_tarea(tarea):
    Tarea.objects.get(id=tarea.id).update(eliminada=True)    
    tarea.save()
    SubTarea.objects.filter(tarea_id=tarea).update(eliminada=True)
    subtarea.save()
    imprimir_en_pantalla()

def elimina_sub_tarea(subtarea):
    SubTarea.objects.get(id=subtarea.id).update(eliminada=True)
    subtarea.save()
    imprimir_en_pantalla()

def imprimir_en_pantalla():
    tareas = Tarea.objects.filter(eliminada=False)
    for tarea in tareas:
        print(f"[{tarea.id}] {tarea.descripcion}")
        subtareas = SubTarea.objects.filter(tarea=tarea, eliminada=False)
        for subtarea in subtareas:
            print(f"....[{subtarea.id}] {subtarea.descripcion}")