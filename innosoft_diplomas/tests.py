import pandas as pd


class DiplomaAutomaticoTestCase():
    def setUp(self):
        return True

if __name__ == "__main__":  
    # Crear un DataFrame de  Pandas a partir de los datos.
    df = pd.DataFrame({'DNI': [111111111, 111111112, 111111113, 111111114, 111111115, 111111116, 111111117],
                        'Apellidos': ["Alé Palacios", "Gata Fernández", "Biedma Fresno", "Yanes Ariza", "Losada Ostos", "Merino Verde", "Benavides Cuevas"],
                        'Nombre': ["Francisco", "José Manuel", "Pedro", "Miguel", "Guillermo", "Enrique", "David"],
                        'Uvus': ["fraalepal", "josgatfer", "pedbiefre", "migyanari", "guilosost", "enrmerver", "davbencue"],
                        'Correo': ["fraalepal@us.es", "josgatfer@us.es", "pedbiefre@us.es", "migyanari@us.es", "guilosost@us.es", "enrmerver@us.es", "davbencue@us.es"],
                        'Perfil': ["http://evidentia.test/20/profiles/view/1", "http://evidentia.test/20/profiles/view/2", "http://evidentia.test/20/profiles/view/3", "http://evidentia.test/20/profiles/view/4", "http://evidentia.test/20/profiles/view/5", "http://evidentia.test/20/profiles/view/6", "http://evidentia.test/20/profiles/view/7"],
                        'Participación': ["ASSISTANCE", "ASSISTANCE", "ASSISTANCE", "ASSISTANCE", "ASSISTANCE", "ASSISTANCE", "ASSISTANCE"],
                        'Comité': [None, None, "Sostenibilidad", None, "Logística", None, "Logística"],
                        'Evidencia aleatoria': [None, None, None, None, None, None, None],
                        'Horas de evidencia aleatoria': [None, None, None, None, None, None, None],
                        'Eventos asistidos': [10, 10, 10, 7, 10, 4, 10],
                        'Horas de asistencia': [10, 10, 10, 7, 10, 4, 10],
                        'Reuniones asistidas': [None, None, None, None, None, None, None],
                        'Bono de horas': [None, None, None, None, None, None, None],
                        'Horas de reuniones': [None, None, None, None, None, None, None],
                        'Evidencias registradas': [None, None, None, None, None, None, None],
                        'Horas de evidencias': [None, None, None, None, None, None, None],
                        'Horas en total': [10, 10, 10, 7, 10, 4, 10]})
    

    # Crear un ExcelWriter a partir de XlsxWriter.
    writer = pd.ExcelWriter('tests.xlsx', engine='xlsxwriter')

    # Convertir el DataFrame a un objeto Excel de XlsxWriter.
    df.to_excel(writer, sheet_name='Worksheet', index=False)

    # Cerrar el Writer y devolver el fichero creado.
    writer.save()
pass