# Faqat hisoblarni saqlash uchun klass
class Hasaplar:
    """Hasaplar doretmek uchuin klass"""
    def __init__(self,name,code):
        self.name = name
        self.code = code

    def __repr__(self):
        """Hasaplar hakynda maglumat beryan metod"""
        return f"{self.name} {self.code}"
    


# Pravodkalar uchin klass
class Pravodka:
    """Pravodkalar bermek uchin klass"""
    def __init__(self):

        self.dt = 0
        self.kt = 0
        self.__sum_dt = 0
        self.__sum_kt = 0

    def pravodka_DT(self,hasap):
        """Hasaplaryng DT tarapyny yazmak uchin metod"""
        self.dt = hasap
        return self.dt
    
    
    def DT_sum(self,sum):
        """DT hasaolar boyuncha summa"""
        if sum >= 0:
            self.__sum_dt += sum
        else:
            print("0 dan kichi sany girizip bolmayar")
        return self.__sum_dt
    

    def pravodka_KT(self,hasap):
        """Hasaplaryng KT tarapyny yazmak uchin pravodka"""
        self.kt = hasap
        return self.kt
    
    
    def KT_sum(self,sum):
        """KT hasaolar boyuncha summa"""
        if sum >= 0:
            self.__sum_kt += sum
        else:
            print("0 dan kichi sany girizip bolmayar")
        return self.__sum_kt
    
    
    def __repr__(self):
        """Aragatnashykdaky hasaplary gorkezmek"""
        info = "    DT aragatnashyk                                                        KT aragatnashyk\n"
        info +=f"{self.dt}: {self.__sum_dt}                          {self.kt}: {self.__sum_kt}\n"
        info +=f"Jemi:   {self.__sum_dt + self.__sum_kt} manat"
        return info
    
    

