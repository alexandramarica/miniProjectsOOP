from abc import ABC, abstractmethod #metoda prin care putem crea o clasa abstracta,importam clasa abstracta

class GraditinaABC(ABC): #punem ABC dupa o clasa care stim ca e abstrracta

    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError('Metoda nu este implementata')




