import re #regex

def _parse_macro(self):
    self._whileOpen = []
    self._whileIter = 0
    self._iter_lines(self._parse_macro_comm)
    if len(self._whileOpen):
      self._flag = False
      self._errm = "!While not closed!"

def _parse_macro_comm(self, line, p, o):
    if line[0] != "$": #ak nije $ samo return
        return line
    else: #je
        lines = []
        if re.search("^\$MV\((\d|\w)+,(\d|\w)+\)$", line) != None:  #$MV(A,B)
          A = re.split("[(,)]", line)[1] # A
          B = re.split("[(,)]", line)[2] #B
          lines.append("@" + A) # Odi u a spremi vrij
          lines.append("D=M")
          lines.append("@" + B) # odi u b iz a u b spremi vrij
          lines.append("M=D")
          return lines
        elif re.search("^\$SWP\((\d|\w)+,(\d|\w)+\)$", line) != None: #$SWP(A,B)
          A = re.split("[(,)]", line)[1] #A
          B = re.split("[(,)]", line)[2] #B
          lines.append("@" + A) # u A -> ucitaj vrij A
          lines.append("D=M")
          lines.append("@Swap") # Spremi iz  a u swap
          lines.append("M=D")
          lines.append("@" + B) #ucitaj vrij iz b 
          lines.append("D=M")
          lines.append("@" + A) # spremi iz b u a
          lines.append("M=D")
          lines.append("@Swap")
          lines.append("D=M")
          lines.append("@" + B) # spremi iz swap u b
          lines.append("M=D")
        elif re.search("^\$SUM\((\d|\w)+,(\d|\w)+,(\d|\w)+\)$", line) != None: #$SUM(A,B,C)
          A = re.split("[(,)]", line)[1] #a vrij
          B = re.split("[(,)]", line)[2] #b vrij
          D = re.split("[(,)]", line)[3] # d spremi
          lines.append("@" + A) 
          lines.append("D=M")
          lines.append("@" + B)
          lines.append("D=D+M") #zbroj 
          lines.append("@" + D)
          lines.append("M=D") #spremi 
        elif re.search("^\$WHILE\((\d|\w)+\)$", line) != None:
          n = re.split("[()]", line)[1]
          self._whileOpen.append(self._whileIter)
          lines.append("(WHILE" + str(self._whileIter) + ")")
          lines.append("@" + n)
          lines.append("D=M")
          lines.append("@WHILE_END" + str(self._whileIter))
          lines.append("D;JEQ")
          self._whileIter += 1 
        elif re.search("^\$END$", line) != None: #end
          if len(self._whileOpen) == 0:  #greska, nema loopa 
            self._flag = False
            self._line = o
            self._errm = "!Ending non exis. loop!"
          else: 
            n = self._whileOpen.pop() 
            lines.append("@WHILE" + str(n))
            lines.append("0;JMP") #jumpaj
            lines.append("(WHILE_END" + str(n) + ")") #zavrsi
        else: #nije nista od navedenog
            self._flag = False
            self._line = o
            self._errm = "!Invalid macro!"
    return lines # vrati