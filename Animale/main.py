import ClasseCane
import ClasseGatto
import io
import sys


GoldenRetriever = ClasseCane.Cane("GoldenRetriever", False, True, 'Canis', 'Panna', 4, True, 10, 'M', "tundra" )
print(GoldenRetriever.volteChiamate())
Bassotto = ClasseCane.Cane("Bassotto",True,False,'Canis', "Marrone", 4, True, 5, 'F', "tundra")
print(Bassotto.volteChiamate())
Sfinge = ClasseGatto.Gatto("Sfinge", False, True, "Felis", "Marroncino", 4, True, 3, 'F')
Sfinge.faiVerso()
Bassotto.faiVerso()
Bassotto.stessoLuogo(GoldenRetriever)

#Catturiamo l'ouptut prima di stamparlo per testare che sia effettivamente quello che ci aspettiamo.
capturedOutput = io.StringIO()
sys.stdout = capturedOutput
sys.stdout = sys.__stdout__
print(capturedOutput)