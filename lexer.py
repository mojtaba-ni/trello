from rply import LexerGenerator


class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()  # This is a requiment will be added later

    # Toekens for operators
    self.lexer.add("SUM", r"\+")
    self.lexer.add("SUB", r"\-")
    self.lexer.add("MUL", r"\*")
    self.lexer.add("DIV", r"\/")

    """
        //TODO
        tokens will be completed later on
    """

