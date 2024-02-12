class Caneta:
    def __init__(self, cor):
        self.colour = cor
    
    """ 
    # getter    
    def get_cor(self):
        # execute actions
        # such check the attributes values or something else.
        print('Method Getter executed successfully')
        return self.color 
    """
    
    @property
    def color(self):
        print("Executando o metodo getter ")
        return self.colour


if __name__ == "__main__":
    # cliente: parte do programa que executa seu código
    # can be other modules as well
    # private protected public -- attribute use
    pen = Caneta('blue')
    print(pen.color)
    print(pen.color)
    print(pen.color)
    # print(pen.get_cor())
    # print(pen.get_cor())
    # print(pen.get_cor())