from unittest.case import TestCase
import pandas as pd
import unittest
from innosoft_diplomas.diploma_automatico import organizadorAuxiliar, asistenciaAuxiliar

class DiplomaAutomaticoTestCase(TestCase):
    def setUp(self):
        # Crear un DataFrame de  Pandas a partir de los datos.
        #DataFrame con datos válidos
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
        
        #DataFrame con horas totales negativas y comités numéricos
        df1 = pd.DataFrame({'DNI': [111111111, 111111112, 111111113, 111111114, 111111115, 111111116, 111111117],
                            'Apellidos': ["Alé Palacios", "Gata Fernández", "Biedma Fresno", "Yanes Ariza", "Losada Ostos", "Merino Verde", "Benavides Cuevas"],
                            'Nombre': ["Francisco", "José Manuel", "Pedro", "Miguel", "Guillermo", "Enrique", "David"],
                            'Uvus': ["fraalepal", "josgatfer", "pedbiefre", "migyanari", "guilosost", "enrmerver", "davbencue"],
                            'Correo': ["fraalepal@us.es", "josgatfer@us.es", "pedbiefre@us.es", "migyanari@us.es", "guilosost@us.es", "enrmerver@us.es", "davbencue@us.es"],
                            'Perfil': ["http://evidentia.test/20/profiles/view/1", "http://evidentia.test/20/profiles/view/2", "http://evidentia.test/20/profiles/view/3", "http://evidentia.test/20/profiles/view/4", "http://evidentia.test/20/profiles/view/5", "http://evidentia.test/20/profiles/view/6", "http://evidentia.test/20/profiles/view/7"],
                            'Participación': ["ASSISTANCE", "ASSISTANCE", "ASSISTANCE", "ASSISTANCE", "ASSISTANCE", "ASSISTANCE", "ASSISTANCE"],
                            'Comité': [None, None, 12, None, 12, None, 12],
                            'Evidencia aleatoria': [None, None, None, None, None, None, None],
                            'Horas de evidencia aleatoria': [None, None, None, None, None, None, None],
                            'Eventos asistidos': [10, 10, 10, 7, 10, 4, 10],
                            'Horas de asistencia': [10, 10, 10, 7, 10, 4, 10],
                            'Reuniones asistidas': [None, None, None, None, None, None, None],
                            'Bono de horas': [None, None, None, None, None, None, None],
                            'Horas de reuniones': [None, None, None, None, None, None, None],
                            'Evidencias registradas': [None, None, None, None, None, None, None],
                            'Horas de evidencias': [None, None, None, None, None, None, None],
                            'Horas en total': [-10, -10, -10, -7, -10, -4, -10]})
        
        #DataFrame con horas totales no numéricas
        df2 = pd.DataFrame({'DNI': [111111111, 111111112, 111111113, 111111114, 111111115, 111111116, 111111117],
                            'Apellidos': ["Alé Palacios", "Gata Fernández", "Biedma Fresno", "Yanes Ariza", "Losada Ostos", "Merino Verde", "Benavides Cuevas"],
                            'Nombre': ["Francisco", "José Manuel", "Pedro", "Miguel", "Guillermo", "Enrique", "David"],
                            'Uvus': ["fraalepal", "josgatfer", "pedbiefre", "migyanari", "guilosost", "enrmerver", "davbencue"],
                            'Correo': ["fraalepal@us.es", "josgatfer@us.es", "pedbiefre@us.es", "migyanari@us.es", "guilosost@us.es", "enrmerver@us.es", "davbencue@us.es"],
                            'Perfil': ["http://evidentia.test/20/profiles/view/1", "http://evidentia.test/20/profiles/view/2", "http://evidentia.test/20/profiles/view/3", "http://evidentia.test/20/profiles/view/4", "http://evidentia.test/20/profiles/view/5", "http://evidentia.test/20/profiles/view/6", "http://evidentia.test/20/profiles/view/7"],
                            'Participación': ["ASSISTANCE", "ASSISTANCE", "ASSISTANCE", "ASSISTANCE", "ASSISTANCE", "ASSISTANCE", "ASSISTANCE"],
                            'Comité': [None, None, 12, None, 12, None, 12],
                            'Evidencia aleatoria': [None, None, None, None, None, None, None],
                            'Horas de evidencia aleatoria': [None, None, None, None, None, None, None],
                            'Eventos asistidos': [10, 10, 10, 7, 10, 4, 10],
                            'Horas de asistencia': [10, 10, 10, 7, 10, 4, 10],
                            'Reuniones asistidas': [None, None, None, None, None, None, None],
                            'Bono de horas': [None, None, None, None, None, None, None],
                            'Horas de reuniones': [None, None, None, None, None, None, None],
                            'Evidencias registradas': [None, None, None, None, None, None, None],
                            'Horas de evidencias': [None, None, None, None, None, None, None],
                            'Horas en total': ["-10asdad", "-10asdads", "-10asdasd", "-10adsad", "-10adasd", "-10asdads", "-10dasda"]})
        
        #DataFrame con Eventos asistidos no numéricos
        df3 = pd.DataFrame({'DNI': [111111111, 111111112, 111111113, 111111114, 111111115, 111111116, 111111117],
                            'Apellidos': ["Alé Palacios", "Gata Fernández", "Biedma Fresno", "Yanes Ariza", "Losada Ostos", "Merino Verde", "Benavides Cuevas"],
                            'Nombre': ["Francisco", "José Manuel", "Pedro", "Miguel", "Guillermo", "Enrique", "David"],
                            'Uvus': ["fraalepal", "josgatfer", "pedbiefre", "migyanari", "guilosost", "enrmerver", "davbencue"],
                            'Correo': ["fraalepal@us.es", "josgatfer@us.es", "pedbiefre@us.es", "migyanari@us.es", "guilosost@us.es", "enrmerver@us.es", "davbencue@us.es"],
                            'Perfil': ["http://evidentia.test/20/profiles/view/1", "http://evidentia.test/20/profiles/view/2", "http://evidentia.test/20/profiles/view/3", "http://evidentia.test/20/profiles/view/4", "http://evidentia.test/20/profiles/view/5", "http://evidentia.test/20/profiles/view/6", "http://evidentia.test/20/profiles/view/7"],
                            'Participación': ["ASSISTANCE", "ASSISTANCE", "ASSISTANCE", "ASSISTANCE", "ASSISTANCE", "ASSISTANCE", "ASSISTANCE"],
                            'Comité': [None, None, "Sostenibilidad", None, "Logística", None, "Logística"],
                            'Evidencia aleatoria': [None, None, None, None, None, None, None],
                            'Horas de evidencia aleatoria': [None, None, None, None, None, None, None],
                            'Eventos asistidos': ["-10asdad", "-10asdads", "-10asdasd", "-10adsad", "-10adasd", "-10asdads", "-10dasda"],
                            'Horas de asistencia': [10, 10, 10, 7, 10, 4, 10],
                            'Reuniones asistidas': [None, None, None, None, None, None, None],
                            'Bono de horas': [None, None, None, None, None, None, None],
                            'Horas de reuniones': [None, None, None, None, None, None, None],
                            'Evidencias registradas': [None, None, None, None, None, None, None],
                            'Horas de evidencias': [None, None, None, None, None, None, None],
                            'Horas en total': [10, 10, 10, 7, 10, 4, 10]})
        
        #DataFrame con números en los apellidos
        df4 = pd.DataFrame({'DNI': [111111111, 111111112, 111111113, 111111114, 111111115, 111111116, 111111117],
                            'Apellidos': [1, 2, 3, 4, 5, 6, 7],
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

        #DataFrame con números en el nombre
        df5 = pd.DataFrame({'DNI': [111111111, 111111112, 111111113, 111111114, 111111115, 111111116, 111111117],
                            'Apellidos': ["Alé Palacios", "Gata Fernández", "Biedma Fresno", "Yanes Ariza", "Losada Ostos", "Merino Verde", "Benavides Cuevas"],
                            'Nombre': [1, 2, 3, 4, 5, 6, 7],
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
        writer = pd.ExcelWriter('./muestras_pruebas/tests.xlsx', engine='xlsxwriter')
        writer1 = pd.ExcelWriter('./muestras_pruebas/tests1.xlsx', engine='xlsxwriter')
        writer2 = pd.ExcelWriter('./muestras_pruebas/tests2.xlsx', engine='xlsxwriter')
        writer3 = pd.ExcelWriter('./muestras_pruebas/tests3.xlsx', engine='xlsxwriter')
        writer4 = pd.ExcelWriter('./muestras_pruebas/tests4.xlsx', engine='xlsxwriter')
        writer5 = pd.ExcelWriter('./muestras_pruebas/tests5.xlsx', engine='xlsxwriter')

        # Convertir el DataFrame a un objeto Excel de XlsxWriter.
        df.to_excel(writer, sheet_name='Worksheet', index=False)
        df1.to_excel(writer1, sheet_name='Worksheet', index=False)
        df2.to_excel(writer2, sheet_name='Worksheet', index=False)
        df3.to_excel(writer3, sheet_name='Worksheet', index=False)
        df4.to_excel(writer4, sheet_name='Worksheet', index=False)
        df5.to_excel(writer5, sheet_name='Worksheet', index=False)

        # Cerrar el Writer y devolver el fichero creado.
        writer.save()
        writer1.save()
        writer2.save()
        writer3.save()
        writer4.save()
        writer5.save()
        

    def testNombre(self):
        df = pd.read_excel("./muestras_pruebas/tests.xlsx", header=None)
        nombre = df.iloc[1].values[2]
        self.assertEqual("Francisco", nombre)

    def testApellidos(self):
        df = pd.read_excel("./muestras_pruebas/tests.xlsx", header=None)
        apellidos = df.iloc[1].values[1]
        self.assertEqual("Alé Palacios", apellidos)

    def testEventosAsistidos(self):
        df = pd.read_excel("./muestras_pruebas/tests.xlsx", header=None)
        eventos_asistidos = df.iloc[1].values[10]
        self.assertEqual(10, eventos_asistidos)

    def testHorasTotalesAsistidas(self):
        df = pd.read_excel("./muestras_pruebas/tests.xlsx", header=None)
        horas_totales = df.iloc[1].values[17]
        self.assertEqual(10, horas_totales)       
    
    #Tests Diplomas Automaticos de Organizador
    def testDiplomasAutomaticosOrganizador3Correctos(self):
        df = pd.read_excel("./muestras_pruebas/tests.xlsx", header=None)
        self.assertEqual(3, organizadorAuxiliar(df))

    def testDiplomasAutomaticosOrganizadorDatosNumericos(self):
        df = pd.read_excel("./muestras_pruebas/tests1.xlsx", header=None)
        self.assertEqual(0, organizadorAuxiliar(df))

    #Tests Diplomas Automaticos de Asistencia
    def testDiplomasAutomaticosAsistencia7Correctos(self):
        df = pd.read_excel("./muestras_pruebas/tests.xlsx", header=None)
        self.assertEqual(7, asistenciaAuxiliar(df, 1, []))

    def testDiplomasAutomaticosAsistenciaHorasNegativas(self):
        df = pd.read_excel("./muestras_pruebas/tests1.xlsx", header=None)
        #Las filas que son negativas no dan error, se saltan
        self.assertEqual(0, asistenciaAuxiliar(df, 1, []))

    #Cualquier fila que no cumpla las restricciones se salta y no se hace PDF de ella
    def testDiplomasAutomaticosAsistenciaHorasisNaN(self):
        df = pd.read_excel("./muestras_pruebas/tests2.xlsx", header=None)
        self.assertEqual(0, asistenciaAuxiliar(df, 1, []))
    
    def testDiplomasAutomaticosAsistenciaEventosAsistidosisNaN(self):
        df = pd.read_excel("./muestras_pruebas/tests3.xlsx", header=None)
        self.assertEqual(0, asistenciaAuxiliar(df, 1, []))
    
    def testDiplomasAutomaticosAsistenciaApellidosNoString(self):
        df = pd.read_excel("./muestras_pruebas/tests4.xlsx", header=None)
        self.assertEqual(0, asistenciaAuxiliar(df, 1, []))

    def testDiplomasAutomaticosAsistenciaNombreNoString(self):
        df = pd.read_excel("./muestras_pruebas/tests5.xlsx", header=None)
        self.assertEqual(0, asistenciaAuxiliar(df, 1, []))

    #Test Diplomas Automáticos Custom de Asistencia
    def testDiplomasAutomaticosCustom7Correctos(self):
        df = pd.read_excel("./muestras_pruebas/tests.xlsx", header=None)
        textos = ["INNOSOFT TITULO","confiere el siguiente certificado a:","por su asistencia a ",
        " evento/s durante las jornadas de Innosoft Days","con una dedicación total de "," hora/s","04/01/2021",
        "./resources/images/PLANTILLA.jpg"]
        self.assertEqual(7, asistenciaAuxiliar(df, 2, textos))
    
    def testDiplomasAutomaticosCustomNombreNoString(self):
        df = pd.read_excel("./muestras_pruebas/tests5.xlsx", header=None)
        textos = ["INNOSOFT TITULO","confiere el siguiente certificado a:","por su asistencia a ",
        " evento/s durante las jornadas de Innosoft Days","con una dedicación total de "," hora/s","04/01/2021",
        "./resources/images/PLANTILLA.jpg"]
        self.assertEqual(0, asistenciaAuxiliar(df, 2, textos))
